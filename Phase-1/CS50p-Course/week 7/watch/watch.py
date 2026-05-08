import re


def main():
    print(parse(input("HTML: ")), end="")


def parse(s):
    s=s.strip()
    url=re.sub(r"^<iframe.+?src=\"", "", s)
    if url == s:
        return None
    url=re.sub(r"\".+", "", url)
    url=re.sub(r"http://", "https://", url)
    if re.search(r"(?:www\.)?youtube\.com/embed/", url):
        url=re.sub(r"(?:www\.)?youtube\.com/embed/", "youtu.be/", url)
        return url
    return None

if __name__ == "__main__":
    main()

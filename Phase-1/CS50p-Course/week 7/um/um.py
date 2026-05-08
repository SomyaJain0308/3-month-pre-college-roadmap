import re


def main():
    print(count(input("Text: ")))


def count(s):
    count=0
    count=count+len(re.findall(r"\bum\b", s , re.IGNORECASE))
    return count


if __name__ == "__main__":
    main()

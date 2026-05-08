import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches:=re.search(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", ip):
        if 0<=int(matches[1])<256 and 0<=int(matches[2])<256 and 0<=int(matches[3])<256 and 0<=int(matches[4])<256:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()

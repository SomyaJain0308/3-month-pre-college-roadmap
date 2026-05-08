import re
import sys


def main():
    print(convert(input("Hours: ")))


time={
    "1 AM":"01",
    "2 AM":"02",
    "3 AM":"03",
    "4 AM":"04",
    "5 AM":"05",
    "6 AM":"06",
    "7 AM":"07",
    "8 AM":"08",
    "9 AM":"09",
    "10 AM":"10",
    "11 AM":"11",
    "12 AM":"00",
    "1 PM":"13",
    "2 PM":"14",
    "3 PM":"15",
    "4 PM":"16",
    "5 PM":"17",
    "6 PM":"18",
    "7 PM":"19",
    "8 PM":"20",
    "9 PM":"21",
    "10 PM":"22",
    "11 PM":"23",
    "12 PM":"12",
}


def convert(s):
    a, b=s.split(" to ")
    if len(a)<9:
        if not re.search(r"AM", a) and not re.search(r"PM",a):
            raise ValueError
        if re.search(r":", a):
            c, d=a.split(":")
            if " AM" in d:
                d=d.replace(" AM", "")
                c=f"{c} AM"
            if " PM" in d:
                d=d.replace(" PM", "")
                c=f"{c} PM"
            if int(d)<60 and len(d)<3:
                first= f"{time[c]}:{d}"
            elif "AM" in d:
                raise ValueError
            elif "PM" in d:
                raise ValueError
            else:
                raise ValueError
    if len(b)<9:
        if not re.search(r"AM", b) and not re.search(r"PM",b):
            raise ValueError
        if re.search(r":", b):
            e, f=b.split(":")
            if " AM" in f:
                f=f.replace(" AM", "")
                e=f"{e} AM"
            if " PM" in f:
                f=f.replace(" PM", "")
                e=f"{e} PM"
            if int(f)<60 and len(f)<3:
                last= f"{time[e]}:{f}"
                return f"{first} to {last}"
            elif "AM" in f:
                raise ValueError
            elif "PM" in f:
                raise ValueError
            else:
                raise ValueError
        elif not re.search(r":", a) and not re.search(r":", b) and re.search("^([01])?[0-9] .M$", a) and re.search("^([01])?[0-9] .M$", b):
            first= f"{time[a]}:00"
            last= f"{time[b]}:00"
            return f"{first} to {last}"
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()

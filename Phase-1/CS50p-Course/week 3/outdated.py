#Hardest problem yet made me think if comsci was even for me or not.

"""
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below.
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""
months={
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12",
    }
while True:
    date=input("Date: ").title().strip()
    if "/" in date:
        m, d, y=date.split("/")
        while True:
            if m.isnumeric():
                break
            else:
                continue
    elif ", " in date:
        C, y=date.split(", ")
        m, d=C.split(" ")
        while True:
            if d.isnumeric():
                break
            else:
                continue
    else:
        continue
    if m.isnumeric():
        if int(m)< 10 and  int(d)<10:
            print(f"{y}-0{m}-0{d}")
            break
        elif 13>int(m)>=10 and int(d)<10:
            print(f"{y}-{m}-0{d}")
            break
        elif 12>=int(m)>=10 and int(d)<=10:
            print(f"{y}-{m}-{d}")
            break
        elif 32>int(d)>=10 and int(m)<10:
            print(f"{y}-0{m}-{d}")
            break
        else:
            continue
    elif m.isalpha():
        if m in months:
            month_num = months[m]
            if int(d)<10:
                print(f"{y}-{month_num}-0{d}", end="")
                break
            elif 10<int(d)<32:
                print(f"{y}-{month_num}-{d}", end="")
                break
            else:
                continue
        break

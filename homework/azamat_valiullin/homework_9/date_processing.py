import datetime

given_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(given_date, "Jan %d, %Y - %H:%M:%S")
print(python_date)

month = python_date.strftime("%B")
print(month)

human_date = datetime.datetime.strftime(python_date, f"%d.%m.%Y, %I:%M %p ")
# pm = python_date.strftime("%p").lower()
# print(f"{human_date}{pm}")
print(human_date)

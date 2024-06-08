import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
destination_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


def file_reader():
    with open(destination_path, "r") as file_list:
        for line in file_list.readlines():
            yield line


date_list = [line[2:29].lstrip() for line in file_reader()]


for index, date_str in enumerate(date_list):
    current_time = datetime.datetime.now()
    if index == 0:
        date1 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        print(f"Date 1 a week later: {date1 + datetime.timedelta(weeks=1)}")
    elif index == 1:
        date2 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        print(f"Date 2 is a {date2.strftime('%A')}")
    elif index == 2:
        date3 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        days_ago = (current_time - date3).days
        print(f"Date 3 was {days_ago} days ago.")

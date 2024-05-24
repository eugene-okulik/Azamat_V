import statistics


temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22,
    23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


def hot_days(n):
    return n > 28


new_list = list(filter(hot_days, temperatures))

if new_list:
    max_temp = max(new_list)
    min_temp = min(new_list)
    average_temp = statistics.mean(new_list)
    print(f"max: {max_temp}, min: {min_temp}, average: {round(average_temp)}")
else:
    print("No temperatures")

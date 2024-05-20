words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    i = 0
    while i < value:
        print(key, end="")
        i += 1
        if i == value:
            break
    print("")

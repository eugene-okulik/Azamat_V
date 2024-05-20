def total_number():
    results = [
        "результат операции: 42",
        "результат операции: 54",
        "результат операции: 209",
        "результат : 2"
    ]
    for result in results:
        if result:
            number = int(result.split(':')[1]) + 10
            print(f"Addition result: {number}")


total_number()


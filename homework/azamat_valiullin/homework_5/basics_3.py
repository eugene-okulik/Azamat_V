# Task 1
person = ["John", "Doe", "New York", "+1372829383739", "US"]
name, last_name, city, phone, country = person
print(f"name: {name}, last_name: {last_name}, phone: {phone}, country: {country}")

# Task 2
results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат операции: 9"
]

result_1 = results[0][results[0].index(":") + 2:]
addition_number_1 = int(result_1) + 10
print(f"Total number: {addition_number_1}")

result_2 = results[1][results[0].index(":") + 2:]
addition_number_2 = int(result_2) + 10
print(f"Total number: {addition_number_2}")

result_3 = results[2][results[0].index(":") + 2:]
addition_number_3 = int(result_3) + 10
print(f"Total number: {addition_number_3}")

# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_all = ", ".join(students)
subjects_all = ", ".join(subjects)
print(f"Students {students_all} study these subjects: {subjects_all}")

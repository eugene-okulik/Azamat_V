import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создайте студента (student)

cursor.execute("""
INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)
""", ('test name', 'test surname', None))
student_id = cursor.lastrowid
print(f"Student id: {student_id}")

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    query, [
        ('Test book1', student_id),
        ('Test book2', student_id)
    ]
)

# Создайте группу (group) и определите своего студента туда

query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('test group', '2023', '2025')
cursor.execute(query, values)
group_id = cursor.lastrowid
print(f"Group id: {group_id}")

query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)

# Создайте несколько учебных предметов (subjects)

cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ("Test subject1",))
subject1_id = cursor.lastrowid
print(f"Subject 1 id: {subject1_id}")

cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ("Test subject2",))
subject2_id = cursor.lastrowid
print(f"Subject 2 id: {subject2_id}")

# Создайте по два занятия для каждого предмета (lessons)

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('test lesson1', subject1_id))
lesson1_id = cursor.lastrowid
print(f"Lesson1 id: {lesson1_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('test lesson2', subject1_id))
lesson2_id = cursor.lastrowid
print(f"Lesson2 id: {lesson2_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('test lesson3', subject2_id))
lesson3_id = cursor.lastrowid
print(f"Lesson3 id: {lesson3_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('test lesson4', subject2_id))
lesson4_id = cursor.lastrowid
print(f"Lesson4 id: {lesson4_id}")


# Поставьте своему студенту оценки (marks) для всех созданных вами занятий

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query, [
        ('test value1', lesson1_id, student_id,),
        ('test value2', lesson2_id, student_id,),
        ('test value3', lesson3_id, student_id,),
        ('test value4', lesson4_id, student_id,)
    ]
)

db.commit()

# Получите информацию из базы данных:
# Все оценки студента

student_grades = """
SELECT s.id, s.name , s.second_name , m.value , m.lesson_id
FROM students s
INNER JOIN marks m ON s.id = m.student_id
WHERE s.id = %s;
"""

cursor.execute(student_grades, (student_id,))
for student_grades in cursor.fetchall():
    print(f"Student grades: {student_grades}")

print("*" * 200)

# Все книги, которые находятся у студента

student_books = """
SELECT s.id, s.name , s.second_name , b.title
FROM students s
RIGHT JOIN books b on s.id = b.taken_by_student_id
WHERE s.id = %s;
"""

cursor.execute(student_books, (student_id,))
for student_books in cursor.fetchall():
    print(f"Student books: {student_books}")

print("*" * 200)

"""
Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий
и предметов (всё одним запросом с использованием Join)
"""

student_all = """
SELECT s.id, s.name, s.second_name, g.title, g.start_date, g.end_date, s2.title, l.title, l.subject_id,
m.value, m.lesson_id, b.title
FROM students s
left join `groups` g on s.group_id = g.id
left join marks m on s.id = m.student_id
left join lessons l on m.lesson_id = l.id
left join subjets s2 on l.subject_id = s2.id
left join books b on s.id = b.taken_by_student_id
WHERE s.id = %s;
"""
cursor.execute(student_all, (student_id,))
for student_all in cursor.fetchall():
    print(f"Student all: {student_all}")


db.close()

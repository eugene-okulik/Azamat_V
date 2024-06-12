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

query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('test name', 'test surname')
cursor.execute(query, values)

student_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM students WHERE id = {student_id}")
student = cursor.fetchone()
student_id = student['id']
print(f"Student id: {student_id}")

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    query, [
        ('Test book1', student_id),
        ('Test book2', student_id)
    ]
)

cursor.execute("SELECT * FROM books ORDER BY id DESC LIMIT 1")
book2 = cursor.fetchone()
book2_id = book2['id']
print(f"Book2 id: {book2_id}")


cursor.execute("SELECT * FROM books ORDER BY id DESC LIMIT 1, 1")
book1 = cursor.fetchone()
book1_id = book1['id']
print(f"Book1 id: {book1_id}")

# Создайте группу (group) и определите своего студента туда

query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('test group', '2023', '2025')
cursor.execute(query, values)

group_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM `groups` WHERE id = {group_id}")
group = cursor.fetchone()
group_id = group['id']
print(f"Group id: {group_id}")

query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)

# Создайте несколько учебных предметов (subjects)

query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    query, [
        ("Test subject1",),
        ("Test subject2",)
    ]
)

cursor.execute("SELECT * FROM subjets ORDER BY id DESC LIMIT 1")
subject2 = cursor.fetchone()
subject2_id = subject2['id']
print(f"Subject2 id: {subject2_id}")

cursor.execute("SELECT * FROM subjets ORDER BY id DESC LIMIT 1, 1")
subject1 = cursor.fetchone()
subject1_id = subject1['id']
print(f"Subject1 id: {subject1_id}")

# Создайте по два занятия для каждого предмета (lessons)

query = "INSERT INTO lessons (title, subject_id) values (%s, %s)"
cursor.executemany(
    query, [
        ('test lesson1', subject1_id),
        ('test lesson2', subject2_id)
    ]
)

cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 1")
lesson2 = cursor.fetchone()
lesson2_id = lesson2["id"]
print(f"Lesson2 id: {lesson2_id}")

cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 1, 1")
lesson1 = cursor.fetchone()
lesson1_id = lesson1['id']
print(f"Lesson1 id: {lesson1_id}")


# Поставьте своему студенту оценки (marks) для всех созданных вами занятий

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query, [
        ('test value1', lesson1_id, student_id,),
        ('test value2', lesson2_id, student_id,)
    ]
)

cursor.execute("SELECT * FROM marks ORDER BY id DESC LIMIT 1")
marks2 = cursor.fetchone()
marks2_id = marks2['id']
print(f"Marks2 id: {marks2_id}")

cursor.execute("SELECT * FROM marks ORDER BY id DESC LIMIT 1, 1")
marks1 = cursor.fetchone()
marks1_id = marks1['id']
print(f"Marks1 id: {marks1_id}")
db.commit()

# Получите информацию из базы данных:
# Все оценки студента

student_grades = f"""
SELECT s.id, s.name , s.second_name , m.value , m.lesson_id
FROM students s
INNER JOIN marks m ON s.id = m.student_id
WHERE s.id = {student_id};
"""
cursor.execute(student_grades)
for student_grades in cursor.fetchall():
    print(f"Student grades: {student_grades}")

print("*" * 200)

# Все книги, которые находятся у студента

student_books = f"""
SELECT s.id, s.name , s.second_name , b.title
FROM students s
RIGHT JOIN books b on s.id = b.taken_by_student_id
WHERE s.id = {student_id};
"""

cursor.execute(student_books)
for student_books in cursor.fetchall():
    print(f"Student books: {student_books}")

print("*" * 200)

"""
Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий
и предметов (всё одним запросом с использованием Join)
"""

student_all = f"""
SELECT s.id, s.name, s.second_name, g.title, g.start_date, g.end_date, s2.title, l.title, l.subject_id,
m.value, m.lesson_id, b.title
FROM students s
left join `groups` g on s.group_id = g.id
left join marks m on s.id = m.student_id
left join lessons l on m.lesson_id = l.id
left join subjets s2 on l.subject_id = s2.id
left join books b on s.id = b.taken_by_student_id
WHERE s.id = {student_id};
"""
cursor.execute(student_all)
for student_all in cursor.fetchall():
    print(f"Student all: {student_all}")


db.close()

import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'))

cursor = db.cursor()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
destination_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")


with open(destination_path, "r", newline="") as data_file:
    reader = csv.reader(data_file)
    next(reader)

    for row in reader:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

        query = """
        SELECT s.name, s.second_name, g.title, b.title, s2.title, l.title, m.value
        FROM students s
        JOIN `groups` g ON s.group_id = g.id
        JOIN books b ON s.id = b.taken_by_student_id
        JOIN marks m ON s.id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjets s2 ON l.subject_id = s2.id
        WHERE s.name = %s
        AND s.second_name = %s
        AND g.title = %s
        AND b.title = %s
        AND s2.title = %s
        AND l.title = %s
        AND m.value = %s
        """
        values = (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)
        data = cursor.execute(query, values)

        data_result = cursor.fetchall()

        if not data_result:
            print(f"Not found in DB: {row}")


db.close()

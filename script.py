# SQL

# What is SQL - Its a programming languageused to manage relational database.


#  Installing and setting up sqlite
# sudo apt install sqlite3
# sqlite3 --version

# Connect db
# Insert values to the db using SQL
# Retriving values from the db SQL running queries

# Datatypes In SQL
# NULL -  on values
# TEXT 
# INTEGER
# REAL - Decimals
# BLOB - Binary data 

import sqlite3
from students import Student

conn = sqlite3.connect('students.db')

# cursor object
c = conn.cursor()

# Creating a table
# c.execute(""" CREATE TABLE students (
#           first_name text,
#           last_name text,
#           grade integer
#           )""")

# Inserting values to the table 
# c.execute("INSERT INTO students VALUES ('Leon', 'Kipchumba', 88)")

# Retriving values from the db
c.execute(" SELECT * FROM students WHERE last_name= 'Kipchumba'")
print(c.fetchall())



# Insert multiple students
students = [
    {'first_name': 'Timon', 'last_name': 'Kosgei', 'grade': 90},
    {'first_name': 'Michelle', 'last_name': 'Wairimu', 'grade': 78},
    {'first_name': 'Felicia', 'last_name': 'Kwame', 'grade': 72},
    {'first_name': 'Damaris', 'last_name': 'Kerubo', 'grade': 82},
]


# for student in students:
#     c.execute("INSERT INTO students VALUES (?, ?, ?)", (student['first_name'], student['last_name'],student['grade']))


# c.execute("SELECT * FROM students")
# results = c.fetchall()

# for record in results:
#     print(record)

# Creating students objects

std_one = Student("James", "Kungu", 78)
std_two = Student("Grace", "Mwangi", 76)


# CRUD Basics
# Creating function queries
def insert_std(std):
    with conn:
        c.execute("INSERT INTO students VALUES('{}', '{}', '{}')".format(std.first_name, std.last_name, std.grade))

def get_std_name(first_name, last_name):
    c.execute("SELECT * FROM students WHERE first_name = ? AND last_name = ?", (first_name, last_name))
    return c.fetchall()

def update_grade(std, grade):
    with conn:
        c.execute("UPDATE students SET grade = ? WHERE first_name = ? AND last_name = ?",
              (grade, std.first_name, std.last_name))
        
def remove_std(std):
    with conn:
        c.execute("DELETE FROM students WHERE first_name = ? AND last_name = ?", (std.first_name, std.last_name))


# Calling functions
# insert_std(std_one)
# insert_std(std_two)
        
student_results = get_std_name("Timon", "Kosgei")
print(student_results)


# update_grade(std_two, 96)

remove_std(std_one)


conn.commit()
conn.close()
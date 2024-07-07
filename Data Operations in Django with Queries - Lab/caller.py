import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student
# Import your models here
# Run and print your queries

# def add_students():
#     student1 = Student(
#         student_id='FC5204',
#         first_name='John',
#         last_name='Doe',
#         birth_date='1995-05-15',
#         email='john.doe@university.com'
#     )
#     student1.save()

#     student2 = Student(
#         student_id='FE0054',
#         first_name='Jane',
#         last_name='Smith',
#         birth_date=None,
#         email='jane.smith@university.com'
#     )
#     student2.save()

#     student3 = Student(
#         student_id='FH2014',
#         first_name='Alice',
#         last_name='Johnson',
#         birth_date='1998-02-10',
#         email='alice.johnson@university.com'
#     )
#     student3.save()

#     student4 = Student(
#         student_id='FH2015',
#         first_name='Bob',
#         last_name='Wilson',
#         birth_date='1996-11-25',
#         email='bob.wilson@university.com'
#     )
#     student4.save()

    
# add_students()
# print(Student.objects.all())


# def get_students_info():
#     students = Student.objects.all()
#     result = ""

#     for student in students:
#         result += f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}\n"

#     return result

# print(get_students_info())


# def update_students_emails():
#     students = Student.objects.all()

#     for student in students:
#         first_part, second_part = student.email.split('@')
#         second_part = '@uni-students.com'
#         student.email = first_part + second_part
#         student.save()


# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)


def truncate_students():
    Student.objects.all().delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")

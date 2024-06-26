import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student
# Run and print your queries

def add_students():
    s1 = Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com')
    
    s2 = Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com')
    
    s3 = Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com')
    
    s4 = Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com')

# add_students()
# print(Student.objects.all())

def get_students_info():
    student_data = []

    for s in Student.objects.all():
        student_data.append(f"Student №{s.student_id}: {s.first_name} {s.last_name}; Email: {s.email}")
    
    return '\n'.join(student_data)

# print(get_students_info())

def update_students_emails():
    
    for s in Student.objects.all():
        email_parts = s.email.split("@")
        new_email = f"{email_parts[0]}@uni-students.com"
        s.email = new_email
        s.save()

    # for s in Student.objects.all():
    #     new_email = s.email.replace('university.com', 'uni-students.com')
    #     s.email = new_email
    #     s.save()

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

def truncate_students():
    Student.objects.all().delete()

# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")

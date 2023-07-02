# subject_module.py
class Subject:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
# Create a Subject object
Subject = Subject("Math",90)

# Access the attributes
print(Subject.name)  # Output: Math
print(Subject.name)  #Output : 90
#q : 2
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []
        # student_module.py

        class Student:
            def __init__(self, name, age, city):
                self.name = name
                self.age = age
                self.city = city
                self.marks = []

            def add_mark(self, mark):
                self.marks.append(mark)

            def get_all_marks(self):
                return self.marks

            def calc_average(self):
                if len(self.marks) == 0:
                    return 0
                return sum(self.marks) / len(self.marks)
 # q : 3
# main.py
# main.py

import subject_module
import student_module

# Create objects of the Subject class
subject1 = subject_module.Subject("Mathematics")
subject2 = subject_module.Subject("Science")
subject3 = subject_module.Subject("English")

# Create objects of the Student class
student1 = student_module.Student("John Doe", 18, "New York")
student2 = student_module.Student("Jane Smith", 17, "Los Angeles")
student3 = student_module.Student("Mike Johnson", 16, "Chicago")

# Accessing attributes of the objects
print(subject1.name)  # Output: Mathematics
print(student1.name)  # Output: John Doe

# Adding marks for students
student1.add_mark(85)
student1.add_mark(90)
student2.add_mark(78)
student2.add_mark(92)
student3.add_mark(80)

# Getting all marks for a student
print(student1.get_all_marks())  # Output: [85, 90]

# Calculating the average mark for a student
average_mark_student1 = student1.calc_average()
print(average_mark_student1)  # Output: 87.5


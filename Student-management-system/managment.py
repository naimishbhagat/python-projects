class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    
    def display_info(self):
        print(f"Name: {self.name}, age: {self.age}, roll: {self.roll_number}")


class School:
    def __init__(self):
        self.students = []
    
    def add_student(self,name,age,roll_number):
        student = Student(name,age,roll_number)
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            student.display_info()

    def edit_student(self, roll_number,new_name,new_age):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = new_name
                student.age = new_age
                print(f"Student {student.name} successsfully updated")
                return
    def delete_student(self,roll_number):
         for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student successsfully removed")
                return
   
school = School()
while True:
    choice = input("Enter your choice: \n1) Add student \n2)Display list of students\n3)Edit Data of Student\n4)Delete Student\n5)Quit\n")
    if choice == "1":
        name = input("Enter name of the student: ")
        age = input("Enter age of the student: ")
        roll_number = input("Enter roll number of the student: ")
        school.add_student(name,age,roll_number)
    elif choice == "2":
        school.display_students()
    elif choice == "3":
        roll_number = input("Enter roll number which you want to edit: ")
        new_name =  input("Enter new name of the student: ")
        new_age = input("Enter new age of the student: ")
        school.edit_student(roll_number,new_name,new_age)
    elif choice == "4":
        roll_number = input("Enter roll number which you want to delete: ")
        school.delete_student(roll_number)
    elif choice == "5":
        break
    
#Assignment - 2
# Write a program with
# Student class to store the data of student (like name, rollno, age and gender)
# as parameter
# Mark class takes the marks of different subject
# Display class will print the name, rollno and totalmark
class Student:
    def __init__(self, name, roll_no, age, gender):
        self.name = name
        self. roll_no = roll_no
        self.age = age
        self.gender = gender
class Mark(Student):
    def __init__(self, sub1, sub2, name, roll_no, age, gender):
        self.sub1 = sub1
        self.sub2 = sub2
        Student.__init__(self, name, roll_no, age, gender)
class Display(Mark):
    def __init__(self , sub1, sub2, name, roll_no, age, gender ):
        Mark.__init__(self, sub1, sub2, name, roll_no, age, gender )
        self.total = sub1 + sub2
    def print_output(self):
        print("NAME:", self.name)
        print("ROLL_NUMBER:", self.roll_no)
        print("TOTAL:", self.total)
Sub1=int(input("enter the Chemistry mark=",))
Sub2=int(input("enter the Maths mark=",))
name=str(input("enter the name=",))
roll_no=int(input("enter roll_number=",))
age=int(input("enter age=",))
gender=str(input("enter the gender=",))
ob=Display(Sub1 ,Sub2, name, roll_no, age, gender)
ob.print_output()
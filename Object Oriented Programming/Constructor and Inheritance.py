class Person:
    def __init__(self,name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def eat(self):      # 'self' key word refer to this class
        print("eating")

    def walk(self):
        print("walking")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Student(Person):  # Inheritance example 'class get properities of other class'
    ID = ""
    name = ""
                        #if you create new constructor in this class, you can't user the constructor of other class
    def mark(self):
        print("Mark is good")

student = Student("Mohanned",20,"Male",8774)
student.walk()
student.mark()

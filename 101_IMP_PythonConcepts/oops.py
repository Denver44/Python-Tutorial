class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def getmarks(self):
        return self.marks


class Course:
    def __init__(self, coursename, max_student):
        self.course = coursename
        self.max = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max:
            self.students.append(student)
            return True
        return False

    def getaverage(self):
        sum = 0
        for student in (self.students):
            sum += student.getmarks()

        return  sum / len(self.students)


s1 = Student("Durgesh", 21, 50)
s2 = Student("Vishal", 20, 50)
s3 = Student("Harshil", 22, 50)

# print(s2.getmarks())

c = Course("science", 3)
c.add_student(s1)
c.add_student(s2)
c.add_student(s3)
print(c.getaverage())

c2 = Course("commerce",3)
c2.add_student(s1)
c2.add_student(s2)
c2.add_student(s3)
print(c2.getaverage())
class students:

    def __init__(self,first,last,marks,sex):
        self.first=first
        self.last=last
        self.marks=marks
        self.sex=sex

class Dumb(students):
    pass

print(help(Dumb))

#stu_1= students("Mohan","pigelati",30,"M")
#stu_2= students("Thanuja","pigelati",6,"F")

#print(stu_1.first)
#print(stu_1.first)
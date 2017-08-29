class students:
    #perc_rise = 1.05
    def __init__(self,first,last,marks,sex):
        self.first=first
        self.last=last
        self.marks=marks
        self.sex=sex

    def fill_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):

        self.marks=self.marks*1.05

class Dumb(students):
    perc_rise=1.10

    def __init__(self,first,last,marks,sex,language):
        super().__init__(first,last,marks,sex)
        self.language=language


#print(help(Dumb))

stu_1= Dumb("Mohan","pigelati",30,"M","python")
stu_2= students("Thanuja","pigelati",60,"F")

print(stu_1.language)
print(stu_1.perc_rise)
print(stu_1.marks)
(stu_2.apply_raise())
print(stu_2.marks)
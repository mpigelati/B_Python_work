class student:
    def __init__(self,first,last,sex,marks):

        self.first=first
        self.last=last
        self.sex=sex
        self.marks=marks

    # this is method, Method is nothing but functions

    """Each method in side a class automatically takes instance as an first argument, for ex :- stu_1,stu_2 are instances we are going always
    call that self an instance is the only argument that we need  for full name"""

    def full_name(self):

       return '{} {}'.format(self.first,self.last)



# here the stu_1 and stu_2 are instance
stu_1=student("Mohan","pigelati","M",30)
stu_2=student("Thanuja","pigelati","M",55)

print(stu_1.__class__)
print(stu_1.full_name())
print(stu_2.full_name())
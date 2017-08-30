class Employee :

    number_emp=0
    hick_amount = 1.04

    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname = lname
        self.pay = pay
        Employee.number_emp+=1

    def apply_hick(self):
        self.pay= int(self.pay*self.hick_amount)
        #self.pay = int(self.pay * Employee.hick_amount)

emp=Employee("Mohansai","pigelati",60000)
emp2=Employee("Thanuja","pigelati",69000)
print(emp.pay)
emp.apply_hick()
print(emp.pay)

print(Employee.number_emp)

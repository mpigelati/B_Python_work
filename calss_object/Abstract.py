from abc import ABC, abstractmethod

class Employee(ABC):

     @abstractmethod

     def claculate(self,sal):
        pass

class Developer(Employee):

    def claculate(self,sal):

        finalsal= sal*1.10
        return  finalsal

emp_1= Developer()

print(emp_1.claculate(100000))
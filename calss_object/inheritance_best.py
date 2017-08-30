class pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class cat(pet):
    def __init__(self,name,age,status):
        super().__init__(name,age)
        self.status=status

def Main():
    print("hellow")
    mypet=pet("jack",2)
    jess=cat("bru",3,"dead")

    print("is jess a cat?" +str(isinstance(jess,cat)))
    print(jess.name)
    print(jess.status)
#if __name__ == '__main__':
if __name__ == '__main__':
    Main()

























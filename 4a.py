class student:
    def __init__(self):
        self.id =" "
        self.age = 0
        self.mark = 0
    def validatemarks(self):
        if self.mark>0 and self.mark<100:
            return True
        else:
            return False
    def validateage(self):
        if self.age>20:
            return True
        else:
            return False
    def check_quali(self):
        if self.validatemarks()and self.validateage():
            if self.mark>=65:
                return True
            else:
                return False
        else:
            return False
    def setter(self):
        self.name=int(input("enter id"))
        self.age=int(input("enter age"))
        self.mark=int(input("enter mark"))
    def getter(self):
        print("id",self.id)
        print("age",self.age)
        print("mark",self.mark)
        if self.check_quali():
            print("given information is valild")
        else:
            print("invalid info")

s1=student()
s1.setter()
s1.getter()




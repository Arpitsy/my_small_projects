class student:
    def __init__(self,name,marks):
        self.name=name

        self.marks=marks
    def is_pass(self):
        if int(self.marks)>=40:
            print("you have passed")  
        else:
            print("You have failed")

a=student("zoro","35")
b=student("obito","86")
b.is_pass()

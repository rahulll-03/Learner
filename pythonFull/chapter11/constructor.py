class Employee:
    def __init__(self):
        print("i am constructor Employee")

class Programmer(Employee):
    def __init__(self):
        print("i am program")
        super().__init__()
        print("done")


p=Programmer()
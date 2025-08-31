class Employee:
    name = "default"
    salary = 120000
    def show(self):
        print(f"The name is {self.name} and Salary is {self.salary}")


class Coder:
        language = "Python"
        def printLanguage(self):
                print(f"Out of all language here is your language {self.language}")

class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
                print(f"The name is {self.name} and language is {self.company}")


            
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
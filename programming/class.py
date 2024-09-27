# class

class Car:
    def __init__(self, name, gear, miles):
        self.name = name
        self.gear = gear
        self.miles = miles

    def drive(self, miles):
        self.miles = self.miles + miles

    def shift_gear(self, gear):
        self.gear = gear

car = Car("Tesla", 0, 0)
car.shift_gear(6)
print(car.gear)

#del 
del car

# object oriented programming
# inheritance

class Employee:
    def __init__(self, name, age, dob, job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.job_description = job_description

    def get_salary(self):
        print("salary printed")

class Manager(Employee):
    def __init__(self, name, age, dob, job_description, department, employee):
        super().__init__(name, age, dob, job_description)
        self.department = department
        self.employee = employee

    def add_employee(self):
        print("adding employee")

    def get_salary(self):
        print("salary printed for manager")

manager = Manager("kim", 28, "23-8-2000", "manages every thing", "engineering department", 87)

manager.get_salary()
manager.add_employee()
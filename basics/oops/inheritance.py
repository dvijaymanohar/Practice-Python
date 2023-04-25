
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.__priv = id

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print("My name is {}".format(self.name))
        print("My id is {}".format(self.id))


class Employee(Person):
    def __init__(self, name, id, JobFunction):
        self.name = name
        self.id = id
        self.JobFunction = JobFunction

        # Person.__init(self, name, id)

    def details(self):
        print("My name is {}".format(self.name))
        print("My id is {}".format(self.id))
        print("Job function is {}".format(self.JobFunction))


emp = Employee("VMD", "601", "Software Engineering")
emp.display()
emp.details()
print("Private variable: {}".format(emp.__priv))

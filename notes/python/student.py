class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return ("Name: {}, Age: {}".format(self.name, str(self.age)))


student1=Student("Rick", 20)
student2=Student("Jason", 19)

print(student1)
print(student2)
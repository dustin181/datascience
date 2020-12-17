class Animal:
    def __init__(self, color):
        self.color=color

    def introduce(self):
        print("Hello I am an animal")

    def makeSound(self):
        print("making sound!")

class Dog(Animal):
    def takeCare(self):
        print("I am taking care of you")
    def makeSound(self):
        print("bark bark!")


animal1=Animal("red")
animal2=Animal("green")

animal3=Dog("yellow")

animal1.introduce()
animal1.makeSound()
animal2.introduce()
animal2.makeSound()
animal3.introduce()
animal3.makeSound()
animal3.takeCare()
class Car:
    def __init__(self, mileage, color):
        self.mileage=mileage
        self.color=color

    def __str__(self):
        return ("Mileage: {}, Color: {}".format(self.mileage, str(self.color)))

    def getMileage(self):
        return self.mileage

    def getColor(self):
        return self.color

    def greet(self):
        print("Hello I am a car")


model1 = Car(55,"Red")
model2 = Car(60, "Blue")

print(model1)
print("Mileage: " + str(model2.getMileage()) + ", Color: " + model2.getColor())






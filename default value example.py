class Car():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.reading=0
        
    def describe(self):
        print(f"The name of the vehicle is {self.name} and it's age is {self.age}.")
        print("-------------------")
    
    def running(self):
        print(f"It has reading of {self.reading} miles at the moment.")
        
mycar=Car("Mercedes","13-months")

mycar.running()
print("-------------------")
mycar.reading=30

mycar.running()

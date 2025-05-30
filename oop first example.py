class Restaurant():
    def __init__(self, name,cuisine,location,giveaway):
        self.name=name
        self.cuisine=cuisine
        self.location=location
        self.giveaway=giveaway
        self.entrance_price=0
        
    def describe(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"The favourite dish of the restaurant is {self.cuisine}.")
        print(f"The location of the restaurant is  {self.location}.")
        print(f"The price for loyal visitors of the restaurant is {self.giveaway}.")
        print(f"The entrance price of the restaurant is {self.entrance_price}")
        
    


restaurant1=Restaurant('Ram','specialchat','Bharatpur','watch',)
restaurant2=Restaurant('Hari','Chowemein','Ratnanagar','money',)

print(restaurant1.describe())
print("------------------------")
print(restaurant2.describe())
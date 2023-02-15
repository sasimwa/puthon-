class Vehicle():
    def __init__(self ,model,owner,price,color):
        self.model = model
        self.owner = owner
        self.price = price
        self.color = color
Vehicle_owner_one = Vehicle("Toyota","Caleb","4M","Blue")
print(Vehicle_owner_one.model)
print(Vehicle_owner_one.owner)
print(Vehicle_owner_one.price)
print(Vehicle_owner_one.color)

print("--------------End of owner 1--------------")

Vehicle_owner_two = Vehicle("Mitsubishi","Joy","6M","White")
print(Vehicle_owner_one.model)
print(Vehicle_owner_one.owner)
print(Vehicle_owner_one.price)
print(Vehicle_owner_one.color)

print("--------------End of owner 2--------------")

Vehicle_owner_three = Vehicle("Jeep","Roy","10M","Orange")
print(Vehicle_owner_one.model)
print(Vehicle_owner_one.owner)
print(Vehicle_owner_one.price)
print(Vehicle_owner_one.color)

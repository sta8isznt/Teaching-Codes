class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        attribute = f"{self.restaurant_name} {self.cuisine_type}"
        return attribute.title()
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")
    
restaurant = Restaurant("iiiiiiiiiiiii", "souvlatzidiko")
print(restaurant.describe_restaurant())

print(restaurant.open_restaurant())

first_restaurant = Restaurant("dddddddddd", "mexikaniko")
print(first_restaurant.describe_restaurant())

second_restaurant = Restaurant("aaaaaaaaaaaaaaaa", "italiko")
print(second_restaurant.describe_restaurant())
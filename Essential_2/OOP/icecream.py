class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        attribute = f"{self.restaurant_name} {self.cuisine_type}"
        return attribute.title()
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

my_icecream_stand = IceCreamStand("Gellato", "Icecream", ["Choco", "Cherry"])
my_icecream_stand.show_flavors()

    

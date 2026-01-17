class Car:                    # ALL in ONE place
    def __init__(self, color,fuel):
        self.color = color    # THIS car's data
        self.fuel = fuel
    
    def drive(self):          # Works on THIS car
        self.fuel -= 10

my_car = Car("ee",1)           # Independent car
your_car = Car("ee",1)        # Independent car
my_car.drive()                # Only affects my_car!

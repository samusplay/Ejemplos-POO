class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"The car {self.model} has been sold.")
        else:
            print(f"The car {self.model} is not available.")

    def make_available(self):
        self.is_available = True
        print(f"The car {self.model} is available for sale.")


class Customer:
    def __init__(self, name, id_customer):
        self.name = name
        self.id_customer = id_customer
        self.cars_sold = []

    def buy_car(self, car):
        if car.is_available:
            car.sell()
            self.cars_sold.append(car)
        else:
            print(f"The car {car.model} is not available.")

    def return_car(self, car, concessionaire):
        if car in self.cars_sold:
            car.make_available()
            self.cars_sold.remove(car)
            concessionaire.add_car(car)
            print(f"The car {car.model} has been returned to the concessionaire.")
        else:
            print(f"The car {car.model} is not in the shopping list.")


class Concessionaire:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"The car {car.model} has been added to the inventory.")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added to the registry.")

    def show_cars_available(self):
        print("Available cars:")
        for car in self.cars:
            if car.is_available:
                print(f"{car.model} for ${car.price}")




# Create objects cars
car1 = Car("DeLorean", 1500)
car2 = Car("Chevrolet", 900)

# Create customer
customer1 = Customer("Samuel", "001")

# Create concessionaire
concessionaire = Concessionaire()
concessionaire.add_car(car1)
concessionaire.add_car(car2)
concessionaire.register_customer(customer1)

# Show available cars
concessionaire.show_cars_available()

# Customer buys a car
customer1.buy_car(car1)

# Show available cars again
concessionaire.show_cars_available()

# Customer returns the car
customer1.return_car(car1, concessionaire)

# Show available cars after return
concessionaire.show_cars_available()


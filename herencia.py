class Vehicule:
    def __init__(self, brand, model, price):
        #Encapsulacion 
        self.brand = brand 
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} no está disponible")

#Abstraccion
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    # Abstraccion
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


# Clase que hereda de Vehicule
class Car(Vehicule):
    # Polimorfismo muchas formas pero comportamiento diferente
    def start_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"

# Herencia
class Bike(Vehicule):
    def start_engine(self):
        #polimorfismo
        if self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"


class Truck(Vehicule):
    def start_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El motor del camión {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El motor del camión {self.brand} no está disponible"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicule: Vehicule):
        if vehicule.check_available():
            vehicule.sell()
            self.purchased_vehicles.append(vehicule)
            print(f"{self.name} ha comprado el vehículo {vehicule.brand}.")
        else:
            print(f"Lo siento, {vehicule.brand} no está disponible")
    
    def inquire_vehicle(self, vehicle: Vehicule):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El {vehicle.brand} está {availability} y cuesta {vehicle.get_price()}")


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicule):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicles(self):
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

# Crear instancias de vehículos y clientes
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

# Crear una instancia del concesionario
dealership = Dealership()

# Agregar vehículos al inventario del concesionario
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

# Mostrar vehículos disponibles en el concesionario
dealership.show_available_vehicles()

#Cliente Consultar un vehiculo

customer1.inquire_vehicle(car1)

# Cliente comprar un vehiculo

customer1.buy_vehicle(car1)

# Mostrar vehículos disponibles en el concesionario
dealership.show_available_vehicles()



                       

        






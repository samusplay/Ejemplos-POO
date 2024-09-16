# Definimos una clase llamada BankAccount (Cuenta Bancaria).
# Una clase es como un plano o molde que describe cómo debe ser un objeto.
class BankAccount:

    # Este es el método especial __init__. Se ejecuta automáticamente cada vez que creamos una nueva instancia de la clase.
    # Es como un constructor que establece las propiedades (variables) iniciales del objeto.
    def __init__(self, account_holder, balance):
        # 'self' se refiere al objeto actual que se está creando.
        # Aquí estamos definiendo dos propiedades (atributos) del objeto: el titular de la cuenta y el saldo.
        self.account_holder = account_holder  # Guardamos el nombre del titular de la cuenta.
        self.balance = balance  # Guardamos el saldo inicial de la cuenta.
        self.is_active = True  # Creamos una propiedad que indica si la cuenta está activa o no.

    # Este es un método llamado depositar (deposit).
    # Un método es como una función que pertenece a una clase y define lo que el objeto puede hacer.
    def deposit(self, amount):
        # Primero, verificamos si la cuenta está activa.
        if self.is_active:
            # Si la cuenta está activa, sumamos el monto del depósito al saldo actual.
            self.balance += amount
            # Mostramos un mensaje indicando cuánto se depositó y el saldo actual.
            print(f'Se ha depositado {amount}. Saldo actual: {self.balance}')
        else:
            # Si la cuenta no está activa, mostramos un mensaje de error.
            print('No se puede depositar, cuenta inactiva')

# Resumen rápido de POO:
# 1. **Clases**: Son como plantillas para crear objetos. Definen atributos y métodos.
# 2. **Objetos**: Son instancias de clases. Cada objeto creado tiene sus propias propiedades y puede realizar acciones definidas por los métodos.
# 3. **Atributos**: Son variables que pertenecen a un objeto.
# 4. **Métodos**: Son funciones que pertenecen a un objeto y describen su comportamiento.

# Ejemplo: Si creamos un objeto de la clase BankAccount, como "mi_cuenta = BankAccount('Samuel', 1000)",
# "mi_cuenta" tendrá un titular ('Samuel'), un saldo inicial (1000), y podrá usar el método 'deposit' para aumentar su saldo.
      
    def withdraw(self,amount):
        if self.active:
            if amount<=self.balance:
                self.balance-=amount
                print(f"Se ha retirado{amount}.Saldo actual{self.balance}")

    def desactivate_account(self):
        self.is_active=False
        print(f"la cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active=True
        print(f"la cuenta ha sido activada")

               
account1=BankAccount("Ana",500)
account2=BankAccount("luis",1000)

#llamada a los metodos

account1.deposit(200)
account2.deposit(100)
account1.desactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)




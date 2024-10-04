# Project No.: 4
# Author: Tobyn Wietfeldt
# Description: Car dealership app

# Super Class
class Car:
    # Initializing
    def __init__(self, brand, model, year, price, car_type):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__type = car_type

    # Setters and getters
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_type(self):
        return self.__type

    def set_type(self, car_type):
        self.__type = car_type

    # Super print method (overridden by subclasses using polymorphism)
    def print_info(self):
        print(f"{self.__brand:<10} {self.__model:<15} {self.__year:<6} {self.__price:<10,.2f} {self.__type:<10}", end=" ")


# Import cars (Sub-class)
class ImportCar(Car):
    # Initializing
    def __init__(self, brand, model, year, price, car_type, country, tax):
        super().__init__(brand, model, year, price, car_type)
        self.__country = country
        self.__tax = tax

    # Setters and getters
    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_tax(self):
        return self.__tax

    def set_tax(self, tax):
        self.__tax = tax

    # Overriding old method for printing info
    def print_info(self):
        super().print_info()
        print(f"{self.__country:<10} {self.__tax}%")


# Domestic cars (Sub-class)
class DomesticCar(Car):
    # Initializing
    def __init__(self, brand, model, year, price, car_type, state):
        super().__init__(brand, model, year, price, car_type)
        self.__state = state

    # Setters and getters
    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    # Overriding old method for printing info
    def print_info(self):
        super().print_info()
        print(f"{self.__state:<4}")


# Class for main method
class MainMethods:
    def main(self):
        # printing and getting input
        print("Welcome to Domestic/Imported Cars Application\n")
        print("Step One:")
        stock_file = input("Please enter a file name (with information about Cars in Stock) : ")
        print(f"Input file name for Cars in Stock: {stock_file}\n")

        # Creating objects, printing output
        import_cars = []
        domestic_cars = []
        with open(stock_file, "r") as stock:
            for line in stock:
                car = line.strip().split()
                if car[0] == "I":
                    import_car = ImportCar(car[1], car[2], car[3], int(car[4]), car[5], car[6], tax=int(car[7]))
                    import_cars.append(import_car)
                else:
                    domestic_car = DomesticCar(car[1], car[2], car[3], int(car[4]), car[5], car[6])
                    domestic_cars.append(domestic_car)

        print("Imported Cars")
        for car in import_cars:
            car.print_info()

        print("\nDomestic Cars")
        for car in domestic_cars:
            car.print_info()

        print(f"\nNumber of imported cars = {len(import_cars)}")
        print(f"Number of domestic cars = {len(domestic_cars)}")
        print(f"Total = {len(import_cars) + len(domestic_cars)}")

        # printing and getting input
        print("\nStep Two")
        expected_file = input("Please enter a file name (with information about Cars expected to arrive) : ")
        print(f"Input file name for Cars expected to arrive: {expected_file}\n")

        # Creating more objects, printing output
        with open(expected_file, "r") as expected:
            for line in expected:
                car = line.strip().split()
                if car[0] == "I":
                    import_car = ImportCar(car[1], car[2], car[3], int(car[4]), car[5], car[6], tax=int(car[7]))
                    import_cars.append(import_car)
                else:
                    domestic_car = DomesticCar(car[1], car[2], car[3], int(car[4]), car[5], car[6])
                    domestic_cars.append(domestic_car)

        print("Imported Cars")
        for car in import_cars:
            car.print_info()

        print("\nDomestic Cars")
        for car in domestic_cars:
            car.print_info()

        print(f"\nNumber of imported cars = {len(import_cars)}")
        print(f"Number of domestic cars = {len(domestic_cars)}")
        print(f"Total = {len(import_cars) + len(domestic_cars)}")

        print("\nStep Three\n")

        # Updating Import tax, printing output
        print("Imported Cars")
        for car in import_cars:
            if car.get_country() == "Japan":
                car.set_tax((car.get_tax() + 5))
            car.print_info()

        # Updating price, printing output
        print("\nDomestic Cars")
        for car in domestic_cars:
            car.set_price((car.get_price() * 1.15))
            car.print_info()

        print(f"\nNumber of imported cars = {len(import_cars)}")
        print(f"Number of domestic cars = {len(domestic_cars)}")
        print(f"Total = {len(import_cars) + len(domestic_cars)}")

        # Find cheaper cars
        print("\nFilter price less than: 15000.0")
        cheap = []
        for car in domestic_cars:
            if car.get_price() < 15000:
                cheap.append(car)
        for car in import_cars:
            if car.get_price() < 15000:
                cheap.append(car)

        # sort cheaper cars and print output
        sorted_cheap = sorted(cheap, key=lambda car: car.get_price())
        for car in sorted_cheap:
            car.print_info()
        print(f"\nNumber of cars = {len(cheap)}")

        # calculate price including taxes and print output
        price = 0
        for car in domestic_cars:
            price += car.get_price()*1.06
        for car in import_cars:
            price += car.get_price() * (1 + (car.get_tax() / 100))*1.06

        print(f"\nTotal price of cars in the Stock: ${price:,.2f}")


# call main method
main = MainMethods()
main.main()

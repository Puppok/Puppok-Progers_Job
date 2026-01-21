class Transport:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed  # км/ч
        self.position = 0  # км
        self.fuel = 100  # литры

    # Движение (должен быть переопределен)
    def move(self, distance):
        raise NotImplementedError("Подклассы должны реализовать move()")

    # Заправка
    def refuel(self, amount):
        self.fuel += amount
        if self.fuel > 100:
            self.fuel = 100
        print(f"{self.brand} {self.model}: заправлено {amount}л")

    # Информация
    def info(self):
        print(f"{self.brand} {self.model}")
        print(f"Скорость: {self.speed} км/ч")
        print(f"Позиция: {self.position} км")
        print(f"Топливо: {self.fuel:.1f}л\n")

# Автомобиль
class Car(Transport):
    def __init__(self, brand, model, speed, num_seats):
        super().__init__(brand, model, speed)
        self.num_seats = num_seats

    # Автомобиль едет по дороге
    def move(self, distance):
        fuel_needed = distance * 0.1  # 0.1л на км

        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.position += distance
            print(f"{self.brand} проехал {distance} км")
        else:
            max_distance = self.fuel / 0.1
            print(f"Недостаточно топлива, можно проехать только {max_distance:.1f} км")

# Велосипед
class Bicycle(Transport):
    def __init__(self, brand, model):
        super().__init__(brand, model, speed=20)
        self.fuel = float('inf')  # Не нужно топливо

    # Велосипед едет медленнее
    def move(self, distance):
        self.position += distance
        print(f"{self.brand} проехал {distance} км (без топлива!)")

    # Велосипеду не нужна заправка
    def refuel(self, amount):
        print(f"{self.brand}: велосипеду не нужно топливо!")

# Самолет
class Plane(Transport):
    def __init__(self, brand, model, speed, max_altitude):
        super().__init__(brand, model, speed)
        self.max_altitude = max_altitude
        self.altitude = 0

    # Взлет
    def takeoff(self):
        if self.fuel < 20:
            print(f"Недостаточно топлива для взлёта")
            return False

        self.altitude = self.max_altitude
        self.fuel -= 20
        print(f"{self.brand} взлетел на высоту {self.altitude}м")
        return True

    # Посадка
    def land(self):
        self.altitude = 0
        print(f"{self.brand} приземлился")

    # Самолет летит в воздухе
    def move(self, distance):
        if self.altitude == 0:
            print(f"Сначала нужно взлететь!")
            return

        fuel_needed = distance * 0.2  # Самолёт расходует больше

        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.position += distance
            print(f"{self.brand} пролетел {distance} км на высоте {self.altitude}м")
        else:
            print(f"Недостаточно топлива для полёта")


# Полиморфное использование
vehicles = [
    Car("Toyota", "Camry", 180, 5),
    Bicycle("Stels", "Navigator", ),
    Plane("Boeing", "747", 900, 10000)
]

print("--- Информация о транспорте ---")
for vehicle in vehicles:
    vehicle.info()

print("\n--- Движение ---")

# Все транспорты используют метод move(), но по разному
vehicles[0].move(50)  # Автомобиль едет
vehicles[1].move(10)  # Велосипед едет
vehicles[2].takeoff()  # Самолет сначала взлетает
vehicles[2].move(500)  # Потом летит

print("\n--- Заправка ---")
for vehicle in vehicles:
    vehicle.refuel(30)

print("\n--- Финальное состояние ---")
for vehicle in vehicles:
    vehicle.info()
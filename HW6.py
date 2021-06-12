# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

# import time


class TrafficLight:
    __color = 'Color'

    def running(self):
        while True:
            print('RED')
            time.sleep(7)
            print('YELLOW')
            time.sleep(2)
            print('GREEN')
            time.sleep(10)
            print('YELLOW')
            time.sleep(2)


lights = TrafficLight()
lights.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины
# полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, leng, wid):
        self._length = leng
        self._width = wid

    def mass(self):
        print(self._length * self._width * 25 * 5)


all_mass = Road(26, 17)
all_mass.mass()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': f'{_income}', 'bonus': 1500}


class Position (Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        full_name = f"{self.name} {self.surname}"
        print(full_name.title())

    def get_total_income(self):
        total_income = int(self._income.get('wage')) + int(self._income.get('bonus'))
        print(f'Доход с учетом премии: {total_income} руб.')


worker_info = Position('Иван', 'Иванов', 'строитель', 45000)
worker_info.get_full_name()
worker_info.get_total_income()


worker_info = Position('Карен', 'Айвазян', 'сантехник', 46770)
worker_info.get_full_name()
worker_info.get_total_income()


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} {self.color} начала движение')

    def turn(self, direction):
        print(f'Машина {self.name} {self.color} повернула {direction}')

    def stop(self):
        print(f'Машина {self.name} {self.color} остановилась')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Текущая скорость: {self.speed} км/ч')
        else:
            print(f'Внимание! Превышение скорости!')


class SportCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая скорость: {self.speed} км/ч')
        else:
            print(f'Внимание! Превышение скорости!')


my_towncar = TownCar(50, 'черного цвета', 'Toyota', False)
my_towncar.go()
my_towncar.show_speed()
my_towncar.turn('налево')
my_towncar.stop()

my_sportcar = SportCar(120, 'желтого цвета', 'Lamborgini', False)
my_sportcar.go()
my_sportcar.show_speed()
my_sportcar.turn('направо')
my_sportcar.stop()

my_policecar = PoliceCar(40, 'белого цвета', 'Patriot', True)
my_policecar.go()
my_policecar.show_speed()
my_policecar.turn('налево')
my_policecar.stop()

my_workcar = WorkCar(70, 'красного цвета', 'Kamaz', False)
my_workcar.go()
my_workcar.show_speed()
my_workcar.turn('налево')
my_workcar.stop()

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen (Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка запускается")


class Pencil (Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Начать отрисовку")


class Handle (Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка")


my_stationary = Pen('Hewlett&Pakert')
my_stationary.draw()

my_stationary = Pencil('Red')
my_stationary.draw()

my_stationary = Handle('Flomaster')
my_stationary.draw()

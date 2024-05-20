# Класс для создания дробей
class Fractions:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # метод для получения числителя
    def get_numerator(self):
        return self.numerator

    # метод для получения знаменателя
    def get_denominator(self):
        return self.denominator

    # метод для создания числителя
    def set_numerator(self, numerator):
        self.numerator = numerator

    # метод для создания знаменателя
    def set_denominator(self, denominator):
        self.denominator = denominator

    # метод вывода дроби
    def display(self):
        print(f'{self.numerator} / {self.denominator}')

    # метод сложения дробей
    def add(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fractions(new_numerator, new_denominator)

    # метод вычитания дробей
    def substract(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fractions(new_numerator, new_denominator)

    # метод умножения дробей
    def multiply(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fractions(new_numerator, new_denominator)

    # метод деления дробей
    def division(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fractions(new_numerator, new_denominator)


# класс температуры
class Temperature:
    # метод для перевода температуры из цельсия в фаренейты
    @staticmethod
    def celcius_to_farengeit(celsius):
        print(f"{celsius * 9 / 5 + 32}")

    # метод для перевода температуры из фаренгейта в цельсии
    @staticmethod
    def farengeit_to_celsius(farengeit):
        print(f'{(farengeit - 32) * 5 / 9}')


# класс длинны
class Len:
    # метод перевода длины из километров в мили
    @staticmethod
    def kilometers_to_mills(kilometers):
        print(f'{kilometers * 0.621371}')

    # метод перевода длины из миль в километры
    @staticmethod
    def mills_to_kilometers(mills):
        print(f'{mills * 1.609344}')


# класс объема
class Volume:
    # метод для перевода объема из литров в галлоны
    @staticmethod
    def liters_to_gallons(liters):
        print(f'{liters * 0.219969}')

    # метод для перевода объема из галлонов в литры
    @staticmethod
    def gallons_to_liters(gallons):
        print(f'{gallons * 3.78541}')


Fractions.substract(1, 2)

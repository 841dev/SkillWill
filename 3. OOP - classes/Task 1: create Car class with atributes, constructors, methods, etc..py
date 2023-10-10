class Car:

    __brand = 'Jeep'
    __model = 'GC'
    __production_year = 2011
    __color = 'grey'
    __horse_power = 295
    __is_sport_car = False
    def __init__(self,
                 brand,
                 model,
                 production_year,
                 color,
                 horse_power,
                 is_sport_car):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car
    @property
    def get_brand(self):
        return self.__brand
    @property
    def get_model(self):
        return self.__model
    @property
    def get_production_year(self):
        return self.__production_year

    @property
    def get_horse_power(self):
        return self.__horse_power
    @property
    def get_is_sport_car(self):
        return self.__is_sport_car

    @property
    def get_color(self):
        return self.__color


    def change_color(self, new_color):
        if new_color != self.__color:
            self.__color = new_color
            return True
        else:
            return False

    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power = self.__horse_power + hp
            return True
        else:
            return False

car = Car('Jeep', 'GC', 2011, 'grey', 295, 'False')


print("Brand:", car.get_brand)
print("Model:", car.get_model)
print("Production Year:", car.get_production_year)
print("Color:", car.get_color)
print("Horse Power:", car.get_horse_power)
print("Is Sport Car:", car.get_is_sport_car)

print('\n')

print(car.get_color)
print(car.change_color('red'))
print(car.get_color)

print('\n')

print(car.get_horse_power)
print(car.increase_horse_power(20))
print(car.get_horse_power)
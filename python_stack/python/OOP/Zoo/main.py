class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self,name, age):
        self.animals.append(Lion(name, age))
        return self

    def add_tiger(self,name):
        pass

    def print_all_info(self):
        print("-"*30,self.name,"-"*30)
        for animal in self.animals:
            animal.display_info()
        return self


class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level

    def display_info(self):
        print(f"The animal name is: {self.name}, his age is: {self.age}, the health level is: {self.health}, the happiness level is: {self.happiness}")
    
    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age, health_level = 100, happiness_level = 100):
        super().__init__( name, age, health_level, happiness_level)

    def feed(self):
        self.health += 100
        self.happiness += 100
        print(f"Thank u for feeding me, my health level is {self.health} my happiness level is {self.happiness} ")


class Monkey(Animal):
    def __init__(self, name, age, health_level , happiness_level):
        super().__init__( name, age, health_level, happiness_level)

class Bear(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 13).print_all_info()

animal = Lion("Nala")
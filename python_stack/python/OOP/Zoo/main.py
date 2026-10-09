class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self,name, age):
        self.animals.append(Lion(name, age))
        return self

    def add_monkey(self,name,age):
        self.animals.append(Monkey(name, age))
        return self

    def add_bear(self,name,age):
            self.animals.append(Bear(name, age))
            return self

    def print_all_info(self):
        print("-"*30,self.name,"-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

    def feed(self, animals):
        self.animals[animals].feed()
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

zoo2 = Animal("Sajeda",12,10,5)
zoo2.display_info()

class Lion(Animal):
    def __init__(self, name, age, health_level = 100, happiness_level = 100):
        super().__init__( name, age, health_level, happiness_level)

    def feed(self):
        self.health += 100
        self.happiness += 100
        print(f"Thank u for feeding me, my health level is {self.health} my happiness level is {self.happiness} ")


class Monkey(Animal):
    def __init__(self, name, age, health_level= 100 , happiness_level=100):
        super().__init__( name, age, health_level, happiness_level)

    def feed(self):
            self.health += 50
            self.happiness += 50
            print(f"Thank u for feeding me, my health level is {self.health} my happiness level is {self.happiness} ")

class Bear(Animal):
    def __init__(self, name, age, health_level=100, happiness_level=100):
        super().__init__(name, age, health_level, happiness_level)

    def feed(self):
            self.health += 80
            self.happiness += 80
            print(f"Thank u for feeding me, my health level is {self.health} my happiness level is {self.happiness} ")

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 10).feed(0).print_all_info()
zoo1.add_bear("Sajeda", 13).feed(1).print_all_info()
zoo1.add_monkey("Emil",30).feed(2).print_all_info()

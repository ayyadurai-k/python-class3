from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def food(self):
        print("Cat food is fish")
    
    def make_sound(self):
        print("Meow..!")

cat = Cat()
cat.make_sound()



class Animal:
    def make_sound(self):
        print("Normal Sound")

class Cat(Animal):
    def food(self):
        print("Cat food is fish")


cat = Cat()
cat.make_sound()
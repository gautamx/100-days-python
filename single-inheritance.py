class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal...")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
        
    def make_sound(self):
        super().make_sound()
        # Animal.make_sound(self)       # same as super().make_sound()
        print("Bark!")

d = Dog("Kukkur", "Doggerman")
print(d.name,d.species,d.breed)
d.make_sound()

# a = Animal("Dog", "Dog")
# a.make_sound()
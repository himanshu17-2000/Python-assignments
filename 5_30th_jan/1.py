class Animals:
    def __init__(self, name, species, is_mammal, eats):

        self.name = name
        self.species = species
        self.is_mammal = is_mammal
        self.eats = eats

    def define_me(self):
        print(f"Hi im a {self.name} im a {self.what} and i belong to {self.species} species of  animal kingdom ,{self.what}s {self.speech}" +
              (" and I'm a mammal and " if self.is_mammal else "i'm a non Mammal ") + (f" I'm {self.eats} animal "))
        
class Dog(Animals):
    def __init__(self, name, species, is_mammal, eats):
        self.speech = 'bark'
        self.what = 'dog'
        Animals.__init__(self, name, species, is_mammal, eats)


class Cow(Animals):
    def __init__(self, name, species, is_mammal, eats):
        self.speech = "don't Speak we Moo"
        self.what = 'cow'
        Animals.__init__(self, name, species, is_mammal, eats)

#============== main code ======================================
print()


d = Dog('stufy', 'German Shepard', True, 'Carnivorous')
d.define_me()


print()

c = Cow('kamla', 'Bos indicus', True, 'herbivorous')
c.define_me()


print()

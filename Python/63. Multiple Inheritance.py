# Multiple Inheritance = inherit from more than one parent class
#                        C(A, B)

class Prey:
    def flee(self):
        print("This animals is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

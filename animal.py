class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True

    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "time to eat"


"""cat = Animal()
print(cat.breathe())
print(cat.eat())"""
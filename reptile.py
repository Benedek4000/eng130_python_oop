from animal import Animal


class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "keep working hard to find food"

    def use_venom(self):
        return "if I have it I will use it"


"""smart_reptile = Reptile()
print(smart_reptile.breathe())
print(smart_reptile.hunt())"""
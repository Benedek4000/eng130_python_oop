def __multiply(v1, v2):
    return v1*v2


def __divide(v1, v2):
    return v1/v2


def __mod(v1, v2):
    return v1 % v2


def __cmm(cm):
    return cm/100


def __incm(inch):
    return inch*2.54


class Star:

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
        print(self.mass, self.radius)

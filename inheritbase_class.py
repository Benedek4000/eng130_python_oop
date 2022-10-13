import base_class as bc

print(bc.__multiply(7, 2))
print(bc.__divide(7, 2))
print(bc.__mod(7, 2))
print(bc.__cmm(72))
print(bc.__incm(72))


class Student:

    def __init__(self, name):
        self.name = name
        print(name)
        
# Inheritance

gradnparent class:

```python
class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True

    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "time to eat"
```

parent class: 

```python
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
```

current class:

```python
from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "if I can touch it, I can smell it as well"


smart_snake = Snake()
print(smart_snake.breathe())
print(smart_snake.hunt())
print(smart_snake.use_tongue_to_smell())
```
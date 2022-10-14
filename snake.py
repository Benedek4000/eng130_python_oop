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

import random
import math

num = 100*random.random()
print(num)
print(math.floor(num))
print(round(num))
print(math.ceil(num))

import datetime
import sys
import os

print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
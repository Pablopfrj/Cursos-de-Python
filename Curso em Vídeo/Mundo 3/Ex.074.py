import random
import numpy as np

cont = num = 0
while cont <= 5:
    num = np.random.randint(1, 10, (1, 5))
    cont += 1
n1 = num
print(n1)

import random

A = random.randrange(1,10)
B = random.randrange(1,10)

print("A = ", A)
print("B = ", B)

a1 = (A%2)==1
b1 = (B%2)==1
x = a1 or b1

print("A нечетно: ", a1)
print("B нечетно: ", b1)
print("Хотя бы одно из чисел A и B нечетное: ", x)

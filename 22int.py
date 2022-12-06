import random

N = random.randrange(0,86400)
#N = 150

print("Число секунд: ", N)
x = N%3600
print("Секунды с последнего часа: ", x)
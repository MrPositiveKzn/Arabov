import random

T_F = random.randrange(-200,100)
#T_F = 32
T_C = (T_F - 32)*5/9

print("Degrees Fahrenheit = ",T_F)
print("Degrees Celsius = ",round(T_C,2))
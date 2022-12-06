import random

T_C = random.randrange(-20, 40)
# T_C = 0
T_F = T_C * 9 / 5 + 32

print("Degrees Celsius = ", T_C)
print("Degrees Fahrenheit = ", round(T_F, 2))

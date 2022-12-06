import random

def TriangleInequality(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)
a,b = [random.randrange(1, 7) for i in range(0,2)]
c = random.randrange(5, 12)
while not TriangleInequality(a,b,c):
    a,b = [random.randrange(1, 7) for i in range(0,2)]
    c = random.randrange(5, 12)
    
#a,b,c = [5,3,4]
print("Треугольник")
print("Сторона a: ", a)
print("Сторона b: ", b)
print("Сторона c: ", c)
bool_expr = ((a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == b*b + a*a))
print("Треугольник является прямоугольным: ",bool_expr)
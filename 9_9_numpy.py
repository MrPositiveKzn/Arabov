#Напишите программу NumPy для удаления начальных пробелов из всех элементов данного массива.
import numpy as np

x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
lstripped_char = np.char.lstrip(x)
print("\nRemove the leading whitespaces : ", lstripped_char)
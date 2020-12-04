# 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using
# Pandas module.
import pandas as pd

x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x)

# 2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
print(x.tolist())
print(type(x.tolist()))

# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
a = pd.Series([2, 4, 6, 8, 10])
b = pd.Series([1, 3, 5, 7, 9])
print("To add two series:")
print(a + b)

print("To subtract two series:")
print(a - b)

print("To multiply two series")
print(a * b)

print("To divide two series:")
print(a / b)

# 4. Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
# Comparing the elements of the two series

a1 = pd.Series([2, 4, 6, 8, 10])
b1 = pd.Series([1, 3, 5, 7, 10])
print("To check whether the elements are equal in the two series:")
print(a1 == b1)

print("To check whether elements in series a1 is greater than elements in series b1")
print(a1 > b1)

print("To check whether elements in series a is less than elements in series b")
print(a1 < b1)

# 5. Write a Pandas program to convert a dictionary to a Pandas series.
# Sample Series:
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
s1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
s2 = pd.Series(s1)
print("New series:")
print(s2)

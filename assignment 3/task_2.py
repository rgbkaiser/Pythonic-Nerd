import math

def sq(num):
    return math.sqrt(num)

def log(num):
    return math.log(num)

def sin(num):
    return math.sin(num)

num = int(input("Enter a number: "))

print(f"Square root: {sq(num)}")
print(f"Logarithm: {log(num)}")
print(f"Sine: {sin(num)}")

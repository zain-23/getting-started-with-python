import sys

x = int(input("x: "))
y = int(input("y: "))

try:
   result = x / y
   print(result)
except ZeroDivisionError:
    print("ERROR Cannot divide by Zero")
    sys.exit(1)
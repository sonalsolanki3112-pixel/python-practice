# function,py

# difine a function 
def greet(name):
  print("Hello,", name)
  print("Welcome to python!")

# function with return value
def add_numbers(a, b):
  result = a + b
  return result

# function with default value
def describe(name, city="Bangalore"):
   print(name, "live in", city)

# === CALL FUNCTION ===
greet("sonal")
greet("kets")


total = add_numbers(10,20)
print("10 + 20 =", total)

describe("sonal")
describe("shrihan", "mumbai")

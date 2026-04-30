# error.py

# without error handling - script CRASHES!
# int("hello") this would crash!


# WITH error handling - script stays safe!
def safe_divide(a, b):
   try:
     result = a / b
     print("Result:", result)
   except ZeroDivisionError:
     print("ERROR: cannot divide by zero!")
   except Exception as e:
     print("ERROR:", e)

def get_age():
  try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
  except ValueError:
    print("ERROR: please enter a number not leters!")

# test safe divide
safe_divide(10, 2)
safe_divide(10, 0)


# teast age input
get_age()

a = input("Please enter a number: ")
try:
  print(int(a))
except ValueError:
  print("Please type an integer.")
#compare 2 numbers run again and again
def compare():

  x = int(input("What is x : "))
  y = int(input("What is y : "))
#compare two numbers
  if x < y :
    print("x is less than y")

  if x > y :
    print("x is greater than y")

  if x == y :
    print("x is equal to y")

  n = input("Run again y/n ? ")

  if n == "y":
    compare()

compare()

x = int(input("What is x : "))
y = int(input("What is y : "))

if x<y or x>y :
  print ("x is not equal to y")
else:
  print ("x is equal to y")
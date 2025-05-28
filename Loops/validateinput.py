"""while True:

  n = int(input("What's n? "))
  if n < 0:
    continue
  else:
    break

for _ in range(n):
    print("meow")"""

#function

def main():
   number = get_number ()
   meow (number)

def get_number():
   while True:
    n = int(input("What's n? "))
    if n > 0:
      break
   return n 

def meow(n): 
  for _ in range(n):
    print("meow")
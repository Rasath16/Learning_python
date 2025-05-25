def main():
  x = int(input("What is x : "))
  if is_even(x):
    print("Even")
  else:
    print("odd")

#use boolean
def is_even(num):
  #return True if num%2 == 0 else False
  return num % 2 == 0

main()

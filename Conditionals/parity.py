def main():
  x = int(input("What is x : "))
  if is_even(x):
    print("Even")
  else:
    print("odd")

#use boolean
def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

main()

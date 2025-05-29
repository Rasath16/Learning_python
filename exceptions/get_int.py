def main():
  x = get_int(
    print(f"x is {x}")
  )
  

def get_int():
  while True:

    try:
      x= int(input("What's x? "))

    except ValueError:
      print("x is not an integer")

    else:
      break #can use return x here because it will both break and return same time 
  return x

main()
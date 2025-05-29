def main():
  x = get_int()
  print(f"x is {x}")
  

def get_int():
  while True:
    try:
      x= int(input("What's x? "))
    except ValueError:
      pass
    else:
       return x #can use return x here because it will both break and return same time 
 

main()
def main():
  x = get_int("What's  x? ")
  print(f"x is {x}")
  

def get_int(prompt):
  while True:
    try:
      x= int(input(prompt))
    except ValueError:
      pass
    else:
       return x #can use return x here because it will both break and return same time 
 

main()
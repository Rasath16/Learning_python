def main(): #main program
  hello() #default parameter
  name =input("whats ur name? ")
  hello(name)



def hello(to="world"):#define a funtion with a parameter
  print("Hello", to) 


main()

def maintwo():
  x= float(input ("What's x ? "))
  print ("x squared is ", square(x))

def square(n):
  return pow(n,2)
  
maintwo()



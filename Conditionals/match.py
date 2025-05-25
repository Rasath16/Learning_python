name = input("What's your name? ").title()

if name == "Harry" or name == "Ron" or name == "Hermione" :
  print ("Gryffindor")
elif name == "Draco":
  print ("Slytherin")
else:
  print("Who?")

#using match
name = input("What's your name? ").title()

match name:
  case "Harry" | "Hermione" | "Ron":
    print ("Gryffindor")
  case "Draco":
    print ("Slytherin")
  case _:
    print ("Who ? ")
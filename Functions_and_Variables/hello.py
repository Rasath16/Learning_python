#Ask user the name
name = input("What's your name? \n")
#Greeting hello to user
print("hello", name)
print ("hello" +name)
print("hello! ", end="") #end with no new line #default is\n
print(name)
print("hello!", name , sep="1213") #seperate with something else rather than default single space

print('hello! "friend"') #quotation inside quotation
print(f"hello, {name}") #f strings (special type of strings)
#remove whitespace from str
name = name.strip()
#Capitalize
name = name.capitalize()#1st letter  capitalize
print ("hello", name)
name = name.title()  #all 1st letters capitalize
print ("hello", name)
name = name.strip().title()# all in one
print ("hello", name)

name = input("What's your name? ").strip().title() #one line code
print ("hello", name)

#split user's name into first name and last name\
name = input("What's ur name? ").strip().title()
first, last = name.split(" ")
print (f"hello, {first}")
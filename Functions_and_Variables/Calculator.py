#Get numbers and calculate 
x= input ("What's x ? ")
y= input ("What's y ? ")

z= int(x)+int(y) #converting default string type to integer
print(z)

#without another variable
x= int(input ("What's x ? "))
y= int(input ("What's y ? "))

print(x+y)

#one line code
print (int(input ("What's x ? ")) + int(input ("What's y ? ")) )

#Floats
x= float(input ("What's x ? "))
y= float(input ("What's y ? "))
print(round(x+y)) #round to nearest number

print(f"{x+y:,}") #use comma to seperate big numbers

z = round(x/y,2)            #limit decimal points to two
print(z)
print(f"{z:.2f}")
#students = ["Hermione", "Harry", "Ron","Draco"]
#houses = ["Gryfindor", "Gryfindor", "Gryfindor", "Slytherin" ]

students = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor", 
  "Ron": "Gryffindor",
  "Draco": "Slytherin", }

print(students["Hermione"])

for student in students:
  print(student, students[student], sep= " : ")
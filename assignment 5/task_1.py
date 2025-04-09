dictionary = {'Ram':95,'Shyaam':90,'Mohan':85,'Sohan':99,'Rahul':75}
name = input("Enter the student's name: ")

if dictionary.get(name) is None:
    print("Student not found.")
else:
    print(f"{name}'s marks: {dictionary.get(name)}")

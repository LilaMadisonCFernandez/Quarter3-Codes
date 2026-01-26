student = {}

student["Name"] = input("Enter your name: ")
student["Age"] = int(input("Enter your age: "))
student["Favorite Subject"] = input("Enter your favorite subject: ")

print("\nSTUDENT RECORD")
for key, value in student.items():
    print(f"{key}: {value}")
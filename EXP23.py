
# Family Tree Program

parent = {
    "Ravi": "Kumar",
    "Priya": "Kumar",
    "Anil": "Ravi",
    "Mani": "Ravi"
}

name = input("Enter a person's name: ")

if name in parent:
    print("Parent of", name, "is", parent[name])
else:
    print("Parent not found")

print("\nFamily Tree:")
for child, p in parent.items():
    print(p, "->", child)

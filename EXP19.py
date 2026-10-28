
# Student-Teacher Subject Code

student = {"Anil": "S101"}
teacher = {"Ravi": "T101"}
subject_code = {"S101": "AI101"}
teaches = {"Ravi": "AI101"}

name = input("Enter student name: ")

if name in student:
    code = student[name]
    subject = subject_code[code]

    for t, sub in teaches.items():
        if sub == subject:
            print("Student:", name)
            print("Teacher:", t)
            print("Subject Code:", subject)
else:
    print("Student not found")

stud_marks={"Alice":85,"John":90,"Ram":98,"Laxman":99,"Hashvik":100}
name=input("Enter the student's name: ")
if name in stud_marks.keys():
    print(name+"'s marks:",stud_marks[name])
else:
    print("Student not found.")
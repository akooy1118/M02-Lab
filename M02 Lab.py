#Abigail Kooy
#M02 Lab
#This app allows the user to enter in students' names and gpas and then determines whether or not the student has received any honors.


records= []

while True: 
    last_name = input("Enter the student's last name or type 'ZZZ' to quit: ")
    if (last_name == 'ZZZ' or 'zzz'):
        break

    first_name = input("Enter the student's first name: ")
    student_gpa = float(input("Enter the student's GPA: "))

    records.append((first_name, last_name, student_gpa))
   
for student in records:
    first_name, last_name, student_gpa == student

    if (student_gpa >= 3.5):
        print(f"{first_name} {last_name} is on the Dean's List.")
    elif (student_gpa >= 3.25):
        print(f"{first_name} {last_name} is on the Honor Roll.")
    else: 
        print(f"{first_name} {last_name} unfortunately is not on any honors.")

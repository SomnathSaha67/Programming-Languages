n=int(input("Enter number of subjects: "))
for i in range(n):
    subject=input(f"Enter name of subject {i+1}: ")
    marks=float(input(f"Enter marks obtained in {subject}: "))
    total_marks=float(input(f"Enter total marks for {subject}: "))
    percentage=(marks/total_marks)*100
    if percentage>=90:
        grade='A'
    elif percentage>=80:
        grade='B'
    elif percentage>=70:           
        grade='C'
    elif percentage>=60:
        grade='D'
    elif percentage>=50:
        grade='E'
    else:
        grade='F'
    print(f"Grade for {subject}: {grade}")            
    final_percentage+=percentage
final_percentage/=n
print(f"Overall Percentage: {final_percentage}%")   
if final_percentage>=90:
    final_grade='A'
elif final_percentage>=80:
    final_grade='B'
elif final_percentage>=70:           
    final_grade='C'
elif final_percentage>=60:
    final_grade='D'
elif final_percentage>=50:
    final_grade='E'
else:
    final_grade='F'
print(f"Final Grade: {final_grade}")
studentName = input("Student's Name: " )
studentScore = int(input("Student Score: "))

if studentScore >= 85:
    print(f"{studentName} scored {studentScore} has been granted Merit Scholarship")
elif studentScore >= 50:
    print(f"{studentName} scored {studentScore} has been granted Standard Scholarship")
else:
    print(f"{studentName} scored {studentScore} has been granted Extra Mentorship Scholarship")
    
    

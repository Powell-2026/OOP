from turtledemo.round_dance import stop

name=input("Enter your name:")
grade1=int(input("Enter your first grade:"))
grade2=int(input("Enter your second grade:"))
grade3=int(input("Enter your third grade:"))

if grade1 or grade2 or grade3 > 100 or grade1 or grade2 or grade3 < 0:
    print("Invalid Grade, please enter a grade between 0 and 100")
    exit()

total_grade=grade1+grade2+grade3
Percentile= (total_grade/300)*100

if Percentile <= 100 and Percentile >= 90:
    print("Grade: A")
elif Percentile < 90 and Percentile >= 80:
    print("Grade: B")
elif Percentile < 80 and Percentile >= 70:
    print("Grade: C")
elif Percentile < 70 and Percentile >= 60:
    print("Grade: D")
elif Percentile < 60:
    print("Grade: F")
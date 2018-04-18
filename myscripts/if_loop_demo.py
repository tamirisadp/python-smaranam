##Write a if-elif-else blocks to determine grade obtained by a student based on the total average obtained. Use the below criteria to determine the grade.
##•if total average >= 90, display "Distinct"
##•if in range [60 -90), display "Above average"
##•if in range [40 -60), display "Average"
##•else display "Fail"
##Also determine the grade of a student with average score 68.3

average_score = float(input("Please ensure your average score :"))
grade=""
if average_score >=90:
    grade="Distinct"
elif 60 <= average_score < 90 :
    grade="Above average"
elif 40 <= average_score < 60:
    grade="Average"
else:
    grade="Fail"

print("Your grade is :",grade)
    

    

    


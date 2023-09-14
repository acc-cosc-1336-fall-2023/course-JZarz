import decisions

result = decisions.overtime(45)

if result == False:
    print('30 is not overtime')

if result:
    print('is overtime')
else:
    print('not overtime')

grade = int(input("Enter a numerical grade: "))

letter_grade = decisions.get_letter_grade(grade)

print(f"Grade is:", letter_grade)

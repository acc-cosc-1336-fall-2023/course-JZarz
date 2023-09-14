import decisions

option = int(input("Input Option: "))
total = int(input("Input Total: "))

result = decisions.get_options_ratio(option,total)

rating = decisions.get_faculty_rating(result)

print(rating)

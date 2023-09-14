import decisions

option = int(input("Input Option: "))
total = int(input("Input Total: "))

returned_ratio = decisions.get_options_ratio(option, total)

score = decisions.get_faculty_rating(returned_ratio)

print(f"Your Rating:", score)

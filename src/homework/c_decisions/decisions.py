def get_options_ratio(option, total):
    
    ratio = option / total
    
    return ratio

    #get_faculty_rating(ratio)


def get_faculty_rating(ratio):
    rating = ""

    if(ratio >= .9 and ratio <= 1):
        rating = "Excellent"
    elif(ratio >= .8 and ratio <90):
        rating = "Very Good"
    elif(ratio >= .7 and ratio <80):
        rating = "Good"
    elif(ratio >= .6 and ratio <70):
        rating = "Needs Improvement"
    elif(ratio >= 0 and ratio <60):
        rating = "Unacceptable"
    else:
        print("Invalid")

    return rating    

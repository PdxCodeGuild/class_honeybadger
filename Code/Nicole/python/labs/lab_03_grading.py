# lab_03_grading.py

# versions 1 and 2

def grade():
    grade_list = [(90, 100, "A"), (80, 89, "B"), (70, 79, "C"), (60, 69, "D"), (0, 59, "F")]
    grade_letter = ""
    
    user_grade = input("What is your numeric score? ")
    user_grade = int(user_grade)
    
    for i in range(len(grade_list)):        
        if user_grade >= grade_list[i][0] and user_grade <= grade_list[i][1]:
            # grade_letter.append(grade_list[i][2])
            grade_letter = grade_list[i][2]
            if user_grade % 10 >= 7:
                grade_letter += "+"
            elif user_grade % 10 <= 3:
                grade_letter += "-"
    
    return print(f"Your letter grade is: {grade_letter}")

grade()

# get a grade input
# take that grade compare it to numeric ranges
# print out the corresponding letter grade


user_grade = int(input("Enter your score: "))


# if 90 <= user_grade <= 100:
# 
# if user_grade >= 90:
#     pass
# elif user_grade >= 80


if user_grade <= 100 and user_grade >= 90:
    print(f'Your score was {user_grade}, which equates to an "A" ')
if user_grade < 90 and user_grade >= 80:
    print(f'Your score was {user_grade}, which equates to an "B" ')
if user_grade < 80 and user_grade >= 70:
    print(f'Your score was {user_grade}, which equates to an "C" ')
if user_grade <  70 and user_grade >= 0:
    print(f'Your score was {user_grade}, which equates to a "failure" ')

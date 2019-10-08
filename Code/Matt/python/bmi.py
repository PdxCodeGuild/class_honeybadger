#bmi calculator
# Formula: weight (lb) / [height (in)]2 x 703
# Calculation: [weight (lb) / height (in) / height (in)] x 703

name = "Matt"
height_inch_1 = 69
weight_lbs_1 = 150

name_2 = "BO"
height_inch_2 = 70
weight_lbs_2 = 190

def bmi_formula (name , weight_lbs , height_inch):
    bmi_value = weight_lbs_1 / height_inch_1 * 2 * 703
    print("caclulating")
    print("BMI is : ")
    if bmi_value < 25:
        return  name + ' You are not overweight'
    else:
        return name + ' You are overweight fatty'
result_1 = bmi_formula(name, weight_lbs_1, height_inch_1)
result_2 = bmi_formula(name_2, weight_lbs_2, height_inch_2)
print(result_1)
print(result_2)

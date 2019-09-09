# practice_1_fund_prob5.py

# define the function

power = 0
calc_two_power = 0

while calc_two_power < 2**20:
    calc_two_power = 2**power
    print(calc_two_power)
    power += 1
else:
    print("Done")


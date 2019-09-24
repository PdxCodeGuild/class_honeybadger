# practice_5_comprehensions_prob1.py

# Write a comprehension to generate the first 10 powers of two.

def power_two(num_powers):
    return [2 ** x for x in range(num_powers)]

print(power_two(10))


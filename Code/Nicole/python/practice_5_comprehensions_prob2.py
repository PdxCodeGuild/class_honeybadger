# practice_5_comprehensions_prob2.py

# Write a comprehension to generate the first 10 even numbers.

def ten_even(num):
    return [x for x in range(num) if x % 2 == 0]

print(ten_even(20))
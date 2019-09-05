# def is_even(a):
#     if (a % 2 == 0):
#         print(a)
#         print(f"{a} is even")
#     else:
#         print(f" {a} is odd")
# is_even(3)
#
# def opposite(a, b):
#     if (a < 0 and b > 0) or (a > 0 and b < 0):
#         print(f" {a} and {b} are opposites")
#     else:
#         print(f" {a} and {b} are not opposites")
# opposite(-3, 1)
#
# def near_100(num):
#     if (90 < num < 100):
#         print(f" {num} is within 10 of 100")
#     else:
#         print(f" {num} is not within 10 of 100")
# near_100(7)
#
# def maximum_of_three (a, b, c):
#     if (a > b > c):
#         print(f' {a} is the greatest')
#     elif (b > a > c):
#         print(f' {b} is the greatest')
#     else:
#         print(f' {c} is the greatest')
# maximum_of_three (5, 10, 99)

exponent = 0
num = 2
def powers_of_two(num, power):
        print([num<<exponent for exponent in range(power)])
powers_of_two(2, 20)

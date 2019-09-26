# filename: arbitrary_precision_arithmetic.py

class BigInt:
    def __init__(self, num_str):
        num_list = []
        for i in range(len(num_str)):
            num_list.append(int(num_str[i]))
        num_list.reverse()
        self.nums = num_list

    def __str__(self):
        copy_list = self.nums.copy()
        copy_list.reverse()
        return "".join([str(copy_list[i]) for i in range(len(copy_list))])
    
    def __add__(self, num_two):
        if len(self.nums) > len(num_two.nums):
            max_digits = self.nums
        else:
            max_digits = num_two.nums
        carry = 0
        calculation = []
        for i in range(len(max_digits)):
            if i < len(self.nums):
                v1 = self.nums[i]
            else:
                v1 =0
            if i < len(num_two.nums):
                v2 = num_two.nums[i]
            else:
                v2 = 0
            result = v1 + v2 + carry
            if result < 10:
                carry = 0
                calculation.append(result)
            else:
                calculation.append(result % 10)
                carry = 1
        if carry == 1:
            calculation.append(carry)
        calculation.reverse()
        calc_str = "".join([str(calculation[i]) for i in range(len(calculation))])
        calc_str = calc_str.lstrip('0')
        return BigInt(calc_str)




x = BigInt('87')
y = BigInt('20')
z = x + y # x is self and y is nums_two
print(z)

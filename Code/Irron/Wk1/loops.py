# i = 0
# while i <10:
#     print(i)
#     i +=1
# else:
#     print('done')

# for i in range(10):
#     print(i, end=' ')

# for i in range(4,10): #lower bound is inclusive, upper bound is not
#     print(i, end= ' ')

# for i in range (4, 10, 2):


# text == 'hello world!'
# for char in text:
#     print(char)
             


nums = [5,0,8,3,4,1,6]
# running_total = 0
# length = len(nums)  
# print(length)
# for i in range(len(nums)):
#     #print(nums[i])
#     running_total = nums[i]+running_total
#     # print(running_total)
#     average = running_total/length
#     print(f"The running total is {running_total}")
#     print(f"The average is {average}")
    
#  total = 0
#  for num in nums:
#      total +=num
#      print(total/len(nums))

#v1
# total = 0
# for num in nums:
#     total +=num
#     print(total/len(nums))

#v2
nums = [] #creates an empty container for numbers
#nums.append(5)
#print (nums)

while True:
    num = input("Please enter a number")
    if num =='done':
        break
    #else:
    nums.append(int(num))
    #print(nums)
total = 0
for num in nums:
    total +=num
    print(total/len(nums))

    







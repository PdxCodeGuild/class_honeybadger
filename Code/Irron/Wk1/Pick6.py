import random

# #Winning Numbers
# def pick6():  #creating function called pick6 with no parameters
#     random_numbers_winning = []   #creating an empty container 
#     for i in range(6):  #creating an iteration that runs 6x
#         random_numbers_winning.append(random.randint(1,99)) #appending the random_numbers container by adding 6 random numbers
#     return random_numbers_winning #returning the random numbers
# print(pick6()) #calling function and printing it

# #Ticket Numbers
# def ticket():  #creating function called pick6 with no parameters
#     random_numbers_ticket = []   #creating an empty container 
#     for i in range(6):  #creating an iteration that runs 6x
#         random_numbers_ticket.append(random.randint(1,99)) #appending the random_numbers container by adding 6 random numbers
#     return random_numbers_ticket #returning the random numbers
# print(ticket()) #calling function and printing 

######################################################################################
#Randomly generate 6 numbers between 1 and 99 and place these numbers in a container.
#Return and print value
def generate_ticket():
    winning_numbers = [] #create container
    for i in range(6):
        winning_numbers.append(random.randint(1,99)) #updating container with random number
        i +=1
    return winning_numbers
#print(random_numbers_winning(100)) #calling and printing returned value of module

# def random_numbers_ticket():
#     ticket_numbers = []
#     for i in range(6):
#         ticket_numbers.append(random.randint(1,99))
#         i +=1
#     return ticket_numbers
# #print(random_numbers_ticket(100))

#Matching Test Codes
# count =0
# a = [5,4,3,2,1]
# b = [5,4,4,2,0]
# for i in range(5): #because index start at 0, range is 6 less 1
#     if a[i] != b[i]: #looks at each position in array and compares numbers 
#         continue  #if numbers do not match, continue moves to next value in array
#     count +=1
# print(count)

#Comparing values in arrays and tallying the # of times they match
###Create function and PASS THE ticket numbers and winnig numbers

winning_matches = [0, 4,7,100,50000,1000000,25000000]
count = 0
winnings = 0
winning_ticket = generate_ticket() #calling the generate_ticket module
print(f"The winning numbers are {winning_ticket}")
ticket = generate_ticket() #calling the generate ticket module
print(f"Your numbers are {ticket}") 


# winning_ticket = [1,2,3,4,6,5]
# ticket = [1,2,3,4,5,5]

def compare_winnings(winning_numbers,ticket_numbers):
    count=0
    for i in range(6):
        if winning_numbers[i] != ticket_numbers[i]:
            continue
        count +=1
    return count
print(compare_winnings(winning_ticket, ticket))
print(f"You have {count} matches")

    # for i in range(5):
    #      if winning_matches[i] == count:
    #          winnings = count[i]
    #  return winnings
#print(f"You have {count} matches")    
# print(f"You have earned ${winnings}")
 
# number_of_tickets = 100000  
# ticket_cost = 2
# Balance = winnings-(number_of_tickets *ticket_cost)

# print(f"You have purchased {number_of_tickets} tickets totaling ${ticket_cost*number_of_tickets}")
# print(f"Your total earnings = ${Balance}")
# #print(winning_matches) 




def generate_ticket():
    ticket = [] #create container
    for i in range(6):
        ticket.append(randint(1,99)) #updating container with random number
    return ticket
    







    def main():
        balance = 0
        expenses = 0

        winning_ticket = generate_ticket()

        


    
        





    










    






        






# #Counting Matches 
# # count =0
# # match =0
# # def comparison():
# #     for i in range(6):
# #         if random_numbers_winning[i] == random_numbers_ticket[i]:
# #             count +=1
# #             i +=1
# #     return match
# # print(f"You have {match} matches")      

# random_numbers_winning = [5,2,3,6,7,13]
# random_numbers_ticket = [5,1,3,6,99,8]
# count =0
# match =0
# def comparison():
#     for i in range(6):
#         if random_numbers_winning[i] == random_numbers_ticket[i]:
#             count +=1
#             i +=1
#     return match
# print(f"You have {match} matches")     


# # #Prize
# # def prize():
# #     if match == 1:
# #         return 4
# #     elif match == 2:
# #         return 7
# #     elif match == 3:
# #         return 100   
# #     elif match == 4:
# #         return 50000
# #     elif match == 5:
# #         return 1000000
# #     elif match == 6:
# #         return 25000000
# # print(match)


# #payouts = list of winning options 4, 7, 5000



# #pick six module

# #compare module takes 2 parameters and uses continue 
# #if ticke does not equal winner then continue, else count match
# #main module  define balance and expenses 


# #


        



# # random_numbers = random.randint(1,99)
# # print(random_numbers)
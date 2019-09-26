#Filemname: hangman.py

import random

def picksol():
        return list(random.choice([line.rstrip('\n') for line in open('english.txt', 'r') if len(line)>5]))
       
def play(solution):
        strikes = 0
        winFlag = False
        answer = list('-'*len(solution))
        print(answer, len(answer))
        while winFlag == False and strikes < 10:
                guess = input('guess a letter...')
                if guess in solution:
                        for char in solution:
                                if char == guess:
                                        answer[solution.index(char)] = guess
                else:
                        print('solution does NOT contain ',guess)
                        strikes += 1
                        print(strikes,' strikes out of ten!')
                if answer == solution:
                        print('you win!')
                        winFlag = True
                else:
                        print('your answer so far is ',answer)
                        continue
                

def maingame():
        solution = picksol()
        print(solution)
        play(solution)

maingame()        
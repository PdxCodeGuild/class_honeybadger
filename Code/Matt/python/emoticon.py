# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Assemble and display the emoticon
import random
eye = [':', ';', '8']
nose = ['>','<','-']
mouth = ['0','D',')']


eyes_choice = random.choice(eye)
nose_choice = random.choice(nose)
mouth_choice = random.choice(mouth)

print(f'{eyes_choice}{nose_choice}{mouth_choice}')
df

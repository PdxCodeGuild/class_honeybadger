# Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:
#
# ARI Formula
#
# The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
with open('junglebook.txt', 'r') as f: #open the file
    contents = f.readlines()




# sentences = 0
# words = 0
# characters = 0
# for line in contents:
#     words_list = line.split()
#     # lines = lines + 1
#     sentences += line.count('.') + line.count('!') + line
#     words = words + len(words_list)
#     characters += sum(len(word) for word in words_list)
lines = 0
# sentences = 0
characters = 0
words = 0
for line in contents:
  lines += 1
  words_list = line.split()
  words = words + len(words_list)
  characters += sum(len(word) for word in words_list)
  # sentences += line.count('.') + line.count('!') + lines
print(lines)


def ari_formula(characters,words,sentences):
    score = (4.71 * (characters/words)) + (0.5 * (words/lines) - 21.43)
    return score


print(ari_formula(characters,words,lines))
print(f'line = {lines}')
print(f'words = {words}')
print(f'chars = {characters}')

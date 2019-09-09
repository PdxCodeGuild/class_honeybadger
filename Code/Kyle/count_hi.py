

def count_occurances(text, word):
    count = 0
    for i in range(len(text)-(len(word)-1)):
        print(' '*i + word)
        for j in range(len(word)):
            if text[i+j] != word[j]:
                break
        else:
            count += 1

def count_letter(letter, word):
    return count_occurances(word, letter)


print(count_letter('p', 'poop'))





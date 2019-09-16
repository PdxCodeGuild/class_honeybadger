

import string


def rot13(input_string,n):
    #1 loop over input text by character
    #2 find index of character in alphabet
    #3 use that index to find cooresponding charcter in rotated alphabet
    #4 add rotated character to output string
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' '
    rot_alphabet = alphabet[n%len(alphabet):] + alphabet[:n%len(alphabet)]
    print(alphabet)
    print(rot_alphabet)
    
    output = ''
    for i in range(len(input_string)):
        for y in range(len(alphabet)):
            if input_string[i] == alphabet[y]:
                output += rot_alphabet[y]
        
    return output
        


print(rot13('Josephine of Something', 13))
print()
print(rot13('WBFrCuvArmBsm5BzrGuvAt', -13))






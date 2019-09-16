
#1 loop over input text by character
#2 find index of character in alphabet
#3 use that index to find cooresponding charcter in rotated alphabet
#4 add rotated character to output string

import string

class RotEncoder:
    def __init__(self, n=13):
        self.n = n

    def encode(self, input_string):
        output = ""
        alphabet = string.ascii_lowercase
        rot_alphabet = string.ascii_lowercase[self.n%len(alphabet):] + string.ascii_lowercase[:self.n%len(alphabet)]
        for i in range(len(input_string)):
            for j in range(len(alphabet)):
                if input_string[i] == alphabet[j]:
                    output += rot_alphabet[j]
        return output

    def __str__(self):
        return f"RotEncoder{self.n}"


if __name__ == '__main__':
    coder = RotEncoder(4)
    print(coder.encode("llama"))
    print(coder)












# import string
# 
# class RotEncoder:
#     def __init__(self, input_string, n=13):
#         self.input_string = input_string
#         self.n = n
# 
#     def encode(self):
#         input_string = self.input_string
#         output = ""
#         alphabet = string.ascii_lowercase
#         rot_alphabet = string.ascii_lowercase[self.n%len(alphabet):] + string.ascii_lowercase[:self.n%len(alphabet)]
#         for i in range(len(input_string)):
#             for j in range(len(alphabet)):
#                 if input_string[i] == alphabet[j]:
#                     output += rot_alphabet[j]
#         return output
# 
#     def __str__(self):
#         return f"RotEncoder{self.n}"
# 
# 
# coder = RotEncoder('llama', 4)
# print(coder.encode())
# coder2 = RotEncoder('honeybadger', 9)
# print(coder2.encode())




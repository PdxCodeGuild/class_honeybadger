
string1 = input("Please enter a word... ")


def double(string):
    string_double = list()
    for i in string:
        if i in string:
            string_double.append(i * 2)
        else:
            string_double.append(i)
    return "".join(string_double)

print(double(string1))

double(string1)
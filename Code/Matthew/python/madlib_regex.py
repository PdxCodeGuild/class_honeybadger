
import re


# found on stack overflow
# import re
# array = [3, "$x" , "$y", "$hi_buddy"]
# rep_array = [3, "A", "B", "C"]
# string = "$xena is here $x and $y. foo$x matches too!"
# for pattern, replacement in zip(array[1:], rep_array[1:]):
#     pattern = r'{}\b'.format(re.escape(pattern))
#     string = re.sub(pattern, replacement, string)
# print(string)


text = 'An inspector from the Department of Health and [noun] Services paid a surprise visit to our [adjective] school cafeteria. The lunch special, prepared by our [adjective] dietician, was spaghetti and [noun]-balls with a choice of either a [noun] salad or French [plural noun]. The inspector found the meat-[plural noun] to be overcooked and discovered a live [noun] in the fries, causing him to have a [part of the body] ache. In response, he threw up all over his [plural noun]. In his report, the inspector [adverb] recommended that the school cafeteria serve only nutritious [plural noun] as well as low-calorie [plural noun], and that all of the saturated [plural noun] be eliminated. He rated the cafeteria a [letter of the alphabet]-minus.'

# text = 'Hello, [name]! How is your [noun] going?'

fill_ins = re.findall(r'\[[a-zA-Z0-9_ ]+\]', text)
user_inputs = []
for fill_in in fill_ins:
    value = input('Enter a ' + fill_in.strip('[]') + ': ')
    user_inputs.append(value)

# failed attempt
# split_text = re.split(r'\[[a-zA-Z0-9_ ]+\]', text)
# output = ''
# for i in range(len(split_text)):
#     output += split_text[i] + user_inputs[i]

print(fill_ins)
print(user_inputs)

for i in range(len(fill_ins)):
    fill_in = fill_ins[i]
    fill_in = fill_in.replace('[', r'\[').replace(']', r'\]')
    user_input = user_inputs[i]
    text = re.sub(fill_in, user_input, text, 1)

print(text)



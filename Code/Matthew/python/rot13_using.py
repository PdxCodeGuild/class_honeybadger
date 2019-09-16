

from rot13_with_classes import RotEncoder



def encode_file(encoder, input_path, output_path):
    with open(input_path, 'r') as input_file:
        text = input_file.read()
    text = encoder.encode(text)
    with open(output_path, 'w') as output_file:
        output_file.write(text)
    


rot_encoder = RotEncoder(10)
encode_file(rot_encoder, 'test.txt', 'test2.txt')

# words = ['apple', 'banana', 'pear', 'avocado']
# for word in words:
#     print(rot_encoder.encode(word))





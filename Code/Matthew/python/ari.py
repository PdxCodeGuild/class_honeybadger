


import requests



def count_sentences(text):
    text = text.lower()
    erase_strings = ['a.d.', 'mrs.', 'ms.', 'mr.', 'b.c.']
    for erase_string in erase_strings:
        text = text.replace(erase_string, '')
    count = 0
    for char in text:
        if char in '.!?':
            count += 1
    return count


def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    count = 0
    for char in text:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
    return count

def print_ari(text):
    sentences = count_sentences(text)
    words = count_words(text)
    characters = count_characters(text)
    
    ari = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
    ari = round(ari)
    if ari > 14:
        ari = 14
    ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }
    
    d = ari_scale[ari]
    print(f'This book is at a {d["grade_level"]} reading level, ages {d["ages"]}')
    

url = 'https://www.gutenberg.org/files/60236/60236-0.txt'
response = requests.get(url)
text = response.text

start_index = text.find('The contemplation of the wonders of the universe')
end_index = text.find('                 Appendix')

text = text[start_index:end_index]
print_ari(text)
















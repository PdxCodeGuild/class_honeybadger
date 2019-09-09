#filename: num_to_phr.py

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

elevensies = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['eleventy', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hey = [tens, ones]

phr = ''

num = input('input num...')

numl = list(num)

for d in range(len(numl)):
    numl[d] = int(numl[d])


for i in range(len(numl)):
    if len(numl) > 2 and i == 0:
        print(numl[i])
        phr += ones[numl[i]-1]+'-hundred'
        continue
    
    # print(hey[i])
    # print(numl[i])
    # print()

    phr += hey[i-(len(numl)-2)][numl[i]-1] #hey out of index problem solved by instructor :(
    phr += ' '
     
    if 'eleventy' in phr:
        phr = phr.strip('eleventy')
        phr += elevensies[numl[i+1]-1]
        break
        

print(phr)
    


    
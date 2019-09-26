#filename: lab15_num_to_phr.py

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

elevensies = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hey = [tens, ones]

phr = ''

num = input('input num...')

numl = list(num)

if int(num)%10 == 0 and int(num) < 100:
    print(tens[int(num[0])-1])
    exit()


for d in range(len(numl)):
    numl[d] = int(numl[d])


for i in range(len(numl)):
    if len(numl) > 2 and i == 0:
        print(numl[i])
        phr += ones[numl[i]-1]+'-hundred '
        continue
    
    # print(hey[i])
    # print(numl[i])
    # print()

    if len(numl) > 2 and i == 1 and numl[2] == 0:
        phr += tens[numl[i]-1]
        print(phr)
        exit()
        

    phr += hey[i-(len(numl)-2)][numl[i]-1] #hey out of index problem solved by instructor :(
    phr += ' '
     
    if 'ten' in phr:
        phr = phr.replace('ten','')
        phr += elevensies[numl[i+1]-1]
        break
        

print(phr)
    


    
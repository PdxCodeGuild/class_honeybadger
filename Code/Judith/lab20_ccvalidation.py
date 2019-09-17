#filename: lab20_ccvalidation.py

ccnum = list(input('enter num: '))

def main(ccnum):
    ccnuml = []

    for i in range(len(ccnum)):
        ccnuml.append(int(ccnum[i]))

    print(ccnuml)

    ld = ccnuml[-1]

    ccnuml.pop(-1)

    ccrev = ccnuml[::-1]

    print(ld,ccnuml,ccrev)

    for i in range(len(ccrev)):
        if i%2 == 0:
            ccrev[i] += ccrev[i]
        if ccrev[i] > 9:
            ccrev[i] -= 9

    print(ccrev)

    ccsum = sum(ccrev)
    ccsum = str(ccsum)
    ccsum = list(ccsum)
    ccsuml = int(ccsum[1])
    print(ccsuml)

    if ccsuml == ld:
        return True
    else:
        return False

print(main(ccnum))








    
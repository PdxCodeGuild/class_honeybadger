#filename: peaksandvalleys.py

data = [1, 2, 3, 1, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 1, 7, 6, 7, 8, 7, 9]

def findPeaks(data): #able to recognize cliff at the end as peak
    peaks = []
    
    for i in range(1, len(data)):
        try:
            if data[i-1] < data[i] > data[i+1]: 
                peaks.append(i)
        except:
            if (data[i-1] < data[i] and i == len(data)-1):
                peaks.append(i)
   
    return peaks
      

def findValleys(data):
    valleys = []

    for i in range(1, len(data)-1):
        if data[i-1] > data[i] < data[i+1]:
            valleys.append(i)

        

    return valleys

def peakValley(peaks,valleys):
    peaksAndValleys = []
    
    for i in range(len(peaks)):
        peaksAndValleys.append(peaks[i])
    for i in range(len(valleys)):
        peaksAndValleys.append(valleys[i])
         
    peaksAndValleys.sort()
    return peaksAndValleys

def drawMap(data):
    listMap = []
    for i in range(max(data),0,-1):
        inlist = []
        for el in range(len(data)):
            if data[el] >= i:
                inlist.append('X')
            else:
                inlist.append(' ')
        listMap.append(inlist)
    return listMap

def gapFill(drawMap,findPeaks):
    listMap = drawMap(data)
    oCount = 0
    for lis in listMap:
        for i in range(len(lis)):
            if lis[i-1] in ['X','O'] and lis[i] == ' ' and not i == 0 and 'X' in lis[i:len(lis)]:
                lis[i] = 'O'
    for i in range(len(listMap)):
        print(' '.join(listMap[i]),max(data)-i)
    for lis in listMap:
        for el in lis:
            if el == 'O':
                oCount += 1
    print(oCount)
    return None


    
            
                

    
            

print(peakValley(findPeaks(data),findValleys(data)))

gapFill(drawMap, findValleys)




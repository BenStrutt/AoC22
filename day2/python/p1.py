file = open('../input.txt','r').read().split('\n')
mapFunc = lambda str: points[str.replace(' ','')]

points = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6,
}


sum = sum(map(mapFunc, file))

print(sum)
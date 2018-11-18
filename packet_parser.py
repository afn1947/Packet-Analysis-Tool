"""
File that parses the captured packets and returns a list formatted for the computation phase
Author: Andrew Villella
11/15/2018
packet_parser.py
"""

goodList = []


def parse(inputFile):
    #inputFile = "example.txt"
    outputFile = "test.txt"
    print('called parse function in packet_parser.py')
    L = []
    found_abstract = False
    with open(inputFile, 'r') as f:
        for line in f:
            if 'Echo' in line:
                found_abstract = True
                lineClean = ' '.join(filter(len, line.split(' ')))
                lineClean = lineClean.strip().split(' ')
                L.append(lineClean)
                found_abstract = False

    f.close()
    index = 0
    while index < len(L):
        del L[index][0]
        del L[index][3]
        del L[index][5]
        del L[index][6]
        del L[index][9]
        del L[index][9]
        del L[index][8]
        L[index][4] = (L[index][4] + " " + L[index][5])
        del L[index][5]
        L[index][5] = L[index][5][4:]
        L[index][6] = L[index][6][4:]
        # print(L[index])
        goodList.append(L[index])
        index += 1

    return goodList


if __name__ == '__main__':
    print(parse("example.txt"))

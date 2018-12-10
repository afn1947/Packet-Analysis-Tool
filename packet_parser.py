"""
File that parses the captured packets and returns a list formatted for the computation phase
Author: Andrew Villella
11/15/2018
packet_parser.py
"""
# List of data to be returned by parse function
goodList = []


def parse(inputFile):
    # inputFile = "example.txt"
    outputFile = "test.txt"
    # print('called parse function in packet_parser.py')
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
        # print L[index]
        # del L[index][9]

        del L[index][8]
        L[index][4] = (L[index][4] + " " + L[index][5])
        del L[index][5]
        L[index][5] = L[index][5][4:]
        L[index][6] = L[index][6][4:]
        L[index][7] = L[index][7][:-1]
        # print(L[index])
        goodList.append(L[index])
        index += 1

    return goodList


def parseHex(file):
    """
    Attempt to parse hex - Doesnt work at all
    :param file: file to be read from
    :return: The list of parsed hex
    """
    packetEnd = False
    with open(file, "r") as f:
        for line in f:
            if "No." in line or "Echo" in line:
                pass
            else:
                # line=line.strip().split("  ")
                print line
                line = line[6:]
                print line
                line = line[:-20]
                print line
                line = "".join(line.split())
                print line
                print line.decode('hex')
                # del line[0]
                # del line[len(line)]
                # print line

if __name__ == '__main__':
    """
    For Testing purposes 
    """
    print(parse("../Captures/example.txt"))

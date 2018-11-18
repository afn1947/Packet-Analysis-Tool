"""
Class that filters the captured packets and writes only the needed ones to a new file
Author: Avery Nutting-Hartman
11/15/2018
filter_packets.py
"""
PACKET_START = "No."
PING_TYPE = "Echo (ping)"

"""
Filters the file and keeps all echo request and echo replays 
file: the file containing the data
"""
def filter(file):
    entrys = []
    temp = []
    f = open(file, 'r')
    line = f.readline()
    for i in file:
        if i.isdigit():
            num = i
    newFile = "Node" + str(num) + "_filtered.txt"
    w = open(newFile, 'w')
    temp = ''

    while line != "":
        if PACKET_START in line:
            if len(temp) != 0 and PING_TYPE in temp:
                w.write(temp)
            temp = line
        else:
            temp = temp + line

        line = f.readline()
    if PING_TYPE in temp:
        w.write(temp)


if __name__ == '__main__':
    filter('../Captures/Node2.txt')

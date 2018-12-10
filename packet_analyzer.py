"""
Filters WireShark text file outputs to compute metrics from Echo request and Echo replies
Authors: Avery Nutting-Hartman, Andrew Villella, Ted Kaminski
12/10/2018
"""


from filter_packets import *
from packet_parser import *
from compute_metrics import *

for i in range(1, 5):
    file = filter('../Captures/Node' + str(i) + '.txt')
    data = parse('Node' + str(i) + '_filtered.txt')
    compute(data, i)

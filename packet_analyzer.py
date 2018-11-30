from filter_packets import *
from packet_parser import *
from compute_metrics import *

file=filter('../Captures/Node1.txt')
data = parse('Node1_filtered.txt')
compute(data)

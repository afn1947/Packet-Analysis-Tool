def compute(data):
    print 'called compute function in compute_metrics.py'
    print data
    timeMetrics(data)


'''
Function computes the time and distance based metrics and returns the results.
'''
def timeMetrics(data):
    #TODO compute GoodPut
    RTTlst = []
    frameSize = []
    hopCount = []
    for i in range(0, len(data), 2):
        RTTlst.append(float(data[i + 1][0]) - float(data[i][0]))
        frameSize.append(int(data[i][3]))
        hopCount.append(129-int(data[i][6]))
    RTT = sum(RTTlst) / len(RTTlst)
    throughPut = sum(frameSize) / sum(RTTlst)
    avgHops=sum(hopCount)/len(hopCount)

    print 'The RTT: ', RTT
    print 'Echo Request Throughput: ', throughPut
    print 'Distance Metric: ',avgHops



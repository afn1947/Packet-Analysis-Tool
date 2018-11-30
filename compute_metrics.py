def compute(data):
    # print 'called compute function in compute_metrics.py'
    #print data
    #timeMetrics(data)
    dataSizeMetrics(data)
    timeMetrics(data)

def dataSizeMetrics(data):
    req = []
    replies = []
    for i in range(0, len(data)):
        if(data[i][4] == "Echo request"):
            req.append(data[i])
        elif(data[i][4] == "Echo reply"):
            replies.append(data[i])
    #for i in req:
    #    seq = i[5]
    #    for j in replies:
    #        if(seq == j[5]):

    bytesSent = 0
    bytesRecieved = 0
    for i in req:
        bytesSent+=int(i[3])
    for i in replies:
        bytesRecieved+=int(i[3])
    print "Number of Echo requests sent: ",len(req)
    print "Number of Echo requests recieved: ",len(req)
    print "Number of Echo replies sent: ",len(replies)
    print "Number of Echo replies recieved: ",len(replies)
    print "Total Echo Request bytes sent:",bytesSent
    print "Total Echo Request bytes recieved:",bytesRecieved
    #TODO Echo request data sent in payload
    #TODO Echo request data recieved in payload



def timeMetrics(data):
    """
    Computes the time and distance metrics
    :param data: data to be analyzed
    :return: The results from analysis
    """
    #TODO compute GoodPut
    RTTlst = []
    frameSize = []
    hopCount = []
    HeaderLength = 42
    dataTotal = 0
    for i in range(0, len(data), 2):
        RTTlst.append(float(data[i + 1][0]) - float(data[i][0]))
        frameSize.append(int(data[i][3]))
        hopCount.append(129-int(data[i][6]))
        dataTotal += int(data[i][3])
    RTT = sum(RTTlst) / len(RTTlst)
    throughPut = sum(frameSize) / sum(RTTlst)
    avgHops=sum(hopCount)/len(hopCount)
    goodPut = dataTotal/sum(RTTlst)
    print 'The RTT: ', RTT
    print 'Echo Request Throughput: ', throughPut
    print 'Echo Reguest Goodput: ', goodPut
    print 'Distance Metric - Avg number of hops per Echo Request: ',avgHops



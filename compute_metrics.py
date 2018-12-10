"""
Computes the metrics from a node and prints the resualts to a file
authors: Ted Kaminski and Avery Nutting-Hartman
12/10/2018
"""
# List of the IP addresses for the nodes
nodes = ["192.168.100.1", "192.168.100.2", "192.168.200.1", "192.168.200.2", "192.168.101.254"]

# The length of the headers
HEADERLENGTH = 42

# The max time to live number
TTLMAX = 129


def compute(data, nodeNumber):
    """
    calls the computing functions then the output function
    :param data: data to be parsed
    :param nodeNumber: The number of the node we are parsing data from
    """
    dataArray = dataSizeMetrics(data, nodeNumber - 1)
    timeArray = timeMetrics(data, nodeNumber)
    output(dataArray, timeArray, nodeNumber)


def dataSizeMetrics(data, node):
    """
    Computes the data size metrics and returns a list of them
    :param data: Data to be used to compute metrics
    :param node: The Node number from which the data is from
    :return: List of the computed metrics
    """
    sentRequests, sentReplies = 0, 0
    bytesSent, dataSent = 0, 0

    for i in range(0, len(data)):
        if (data[i][1] == nodes[node]):
            if (data[i][4] == "Echo request"):
                sentRequests += 1
                bytesSent += int(data[i][3])
                dataSent += int(data[i][3]) - 20 - 8 - 14
            elif (data[i][4] == "Echo reply"):
                sentReplies += 1
    recvRequests, recvReplies = 0, 0
    bytesRecv, dataRecv = 0, 0
    for i in range(0, len(data)):
        if (data[i][2] == nodes[node]):
            if (data[i][4] == "Echo request"):
                recvRequests += 1
                bytesRecv += int(data[i][3])
                dataRecv += int(data[i][3]) - 20 - 8 - 14
            elif (data[i][4] == "Echo reply"):
                recvReplies += 1

    dataArray = [sentRequests, recvRequests, sentReplies, sentRequests, bytesSent, bytesRecv, dataSent, dataRecv]
    return dataArray


def timeMetrics(data, nodeNum):
    """
    Computes the time and distance metrics
    :param data: data to be analyzed
    :return: The results from analysis
    """
    nodeNum = nodeNum - 1
    rttList = []
    requestFrameSizeList = []
    requestPayloadSizeList = []
    hopCountList = []
    replyDelayList = []
    for i in range(0, len(data)):
        if data[i][4] == 'Echo reply' and data[i][2] == nodes[nodeNum]:
            # finding the list of hop counts
            hopCountList.append(float(TTLMAX - int(data[i][6])))
        if data[i][1] == nodes[nodeNum] and data[i][4] == 'Echo request':
            # finding the lists of frame and payload size
            requestFrameSizeList.append(int(data[i][3]))
            requestPayloadSizeList.append(int(data[i][3]) - HEADERLENGTH)
            for k in range(i, len(data)):
                if data[i][1] == data[k][2] and data[i][5] == data[k][5] and data[i][2] == data[k][1]:
                    # finding the RTT times list
                    rttList.append(float(data[k][0]) - float(data[i][0]))
                    break
        if data[i][2] == nodes[nodeNum] and data[i][4] == "Echo request":
            for j in range(i, len(data)):
                if data[j][1] == nodes[nodeNum] and data[i][5] == data[j][5] and data[j][4] == "Echo reply":
                    # finding the reply delay
                    replyDelayList.append(float(data[j][0]) - float(data[i][0]))
    rttListSum = sum(rttList) * 1000
    RTT = round((sum(rttList) / len(rttList)) * 1000, 2)
    throughPut = round(sum(requestFrameSizeList) / rttListSum, 1)
    goodPut = round(sum(requestPayloadSizeList) / rttListSum, 1)
    avgHops = round(sum(hopCountList) / len(hopCountList), 2)
    z = str(sum(replyDelayList) / len(replyDelayList))
    z = float(z[:7])
    replyDelay = round(z, 3) * 10

    timeArray = [RTT, throughPut, goodPut, replyDelay, avgHops]
    return timeArray


def output(dataMetrics, timeMetrics, node):
    """
    Prints the metrics to a csv file
    :param dataMetrics: The data based metrics list
    :param timeMetrics: The time based metrics list
    :param node: The number of the node metrics just computed
    """
    if (node == 1):
        fp = open("output.csv", "w+")
    else:
        fp = open("output.csv", "a+")
    fp.write("Node " + str(node) + "\n\n")
    fp.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
    for i in range(0, 4):
        fp.write(str(dataMetrics[i]) + ",")
    fp.write("\nEcho Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
    fp.write(str(dataMetrics[4]) + "," + str(dataMetrics[5]) + "\n")
    fp.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
    fp.write(str(dataMetrics[6]) + "," + str(dataMetrics[7]) + "\n\n")
    fp.write("Average RTT (milliseconds)," + str(timeMetrics[0]) + "\n")
    fp.write("Echo Request Throughput (kB/sec)," + str(timeMetrics[1]) + "\n")
    fp.write("Echo Request Goodput (kB/sec)," + str(timeMetrics[2]) + "\n")
    fp.write("Average Reply Delay (microseconds)," + str(timeMetrics[3]) + "\n")
    fp.write("Average Echo Request Hop Count," + str(timeMetrics[4]) + "\n\n")

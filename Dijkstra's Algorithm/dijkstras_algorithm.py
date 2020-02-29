#################################################################
# Name: Nicole Robles
# Date: February 21, 2020
# Description: Dijkstra's Algorithm
#################################################################

from sys import *

# yoink the nodes from the CSV file
def getNodesFromCSV():
    # read CSV file
    fileCSV = open(argv[1], "r")
    names = fileCSV.readlines()[0:1]
    fileCSV.close()
    # store names of nodes in the CSV file
    names[0] = names[0][1:]
    names[0] = names[0][:(len(names[0]) - 2)]
    names[0] = names[0].split(",")
    allNodes = names[0]
    # take command line input for name of node we are calculating
    nodeName = raw_input("Please, provide the node's name: ")
    return nodeName, allNodes

# calculate the smallest path
def mathTime(list, visited, nodes):
    i = 0
    tester = 99999
    for j in range(1,len(list)):
        # check if list is not empty
        if int(list[j]) != 0:
            # if visited, continue with the next calculation
            if nodes[j - 1] in visited:
                continue
            # compare node to tester value
            if int(list[j]) < tester:
                tester = int(list[j])
                i = j
    # update list of visited nodes
    visited.append(nodes[i - 1])
    return tester, i

# time to have fun with the actual algorithm!!
def dijkstra(nodeLinks, visited, nodes, possibleLinks = "NULL"):
    # first run-through
    if possibleLinks == "NULL":
        # go back and calculate smallest path
        least, i = mathTime(nodeLinks, visited, nodes)
        # format list for the result of the calculation
        for k in range (len(lines)):
            if lines[k][0] == nodes[i - 1]:
                possibleLinks = lines[k]
                break
        # check to see efficiency of path
        inefficiency = 0
        for j in range(1, len(nodeLinks)):
            # check for more efficient paths
            if (nodeLinks[j] != "0" and int(nodeLinks[j]) > (int(possibleLinks[j]) + int(nodeLinks[i]))):
                nodeLinks[j] = str(int(possibleLinks[j]) + int(nodeLinks[i]))
                inefficiency = 1
        # if inefficiency is present, recalculate Dijkstra's Algorithm
        if visited != nodes:
            dijkstra(nodeLinks, visited, nodes, possibleLinks)

    # second and subsequent run-throughs
    else:
        # go back and calculate smallest path
        least, i = mathTime(nodeLinks, visited, nodes)
        # format list for the result of the calculation
        for k in range (len(lines)):
            if lines[k][0] == nodes[i - 1]:
                possibleLinks = lines[k]
                break
        # check to see efficiency of path
        inefficiency = 0
        for j in range(1, len(possibleLinks)):
            # check for more efficient paths
            if (nodeLinks[j] != "0" and int(nodeLinks[j]) > (int(possibleLinks[j]) + int(nodeLinks[i]))):
                nodeLinks[j] = str(int(possibleLinks[j]) + int(nodeLinks[i]))
                inefficiency = 1
        # if inefficiency is present, recalculate Dijkstra's Algorithm
        if (len(visited) != len(nodes)) or (inefficiency == 1):
            dijkstra(nodeLinks, visited, nodes, possibleLinks)
            return nodeLinks
        else:
            return nodeLinks

########################### MAIN ############################################
#    gets nodes from CSV, calculates Dijkstra's Algorithm, prints values    #
#############################################################################

# read file and get nodes and values
node, nodes = getNodesFromCSV()
fileCSV = open(argv[1], "r" )
lines = fileCSV.readlines()[1:]
fileCSV.close()
# list formatting
for j in range(len(lines)):
    lines[j] = lines[j][:(len(lines[j])-2)]
    lines[j] = lines[j].split(",")
for k in range (len(lines)):
    if lines[k][0] == node:
        nodeLinks = lines[k]
        break
# create list to document visited nodes
visited = [node]
dijkstra(nodeLinks, visited, nodes)

################# FORMATTING AND PRINTING ##############################

# basic formatting to be able to print onto terminal
nodeOrder = ""
nodeOrder += visited[0]
nodeOrder += visited[1]
nodeOrderList = nodeOrder
nodeOrderList += ", "
for i in range(2, len(visited)):
    nodeOrder = nodeOrder + visited[i]
    nodeOrderList += nodeOrder
    # add commas in between each node in the list
    # no comma after last node
    if i != 5:
        nodeOrderList += ", "

# printing results in required format
print "Shortest path tree for node {}:".format(node)
print nodeOrderList
print "Costs of least-cost paths for node {}:".format(node)
print "u:{}, v:{}, w:{}, x:{}, y:{}, z:{}".format(nodeLinks[1], nodeLinks[2], nodeLinks[3], nodeLinks[4], nodeLinks[5], nodeLinks[6])



#########################################################################################################################
# Sources used:
# 1 - https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
# 2 - https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
# 3 - http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
# 4 - Google for programming issues (math with lists, list traversals, Dijkstra representation in mathematical terms)
#########################################################################################################################

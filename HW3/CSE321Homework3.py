#!/usr/bin/env python
# coding: utf-8

# #  Q1  #

# #####  DFS  #####

# In[26]:


## A depth first search method using decrease and conquer paradigm

def depthFirstSearch(rootVertex, vertices, edges):
    arr = []
    fromVertices = []
    
    #fill the fromVertices for checking if 
    #there is an edge between the root node and another node
    
    for edge in edges:
        fromVertices.append(edge[0])
    
    #base case representing there is no other edges related with the root node
    #return the array contains current node
    
    if rootVertex[0] not in fromVertices:
        rootVertex[1] += 1
        arr.append(rootVertex[0])
        return arr
    
    #if there is an edge related to root node
    #find the related unvisited vertex and 
    #call the dfs method for the vertex that acts as the root node
    
    else:
        for edge in edges:
            if edge[0] == rootVertex[0]:
                for vertex in vertices:
                    if edge[1] == vertex[0] and vertex[1] == 0:
                        rootVertex[1] += 1
                        arr = depthFirstSearch(vertex, vertices, edges)
                        arr.append(edge[0])
                        return arr
                arr.append(edge[0])
                return arr 
                    


# In[27]:


## A method for marking the vartices as unvisited initially

def markVerticesAsUnvisited(V):
    unvisited = []
    vertices = []
    for u in V:
        unvisited.append(u)
        unvisited.append(0)
        vertices.append(unvisited)
        unvisited = []
    return vertices


# Complexity Analysis of DFS Algorithm:
#     
#     Worst Case :
#     
#         if we take the graph as adjacency matrix, as M[nxn] we have to visit all nodes
#         for each node so we have T(n) = O(n^2)
# 
#         if we take the graph as adjacency list, as M[nxn] we could visit the neighbours
#         for each node so we have T(n) = O(n+e) where e = (edge count)
#  
#  In this implementation, we have the graph as a list so;
#                                                      T(n) = O(n+e)
#     

# #####  BFS  #####

# In[28]:


## A breadth first search method using decrease and conquer paradigm

def breadthFirstSearch(rootVertex, vertices, edges):
    queue = []
    traversal = ""
    #push the root vertex to the queue
    queue.append(rootVertex)
    while queue:
        #if there is a vertex in the queue
        #pop the vertex from the queue as current vertex
        #find an edge that related to that vertex and
        #push the vertices that stands otherside of the edge (a.k.a neighbor)
        v = queue.pop(0)
        for edge in edges:
            if edge[0] == v[0]:
                for ve in vertices:
                    if ve[0] == edge[1] and ve[1] == 0:
                        ve[1] += 1
                        queue.append(ve)
                        traversal += str("->") + str(ve[0])
    #when finish the traversal return the traversal string for representation
    return traversal


# Complexity Analysis of BFS Algorithm: 
# 
#     Worst Case : O(|V|+|E|) where V is the number of vertices and E is the number of edges.

# #####  TEST FOR DFS AND BFS  #####

# In[29]:


## A main method for testing the DFS and BFS algorithms

def mainForDFSandBFS():
    import xlrd

    workbook = xlrd.open_workbook('Graph_data.XLS')
    worksheet = workbook.sheet_by_name('Sheet1')

    rootVertex = [int(worksheet.cell(0, 1).value), 0]

    fromVertices = []
    toVertices = []
    vertices = []
    edge = []
    edges = []
    index = 0

    # fill the list representing the from and to vertices, vertices and edges
    
    for fromVertex in worksheet.col(0,3):
        fromVertices.append(int(fromVertex.value))
    for toVertex in worksheet.col(1,3):
        toVertices.append(int(toVertex.value))

    for vertex in fromVertices:
        edge.append(vertex)
        edge.append(toVertices[index])
        edges.append(edge)
        edge = []
        index += 1

    index = 0  

    for elem in fromVertices:
        if elem not in vertices:
            vertices.append(elem)
    for elem in toVertices:
        if elem not in vertices:
            vertices.append(elem)

    vertices = markVerticesAsUnvisited(vertices)
    traversalArray = []

    # traverse the graph with DFS method
    print("DFS")
    for edge in edges:
        if edge[0] == rootVertex[0]:
            for v in vertices:
                if v[0] == edge[1] and v[1] == 0:
                    #call dfs for first vertex fallowing the root vertex
                    traversalArray = depthFirstSearch(v, vertices, edges)
                    traversalArray = traversalArray[::-1]
                    #add the root vertex at the begining of the traversal
                    traversal = str(edge[0])
                    for node in traversalArray:
                        traversal += str("->") + str(node) 
                    print(traversal)
                    traversalArray = []

    # traverse the graph with BFS method
    print("BFS")
    for v in vertices:
        v[1] = 0
    for v in vertices:
        if v[1] == 0:
            tr = breadthFirstSearch(v, vertices, edges)
            print(str(v[0]) + tr)


# In[ ]:


print("Q1")


# In[30]:


mainForDFSandBFS()


# In[31]:


print("")


# #  Q2  #

# In[32]:


# Game method for the given size of game and given player
# using decrease and conquer paradigm

import random
def onePileNIM(n, whoGoes):
    if n>2:
        # generate a random number for the count of the chips that will be taken
        # it must provides the rule of  => (n mod(m+1) != 0)
        if n == 2:
            m = 1
        else:
            m = random.randint(1,n-2)
        if whoGoes == 1:
            move(1, 0, m)
            whoGoes = 2
        else:
            move(0, 1, m)
            whoGoes = 1
        #decrease the count of chips and change the player
        return onePileNIM(n-m, whoGoes)
    else:
        if whoGoes == 1:
            move(1, 0, 1)
        else:
            move(0, 1, 1)
        #conquer with returning the winner
        return whoGoes


# In[33]:


# Method that represents the move and print who took how many chips from pile
def move(player1, player2, m):
    if player1:
        print("Player 1 takes : " + str(m) + " chips from pile")
    else:
        print("Player 2 takes : " + str(m) + " chips from pile")
        


# In[ ]:


print("Q2")


# In[34]:


# Main for calling the game and announcing the winner
import random
whoGoesFirst = random.randint(1,2)

# take the winner as result
whoWins = onePileNIM(50, whoGoesFirst)
print("")

# decide if the winner is the player
# who made the 1st move or 2nd move

if whoGoesFirst == whoWins:
    print("Player " + str(whoWins) + " won who made the 1st move")
else:
    print("Player " + str(whoWins) + " won who made the 2nd move")


# Complexity Analysis :
# 
#     move(...) function takes constant time => T(n) = O(1)
#     
#     Because of we're calling the recursive method with size of n, the method 
#     takes O(n) time to execute.
#     
#     onePileNIM(...) function takes linear time => T(n) = O(n)

# In[35]:


print("")


# #  Q3  #

# In[36]:


# A method that calculates is there an element in the array that has the same
# value with its index using divide and conquer paradigm

def isIndexEqualsValue(inputArray, low, high):
    # if low index > high index, there is no such element so return -1
    if low>high:
        return -1
    #if there is just one element, the middle can be either low nor high 
    elif low == high:
        middle = low
    else:
        middle = (low+high)//2
    # if middle equals the element at the middleth index,
    # the element that wanted has found
    if middle == inputArray[middle]:
        return middle
    # if middle smaller than the middleth index,
    # the element that wanted can be in the left part
    # either
    # if middle greater than the middleth index,
    # the element that wanted can be in the right part
    # so we search recursively as two parts
    elif middle < inputArray[middle]:
        index = isIndexEqualsValue(inputArray, low, (middle-1))
    elif middle > inputArray[middle]:
        index = isIndexEqualsValue(inputArray, (middle+1), high)
    return index


# In[ ]:


print("Q3")


# In[37]:


# Test for Q3

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
print(arr)
print("index : " + str(isIndexEqualsValue(arr, 0, len(arr)-1)))


# Complexity Analysis :
#     
#     Because of this uses a binary search like method, it takes O(logn) time to execute.
#     
#     T(n) = O(logn)

# In[38]:


print("")


# #  Q4  #

# In[39]:


# A method that finds the subset that has the maximum summation
# using divide and conquer paradigm
def findMaximumSubset(inputArray, low, high):
    
    #base case
    if low == high:
        return {'low':low, 'high':high ,'maxSum':inputArray[low] }
    else:
        middle = (low+high)//2
        
        #calculates the left, right and crossing parts seperately and recursively,
        
        leftPart = findMaximumSubset(inputArray, low, middle)
        rightPart = findMaximumSubset(inputArray, middle+1, high)
        crossingPart = findMaximumCrossingSubset(inputArray, low, middle, high)
        
        #then compare and choose the best one of them
        
        if rightPart['maxSum'] >= leftPart['maxSum'] and rightPart['maxSum'] >= crossingPart['maxSum']:
            return rightPart
        elif leftPart['maxSum'] >= rightPart['maxSum'] and leftPart['maxSum'] >= crossingPart['maxSum']:
            return leftPart
        else:
            return crossingPart


# In[40]:


# A method that finds the crossing subset that has the maximum summation

import math
def findMaximumCrossingSubset(inputArray, low, middle, high):
    rightPart = []
    leftPart = []
    temp = []
    LSummation = -math.inf
    RSummation = -math.inf
    summation = 0
    index = middle
    LMaxIndex = 0
    RMaxIndex = 0
    maximumSummation = 0
    
    #left part
    #calculation for each element from
    #the index of (middle+1) down to low
    for element in inputArray[low:(middle+1)][::-1]:
        summation += element
        temp.append(element)
        if summation > LSummation:
            #right part of the left part
            rightPart = temp
            LSummation = summation
            LMaxIndex = index
        index -= 1
    summation = 0
    index = 0
    temp = []
    
    #right part
    #calculation for each element from
    #the index of (middle+1) to high
    for element in inputArray[(middle+1):(high+1)]:
        summation += element
        temp.append(element)
        if summation > RSummation:
            #left part of the right part
            leftPart = temp
            RSummation = summation
            RMaxIndex = index
        index += 1
        
    maximumSummation = LSummation + RSummation
    
    #merge the parts for subset
    subset = rightPart[::-1][LMaxIndex:(middle+1)] + leftPart[0:(RMaxIndex+1)]
    return {'maxSum':maximumSummation, 'leftIndex':LMaxIndex ,'rightIndex':((middle+1)+RMaxIndex), 'subset':subset }


# In[ ]:


print("Q4")


# In[41]:


# Test for Q4

A=[5, -6, 6, 7, -6, 7, -4, 3]
print(A)
print(findMaximumSubset(A, 0, len(A)-1))


# Complexity Analysis :
# 
#     We have 2 recursive call that has the size n/2, and the method for max crossing sum which     has the size n
# 
#     T(n) = 2T(n/2) + O(n)
#     
#     Due to Master Theorem we have the complexity of:
#         
#         T(n) = O(nlogn)

# In[42]:


print("")


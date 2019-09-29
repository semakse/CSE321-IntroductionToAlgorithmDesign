#!/usr/bin/env python
# coding: utf-8

# ## Q1 ##

# In[1]:


print("\n------Q1-------\n")


# In[2]:


def orderTheJobs(setOfJobs):
    i = 0
    j = 0
    newList = []
    indexes = []
    C = []
    
    while i<len(setOfJobs):
        newList.append(setOfJobs[i])
        indexes.append(i+1)
        C.append(0)
        i += 1
    i = 0
    
    ##ordere due to decreasing wi/ti. That's optimal for job prioritization
    while i < len(newList)-1:
        while j < len(newList)-i-1:
            first = newList[j][1]/newList[j][0]
            second = newList[j+1][1]/newList[j+1][0]
            if first < second :
                temp = newList[j]
                newList[j] = newList[j+1]
                newList[j+1] = temp
                temp = indexes[j]
                indexes[j] = indexes[j+1]
                indexes[j+1] = temp
                
            j += 1
        i += 1
        j = 0
    return {'order' : newList, 'indexes' : indexes}


# In[3]:


from random import randint
jobsWithProcessingTime = []
n = 11
i=0
while i<n:
    t = randint(1,10)
    w = randint(1,10)
    jobsWithProcessingTime.append([t,w])
    i += 1
print("[ti, wi] = " + str(jobsWithProcessingTime))
sortedList = []
sortedList = orderTheJobs(jobsWithProcessingTime)
print("\nsorted [ti, wi] = " + str(sortedList['order']))
print("\norder of jobs to minimize weighted sum = " + str(sortedList['indexes']))


# ## Q2 ##

# In[4]:


print("\n------Q2-------\n")


# In[5]:


print("\n------a)-------\n")


# In[6]:


def printTable(tableOfOperatingCosts, M):
    months = "#\t"
    i = 0
    while i < len(tableOfOperatingCosts):
        months += "Month" + str(i+1) +"\t"
        i += 1
    print(months)
    operatingCostsNY = "NY\t"
    operatingCostsSF = "SF\t"
    i = 0
    while i < len(tableOfOperatingCosts):
        operatingCostsNY += str(tableOfOperatingCosts[i][0]) +"\t"
        operatingCostsSF += str(tableOfOperatingCosts[i][1]) +"\t"
        i += 1
    print(operatingCostsNY)
    print(operatingCostsSF)
    print("\nM = " + str(M) + "\n")
    return {'table' : tableOfOperatingCosts, 'M' : M}

def theAlgorithm(table):
    ## Ni = table[i][0]
    ## Si = table[i][1]
    Month = []
    sumOfCosts = 0
    sumOfCostsStringRep = "" 
    for i in range(0,len(table)):
        Month.append("")
    for i in range(0,len(table)):
        if table[i][0] < table[i][1]:
            Month[i] = "NY"
            sumOfCosts += table[i][0]
            sumOfCostsStringRep += str(table[i][0])
        else:
            Month[i] = "SF"
            sumOfCosts += table[i][1]
            sumOfCostsStringRep += str(table[i][1])
        if i < len(table)-1:
            sumOfCostsStringRep += " + "
        i += 1
    print(Month)
    return {'cost' : sumOfCosts, 'costAsStr' : sumOfCostsStringRep}
    
def showTheAlgorithmDoesntSolves():
    algorithm = "for i= 1 to n \n\tif Ni < Si then \n\t\tOutput “NY in Month i” else\n\t\tOutput “SF in Month i” end"
    
    print("\n" + algorithm + "\n\nThe algorithm above does not correctly solve the problem because if the table was: \n")
    instanceReturnsWrongAnswer = [[1,50], [3, 20], [2, 20], [6, 4]]
    M = 10
    printTable(instanceReturnsWrongAnswer, M)
    print("\nIt outputs:\n")
    res = theAlgorithm(instanceReturnsWrongAnswer)
    sumOfCosts = res['cost'] + 10
    sumOfCostsStr = res['costAsStr'] + " + " + str(M)
    print("\nThe M = 10, so according to the algorithm the sum of the costs will be : \n")
    print("Total Cost = " + sumOfCostsStr + " = " + str(sumOfCosts) + "\n")
    print("\nBut if we would be taken the NY as last city instead of SF,\nwe won't have to be add M value at the end\nand the correct output would be:\n")
    print("\n['NY', 'NY', 'NY', 'NY']\n")
    print("\nAnd the sum of the costs would be:\n")
    print("Total Cost = 1 + 3 + 2 + 6 = 12")


# In[7]:


showTheAlgorithmDoesntSolves()


# In[8]:


print("\n\n------b)-------\n")


# In[9]:


def costOfAnOptimalPlan(n, M, N, S):
    Month = []
    Costs = []
    turnCount = 0
    turn = ""
    turnCost = 0
    for i in range(0,n):
        Month.append("")
        Costs.append(0)
    for i in range(0,n):
        if turn == "N":
            if N[i] < (turnCost + M + S[i]):
                Month[i] = "NY"
                Costs[i] = N[i]
            else:
                Month[i] = "SF"
                Costs[i] = S[i]
                turnCount += 1
                turnCost += M
                turn = "S"
                
        elif turn == "S":
            if S[i] < (turnCost + M + N[i]):
                Month[i] = "SF"
                Costs[i] = S[i]
            else:
                Month[i] = "NY"
                Costs[i] = N[i]
                turnCount += 1
                turnCost += M
                turn = "N"
        else:
            if N[i] < S[i]:
                Month[i] = "NY"
                Costs[i] = N[i]
                turn = "N"
            else:
                Month[i] = "SF"
                Costs[i] = S[i]
                turn = "S"
        i += 1
    return {'Months' : Month, 'Costs' : Costs, 'turnCount' : turnCount}


# In[10]:


n = 4
M = 10
N = [1, 3, 20, 30]
S = [50, 20, 2, 4]
table = []
for i in range(0,n):
    table.append([N[i], S[i]])
    
print("\n")
printTable(table, M)

#N = [5, 20, 5, 20]
#S = [20, 5, 20, 5]


res = costOfAnOptimalPlan(n, M, N, S)
print("\nMonths : " + str(res['Months']) + "\n")
print("\nCosts : " + str(res['Costs'])+ "\n")
costsStr = ""
costsStr = str(res['Costs'][0])
cost = res['Costs'][0]
for i in range(1,len(res['Costs'])):
    costsStr += " + " + str(res['Costs'][i])
    cost += res['Costs'][i]
for i in range(0,res['turnCount']):
    costsStr += " + " + str(M)
    cost += M
print("\nTostal Cost : " + costsStr + " = " + str(cost) + "\n")


# In[ ]:





# In[ ]:





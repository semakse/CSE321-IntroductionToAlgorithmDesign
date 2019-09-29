#!/usr/bin/env python
# coding: utf-8

# ## Q1 ##

# In[1]:


print("\n--------Q1-------\n")


# In[2]:


def penalties(L):
    tempPenalties = []
    hotelList = []
    pen = []
    n = len(L)
    ##base case for initial state
    if n == 1:
        tempPenalties.append(0 + (200 - (L[0]-0))*(200 - (L[0]-0)))
        hotelList.append([L[0]])
        return{'p' : tempPenalties, 'h' : hotelList}
    else:
        k=n-2
        ##use recursion for selecting minimum cost
        res = penalties(L[1:n])
        pen = res['p']
        hotelList = res['h']
        tempPenalties.append(0 + (200 - (L[0]-0))*(200 - (L[0]-0)))
        listOfStopPoints = []
        listOfStopPoints.append([L[0]])
        ##calculate the minimum cost for each hotel
        while k>=0:
            tempPenalties.append(pen[k] + (200 - (L[0]-L[k]))*(200 - (L[0]-L[k])))
            listTemp = []
            if(L[k] != hotelList[k][len(hotelList[k])-1]):
                listTemp = hotelList[k] + [L[k]]
                listOfStopPoints.append(listTemp)
            k -= 1
        pen.append(min(tempPenalties))
        index = 0
        for temp in tempPenalties:
            if temp == min(tempPenalties):
                hotelList.append(listOfStopPoints[index])
                break
            index += 1
        return{'p' : pen, 'h' : hotelList}
    


# In[3]:


##TEST FOR Q1

A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]

hotels = penalties((A[::-1])[0:len(A)])['h']
penalties = penalties((A[::-1])[0:len(A)])['p']
hotelsIndexes = []
hotelsIndexesSub = []
i = 0
for H in hotels:
    for h in H:
        while i<len(A):
            if h == A[i]:
                hotelsIndexesSub.append(i+1)
                i = 0
                break
            i += 1
    hotelsIndexes.append(hotelsIndexesSub)
    hotelsIndexesSub = []

i = 1
for index in hotelsIndexes :
    print("If the last stop is " + str(i) + ". hotel : " + "penalty = " + str(penalties[i-1]) + " stops = " + str(index))
    i += 1


# ## Q2 ##

# In[4]:


print("\n--------Q2-------\n")


# In[5]:


## DICTIONARY FOR WORDS
def DICT(s):
    words = ["it", "was", "the", "best", "of", "times"]
    if s in words:
        return True
    else:
        return False

## RECONSTRUCT THE SENTENCE
def reconstructValidSentence(s, n):
    d = []
    res = []
    i = 0
    j = 0
    dummy = False
    finish = -1
    if n == 0:
        return []
    else:
        while i<n:
            d.append(-1)
            while j<i:
                if (DICT(s[j:(i+1)])):
                    d[j] = 1
                    k = j+1
                    while k<(i+1):
                        d[k] = 0
                        k += 1
                    dummy = True
                    res = reconstructValidSentence(s[(i+1):len(s)], len(s[(i+1):len(s)]))
                    return (d + res)
                j += 1
            j = 0
            i += 1
        if dummy == False:
            return d

##PRINT NEW SENTENCE
def printNewSentence(s, d):
    i = 0
    j = 0
    resultString = ""
    while i<len(d):
        if d[i] == 1:
            j = i
            while i+1 <len(d) and d[i+1] == 0:
                i += 1
            resultString = resultString + s[j:(i+1)] + " "
        i += 1
    print(resultString)


# In[6]:


sentence = "itwasthebestoftimes"
length = len(sentence)
d = reconstructValidSentence(sentence, length)
print("Array Representation : " + str(d))
print("")
if -1 in d:
    print("It cannot reconstituted as a sequence of valid words totally. The words has been found are here :")
else:
    print("It can reconstituted as a sequence of valid words. The reconstituted sentece is : ")
print("")
printNewSentence(sentence, d)


# ## Q3 ##

# In[7]:


print("\n--------Q3-------\n")


# In[8]:


def merge2Array(arr1, arr2):
    merged = []
    if len(arr1) == 1:
        if arr1[0] <= arr2[0]:
            merged = arr1 + arr2
            return merged
        else:
            i = 0
            for elem in arr2:
                if arr1[0] > elem:
                    merged.append(elem)
                    i += 1
            merged.append(arr1[0])
            merged = merged + arr2[i:len(arr2)]
        return merged
    elif len(arr2) == 1:
        if arr2[0] <= arr1[0]:
            merged = arr1 + arr2
            return merged
        else:
            i = 0
            for elem in arr1:
                if arr2[0] > elem:
                    merged.append(elem)
                    i += 1
            merged.append(arr2[0])
            merged = merged + arr1[i:len(arr1)]
        return merged
    else:
        left = merge2Array(arr1[0:(len(arr1)//2)], arr2[0:(len(arr1)//2)])
        print(left)
        right = merge2Array(arr1[(len(arr1)//2):len(arr1)], arr2[(len(arr1)//2):len(arr1)])
        print(right)
        i=0
        j=0
        for elemR in right: 
            while i<len(left):
                if elemR<left[i]:
                    merged.append(elemR)
                    j += 1
                    break
                else:
                    merged.append(left[i])
                    i += 1
        merged = merged + right[j:len(right)]
        return merged
def mergeNSortedArrays(listOfArrays):
    if len(listOfArrays) == 2:
        merged = merge2Array(listOfArrays[0], listOfArrays[1])
        return merged
    else:
        left = mergeNSortedArrays(listOfArrays[0:(len(listOfArrays)//2)])
        right = mergeNSortedArrays(listOfArrays[(len(listOfArrays)//2):len(listOfArrays)])
        merged = merge2Array(left, right)
        print(left)
        print(right)
        return merged


# In[9]:


arr2 = [1,2,15,16]
arr1 = [3,5,6,7]
arr3 = [4,8,9,10]
arr4 = [11,12,13,14]
listNArrays = [arr2, arr1, arr3, arr4]
print("STEPS : ")
print("")
print("\nMerged kxn sizede array : " + str(mergeNSortedArrays(listNArrays)))


# ## Q4 ##

# In[10]:


print("\n--------Q4-------\n")


# In[11]:


from random import randint
def alicesParty(listOfNPeople, listOfPairsWhoKnowEachOther):
    numberOfInvitees = len(listOfNPeople)
    
    ##not knowing people array
    D = []
    i=0
    while i<numberOfInvitees:
        dunno = numberOfInvitees-listOfPairsWhoKnowEachOther[i]-1
        D.append(dunno)
        i += 1
        
    print("\n# of people that i'th person doesn't know = " + str(D))
    
    i = 0
    newS = []
    deletedS = []
    while i<numberOfInvitees:
        if D[i]<5 or K[i]<5:
            deletedS.append(S[i])
        else:
            newS.append(S[i])
        i += 1
    return(newS)


# In[12]:


numberOfInvitees = 20

##invitees
S = []
i = 1
while i<=numberOfInvitees:
    S.append(i)
    i += 1
print("set of potential invitees = " + str(S))

##knowing people array
K = []
i = 0
while i<numberOfInvitees:
    know = randint(3, numberOfInvitees-1)
    K.append(know)
    i += 1
print("\n# of people that i'th person knows = " + str(K))

invitees = alicesParty(S, K)

print("\n best choice of party invitees = " + str(invitees))


# ## Q5 ##

# In[13]:


print("\n--------Q5-------\n")


# In[14]:


def canBeSatisfied(cons):
    i = 0
    j = 0
    subset = []
    while i<len(cons):
        while j<len(cons[i]):
            if cons[i][j] == 1:
                if i not in subset:
                    subset.append(i)
                if j not in subset:
                    subset.append(j)
            j += 1
        i += 1
        j = 0
    for elem1 in subset:
        for elem2 in subset:
            if elem1 != elem2 and cons[elem1][elem2] == 0:
                return False       
    return True


# In[15]:


import math
constraints = []
n = 4
i=0
while i<n:
    constraints.append([math.inf])
    i += 1

i=0
while i<n:
    j=0
    while j<n:
        constraints[i].append(math.inf)
        j += 1
    i += 1

constraints[0][1] = 1
constraints[1][2] = 1
constraints[2][3] = 1
constraints[1][3] = 0
if canBeSatisfied(constraints) == False:
    print("Cannot be satisfied")
else:
    print("Can be satisfied")


# In[ ]:





# In[ ]:





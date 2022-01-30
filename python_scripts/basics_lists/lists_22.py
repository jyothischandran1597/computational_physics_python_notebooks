## Remove Duplicates from List

print("\n Remove Duplicates from List\n")

print("\n------------------------------1. using set()-------------------------------\n")

dupList = [1, 2, 3, 2, 4, 8, 9, 1, 7, 6, 4, 5]
print("List Items = ", dupList)

uniqSet = set(dupList)
uniqList = list(uniqSet)
   
print("\nList Items after removing dDuplicates = ", uniqList)

print("\n------------------------------2. for loop and if-------------------------------\n")

uniqList = []

for val in dupList:
    if val not in uniqList:
        uniqList.append(val)
        
print("\nList Items after removing Duplicates = ", uniqList)

print("\n-----------------------------3. list comprehension-----------------------------\n")

uniqList = []
[uniqList.append(i) for i in dupList if i not in uniqList]

print("List Items after removing Duplicates = ", uniqList)

print("\n------------------------3. enumerate list comprehension-------------------------\n")

uniqList = [val for x, val in enumerate(dupList) if val not in dupList[:x]]

print("List Items after removing Duplicates = ", uniqList)

print("\n--------------------------4. collections.OrderDict()---------------------------\n")

from collections import OrderedDict

uniqList = OrderedDict.fromkeys(dupList)

print("List Items after removing Duplicates = ", list(uniqList))

print("\n---------------------5. numpy.unique() and pandas.unique()----------------------\n")

import numpy as np
import pandas as pd

uniqList = np.unique(dupList).tolist()
print("List Items after removing Duplicates numpy.unique()= ", uniqList)

uniqList2 = pd.unique(dupList).tolist()
print("List Items after removing Duplicates pandas.unique()= ", uniqList2,'\n')

## Find List Items Greater Than Average

print("\n Find List Items Greater Than Average\n")

print("\n-------------------------------1. sum() and for loop----------------------------\n")

List = [0,1,2,3,4,5,6,7,8,9]

Total = sum(List)
Number = len(List)

avg = Total / Number

print('\nList Sum = {0} and Average = {1}'.format(Total, avg))

print('\nTotal List Items Greater than the List Average')
for i in range(len(listAvg)):
    if listAvg[i] > avg:
        print(listAvg[i], end = ' ')
        
print("\n-----------------------------------2. while loop--------------------------------\n")

total = 0

i = 0
while(i < Number):
    total = total + listAvg[i]
    i = i + 1

avg = total / Number

print('\nList Sum = {0} and Average = {1}'.format(total, avg))

print('\nList Items Greater than the List Average')
for i in range(len(listAvg)):
    if listAvg[i] > avg:
        print(listAvg[i], end = ' ')
        

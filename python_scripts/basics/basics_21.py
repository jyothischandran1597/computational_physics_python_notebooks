## Multiplication Table


print("\nMultiplication Table\n")
print("\n------------------------------with nested for loop------------------------------\n")

for i in range(8, 10+1):
    for j in range(1, 10+1):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')
    
print("\n----------------------------with nested while loop------------------------------\n")

i = 8

print("Multiplication Table ")
while(i <= 10):
    j = 1
    while(j <= 10):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
        j = j + 1
    print('==============')
    i = i + 1
    

## Profit or Lose

### 1. Using elif statement

print("\nProfit or loss\n")
print("\n------------------------------with elif----------------------------------------\n")


actual_cost = float(input("Please Enter the Actual Product Price: "))
sale_amount = float(input("Please Enter the Sales Amount: "))
 
if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = {0}".format(amount))
elif(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")
    
### 2. Using elif statements and arithmetic operations
    
print("\n------------------------with elif and operations--------------------------------\n")

actual_cost = float(input("Please Enter the Actual Product Price: "))
sale_amount = float(input("Please Enter the Sales Amount: "))
 
if(actual_cost - sale_amount > 0):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = {0}".format(amount))
elif(sale_amount - actual_cost > 0):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")
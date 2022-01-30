## Calculate compond interest

## A = P(1+r)^n and C = A - P

# Where, 
# * A -> final amount
# * I -> Compond interest
# * P -> principal amount
# * r -> interest rate
# * t -> time in years.

print("\nCalculate compond interest\n")

import math

princ_amount = float(input("Please Enter the Principal Amount : "))
rate_of_int = float(input("Please Enter the Rate of Interest in percentage   : "))
time_period = float(input("Please Enter Time period in Years   : "))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100), time_period)) 
compound_int = ci_future - princ_amount

print("Future Compound Interest for Principal Amount {0} = {1}".format(princ_amount, ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(princ_amount, compound_int))
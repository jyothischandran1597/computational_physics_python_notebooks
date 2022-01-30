## Calculate simple interest

## I = P (r/100) t and  A = I+P

# Where, 
# * A -> final amount
# * I -> simple interest
# * P -> principal amount
# * r -> interest rate in %
# * t -> time in years.

print("\nCalculate simple interest\n")


princ_amount = float(input("Please Enter the Principal Amount : "))
rate_of_int = float(input("Please Enter the Rate of Interest   : "))
time_period = float(input("Please Enter Time period in Years   : "))

simple_interest = (princ_amount * rate_of_int * time_period) / 100

print("\nSimple Interest for Principal Amount {0} = {1}".format(princ_amount, simple_interest))
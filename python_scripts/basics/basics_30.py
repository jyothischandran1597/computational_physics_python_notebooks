## Calculate Electricity Bill

### 1. Electricity board is charging different tariffs for different units. 

print("\n Calculate Electricity Bill \n")
print("\n 1. Electricity board is charging different tariffs for different units. \n")

units = int(input("Please enter Number of Units you Consumed : "))

if(units < 50):
    amount = units * 2.60
    surcharge = 25
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = {:0.2f}".format(total))

print("\n 2. Electricity board charges uniform rates. \n")

units = int(input(" Please enter Number of Units you Consumed : "))

if(units > 500):
    amount = units * 9.65
    surcharge = 85
elif(units >= 300):
    amount = units * 7.75
    surcharge = 75
elif(units >= 200):
    amount = units * 5.26
    surcharge = 55
elif(units >= 100):
    amount = units * 3.76
    surcharge = 35
else:
    amount = units * 2.25
    surcharge = 25

total = amount + surcharge
print("\nElectricity Bill = {:0.2f}".format(total))

## Find Student Grades

print("\n Find Student Grades \n")

english = float(input("Please enter English Marks out of 100: "))
math = float(input("Please enter Math score out of 100: "))
computers = float(input("Please enter Computer Marks out of 100: "))
physics = float(input("Please enter Physics Marks out of 100: "))
chemistry = float(input("Please enter Chemistry Marks out of 100: "))

total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100

print("Total Marks = {:.2f}".format(total))
print("Average Marks = {:0.2f}".format(average))
print("Marks Percentage = {:.2f} %".format(percentage))
print("The final grade is ", end = " ")
if(percentage >= 90):
    print("A Grade")
elif(percentage >= 80):
    print("B Grade")
elif(percentage >= 70):
    print("C Grade")
elif(percentage >= 60):
    print("D Grade")
elif(percentage >= 40):
    print("E Grade")
else:
    print("Fail")
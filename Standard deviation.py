
from math import sqrt

print("--------------------------")
print("Grade statistics tool:")
print("--------------------------")

# Declaring the list of variables to use
choice = True
count = 0
studentGrade = -1
sum = 0
sumNumerator = 0
maxVal = -1
minVal = 1000000000000000
average = 0
standardDeviation = 0

# Taking user choice whether to start entering student final grades or not
while (choice == True):
    choice = input("\nDo you have another student to enter [Y/N]? ").upper()
    
    if (choice == 'Y'):
        
        # Taking in students final grades one by one
        while (choice == 'Y'):
            count += 1
            print("Enter Student - ", count, "’s final percentage grade: ", sep='')
            studentGrade = float(input())
            
            # Doing input validation, by checking if grades ARE NOT less than 0 or greater than 100
            while ((studentGrade < 0) or (studentGrade > 100)):
                print("Please enter a grade greater than or equal to 0 but less than or equal to 100")
                studentGrade = float(input())
                
            sum += studentGrade
            
            # Checking the highest grade entered (MAX as well as the lowest grade entered (MIN)
            if (maxVal < studentGrade):
                maxVal = studentGrade
            elif (minVal > studentGrade):
                minVal = studentGrade
            
            choice = True
    
    # Calculating average when user decides to stop entering student grades
    elif (choice == 'N'):
        average = sum / count 
        choice = False
    else:
        print("--------Please enter either 'Y' or 'N' only--------")
        choice = True

print("\n*******************************************\n")

choice = input("Would you like to include standard deviation in your summary statistics [Y/N]?").upper()

while (choice == 'Y'):
    print("Please re-enter the same percentage grades as you previously did for each student.\n")
    
    # Taking student grades, which was same as before to calculate the standard deviation
    for i in range(1,count+1):
        print("Student", i, ":")
        studentGrade = float(input())
        
        # Doing input validation, by checking if grades ARE NOT less than 0 or greater than 100
        # Calculating standard deviation (SD)
        while ((studentGrade < 0) or (studentGrade > 100)):
            print("Please enter a grade greater than or equal to 0 but less than or equal to 100")
            studentGrade = float(input())
        
        sumNumerator += (studentGrade - average) ** 2
        
    standardDeviation = sqrt(sumNumerator/count)
    standardDeviation = float(format(standardDeviation, '.1f'))
    choice = 'N'
    print("\n------------------------------------------------------------")
    print("The standard deviation (SD) of all the grades entered:", standardDeviation)
    print("\n------------------------------------------------------------")

print("\n*******************************************\n")

# formating user inputs to 1 decimal place precision
maxVal = float(format(maxVal, '.1f'))
minVal = float(format(minVal, '.1f'))
average = float(format(average, '.1f')) 

# Displaying MIN, MAX and average of the grades entered
print("The highest grade (MAX) among all students: ", maxVal,"%", sep="")
print("The lowest grade (MIN) among all the students ", minVal,"%", sep="")
print("The average grade of all the students entered: ", average,"%", sep="")










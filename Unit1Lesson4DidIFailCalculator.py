#In this program, you will develop a calculator that determines if you failed an assignment.
#The program should ask the user for how many points they earned on the assignment.
    #This should be stored as a float in a variable called "pointsEarned".
#It should then ask the user for how many points the assignment was worth.
    #This should be stored as a float in a variable called "pointsPossible".

#The program should then calculate the percentage the user earned on the assignment.
    #This should be stored as a float in a variable called "percentage".
    #The percentage is calculated by dividing the pointsEarned by the pointsPossible.
    #Then, multiply by 100 to get a percentage.



#BEGIN CODING BELOW:

#Constants for the letter grades
#We will set the constants to the minimum percentage needed to earn that grade.
A = 90
B = 80
C = #COMPLETE THIS LINE
D = #COMPLETE THIS LINE

#Ask the user for the points earned and points possible
pointsEarned = float(input("How many points did you earn on the assignment? "))
pointsPossible = #COMPLETE THIS LINE

#Calculate the percentage
percentage = #COMPLETE THIS LINE

#Print the percentage
print("You earned a " + str(percentage) + "% on the assignment.")

#Determine the letter grade
if percentage >= A:
    print("You got an A!")
elif percentage >= B:
    #COMPLETE THIS LINE
elif #COMPLETE THIS LINE
    #COMPLETE THIS LINE   
elif #COMPLETE THIS LINE
    #COMPLETE THIS LINE
else:
    print("You got an F!")


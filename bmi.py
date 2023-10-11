import sys
yourWeightInPounds=input("Please enter your weight in pounds :")
yourHeightInInches=input("Please enter your height in inches :")
#BMI= (weight * 703) / (height * height)-- first convert these strings into integers so they can be calculated using the formula. Then convert back to a (concatenated) strint when printed to console/commmand line
# store the formula calculation for BMI in its own variable 
yourBMI=(float(yourWeightInPounds) * 703) / (float(yourHeightInInches) * float(yourHeightInInches))
#print results by concatenating and converting back into a string 
print("Your body mass index is " + str(yourBMI) + "%")

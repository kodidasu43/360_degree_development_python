#BMI calculator

weight=input("Please enter your Weight in K.G\n")
height=input("Please enter your Height in meters\n")

#BMI calculation logic

weight = int(weight)
height = float(height)

BMI = round(weight/(height * height),1)

print ("your BMI is : ", BMI)
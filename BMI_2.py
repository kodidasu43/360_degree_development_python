#BMI calculator

weight=input("Please enter your Weight in K.G\n")
height=input("Please enter your Height in meters\n")

#BMI calculation logic

weight = int(weight)
height = float(height)

bmi = weight/(height * height)

if bmi < 18.5:
  print("Your BMI is {}, you are underweight.".format(bmi))
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi <30:
  print("Your BMI is {}, you are slightly overweight.".format(bmi))
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
# BMI Calculator
# input weight
# input height

print("Hello user, Welcome to the BMI Calculator.")
weight = int(input("Enter your Weight: "))
height = float(input("Enter your Height in foot: "))

#foot to meter convert
meter = height * 0.3048
#BMI Calculation
bmi = weight / pow(meter,2)

#Showiing result

print("Your BMI after entering Weight:", weight, " and Height:", height, "is ", round(bmi,2))

if bmi >= 18.50 and bmi <= 20.5:
  print("Your BMI is in Normal range.")
else:
  print("You are in Danger Zone.")


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi > 35:
  msg = "you are clinically obese."
elif bmi > 30:
  msg = "you are obese."
elif bmi > 25:
  msg = "you are slightly overweight."
elif bmi > 18.5:
  msg = "you have a normal weight."
else:
  msg = "you are underweight."

print(f"Your BMI is {bmi}, {msg}")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / ((float(height) * float(height)))

if bmi < 18.5:
    print("Your BMI is " + str(round(bmi)) +", you are slightly underweight.")
elif bmi > 18.5 and bmi < 25:
    print("Your BMI is " + str(round(bmi)) +", you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print("Your BMI is " + str(round(bmi)) +", you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print("Your BMI is " + str(round(bmi)) +", you are obese.")
else:
    print("Your BMI is " + str(round(bmi)) +", you are clinically obese.")



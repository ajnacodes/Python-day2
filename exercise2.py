# 🚨 BMI calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = int(weight)
bmi = new_weight / new_height ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
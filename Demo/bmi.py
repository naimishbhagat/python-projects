# BMI = weight in kgs / height in m^2
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f'Your BMI is: {bmi}')
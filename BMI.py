# This program calculates your Body Mass Index (BMI)

height = float (input("Enter your height in cm:  "))
weight = float (input("Enter your weight in kg:  "))

squareOfHeight = height ** 2 / 10000

BMI = weight / squareOfHeight
print("Your BMI is {:.2f}".format(BMI))
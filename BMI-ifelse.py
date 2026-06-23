weight = float(input("Enter weight in kg: "))
height_feet = float(input("Enter height in feet:"))
height = height_feet * 0.3048
BMI = weight/(height*height)
if BMI < 18.5:
    print("Under Weight")
elif 18.5 <= BMI < 24.9:
    print("Normal")
elif 25 <= BMI < 29.9:
    print("OverWeight")
else:
    print("Obese")
print(BMI)
def calculate_bmi(height, weight):
 print("Height = " , height)
 print("Weight = " , weight)
 BMI = weight/(height**2)
 print ("BMI=", round(BMI,2))
 if BMI<18.5:
     print ("undeweight")
     return -1
 elif BMI > 25.0:
        print ("fat")
        return 1
 else:
        print("Normal")
        return 0
calculate_bmi(weight=57, height=1.73)

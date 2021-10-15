def BMI(w,h):

  bmi = w/(pow(h,2))
  bmi_2 = round(bmi,2)
  print(bmi_2)
  
  if bmi < 18.5:
    print("Underweight")
    
  elif bmi >= 18.5 and bmi < 25:
    print("Normal")
    
  elif bmi >= 25 and bmi < 30:
    print("Overweight")
    
  else:
    print("Obese")


weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meter: "))
BMI(weight,height)

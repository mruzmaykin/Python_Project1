#Author - Maxim Ruzmaykin
#Lab 2 - CS2990
#Completed 9/4/2018

repeat = True
while (repeat):
    repeat = False
    print("\n==========Welcome to the BMI calculation program!==========\n")
    type = input("1.USA/English system\n2.Metric system\nPlease, choose standard system: ")
    if (type == "1"): 
        weight =  float(input("Please enter your weight in pounds: "))
        height =  float(input("Please enter your height in inches(not feet): "))
        bmi = (weight/pow(height,2)*703)
        print ("\nYour weight is ", weight, " pounds.\n"
               "Your height is ", height, " inches.\n"
               "Your BMI is ", format(bmi,'.1f'), ".", sep = "")
    elif(type == "2"):
        weight =  float(input("Please enter your weight in kilograms: "))
        height =  float(input("Please enter your height in meters: "))
        bmi = (weight/pow(height,2))
        print ("\nYour weight is ", format(weight,'.1f'), " kilograms.\n"
               "Your height is ", format(height, '.2f'), " meters.\n"
               "Your BMI is ", format(bmi,'.1f'), ".", sep = "")
    if (10< bmi <=19):
        result = "underweight" 
    elif(19<bmi<25):
        result = "normal"
    elif(25<=bmi<30):
        result = "overweight"
    elif(30<=bmi<40):
        result = "obese"
    elif(40<=bmi<50):
        result = "extremely obesity"
    else:
        print("Error, you input invalid BMI.")
        repeat = input("Do you want to run the program again Y/N? ")
        if (repeat == "Y" or repeat == "y"):
            repeat = True
        elif (repeat == "N" or repeat == "n"):
            repeat = False
print ("You have ", result, "BMI.\n\n=======Thank you for using BMI calculation program!========\n")

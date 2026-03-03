"""A simple calorie calculator which takes weight ,height,genger,age and activeness as input and gives calories to meintain,loose and gain weight"""
#importing streamlit to make radio button

age=int(input("Enter your age :"))
height=float(input("Enter your height in cm :"))
weight=float(input("Enter your weight in kg :"))
gender=input("Enter your gender(MALE/FEMALE) in caps :")
print("ACTIVENESS:")
print("lightly active\n" \
"moderately active\n" \
"extremely active")
activity=input("Enter activeness according to given format :")
if gender=="MALE":
    BMR=(10*weight)+(6.25*height)-(5*age)+5
elif gender=="FEMALE":
    BMR=(10*weight)+(6.25*height)-(5*age)-161 
else:
    print("please enter valid gender")
if activity=="lightly active":
    calories_maintain=BMR*1.2
elif activity=="moderately active":
    calories_maintain=BMR*1.55
elif activity=="extremely active":
    calories_maintain=BMR*1.9

calories_loss=calories_maintain-500
calories_gain=calories_maintain+500

print("Calories to maintain weight :",calories_maintain)
print("Calories to loose weight :",calories_loss)
print("Calories to gain weight :",calories_gain)



 
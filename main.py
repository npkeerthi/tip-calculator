print("Welcome to Online tip calculator")
t=float(input("What was the total Bill: $"))
pr=int(input("What percentage bill you would like to give, 10? 12? 15? : %"))
p=int(input("Bill to be splitted among how many people? "))
pay=(t*(pr/100+1))
payf="{:.2f}".format(pay/p)
print(f"Each Person should be paying {(payf)}$")

# print("Welcome to Online tip calculator")
# t=float(input("What was the total Bill: rs"))
# pr=int(input("What percentage bill you would like to give, 10? 12? 15? : %"))
# p=int(input("Bill to be splitted among how many people? "))
# pay= "{:.2f}".format((t+(pr*t)/100)/p)
# print(f"Each Person should be paying {(pay)}rs.")
# i="{:.2}".format(33.000000006)
# print(i)

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Q1
# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n Up above the world so high,\n\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are. ")


# Q2      
# first_name=input("\nenter your first name\n")
# last_name= input("enter your last name\n")
# print("Reverse name:\n",last_name, first_name)


# Q3
# rad=float(input("\nenter radius to calculate the area of the circle\n"))
# pi=3.14
# area= pi*rad*rad
# print("Area:\n",area)


# Q4
# color_list=["Red","Green","White","Black"]
# print("First colour:\n",color_list[0])
# print("Last colour:\n",color_list[3])


# Q5
# n=(input("\nenter the value of n\n"))
# result=int(n)+ int(n*2)+ int(n*3)
# print("Result:\n",result)


# Q6
# values= input("\nEnter comma separated numbers\n")
# list_val=values.split(",")
# tuple_val=tuple(list_val)
# print("list =\n",list_val)
# print("tuple=\n",tuple_val)


# Q7
# celsius=float(input("\nEnter temperature in celsius\n"))
# fahrenheit=((celsius*9/5)+32)
# print("Temp in fahrenheit\n:",fahrenheit)


# Q8
# a=int(input("\nEnter first number\n"))
# b=int(input("Enter second number\n"))
# a,b=b,a
# a+=1
# print("Swapped and incremented values:\n",a,b)


# Q9
# n=int(input("\nEnter a number\n"))
# if(n%2==0):
#     print("Number entered is even")
# else:
#     print("Number entered is odd")    


# Q10
# year=int(input("\nEnter a year\n"))
# if(year%4==0 and year%100!=0 ) or (year%400==0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# Q11
# import math
# x1=float(input("\nEnter x1\n"))
# x2= float(input("Enter x2\n"))
# y1=float(input("Enter y1\n"))
# y2=float(input("Enter y2\n"))
# distance= math.sqrt((x2-x1)**2+(y2-y1)**2)
# print("Distance:",distance)


# Q12
# a=float(input("\nEnter first angle\n"))
# b=float(input("Enter second angle\n"))
# c=float(input("Enter third angle\n"))
# if(a+b+c==180 and a>0 and b>0 and c>0):
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")    


# Q13
# P=float(input("\nEnter principal amount\n"))
# R=float(input("Enter annual interest rate(%)\n"))
# T=float(input("Enter time period in years\n"))
# N=int(input("Enter number of times interest applied per year\n"))
# A=P*(1+R/(100*N))**(N*T)
# CI=A-P
# print("Compound interest:", CI)
# print("Total amunt:", A)


# Q14
# a=int(input("\nEnter a number\n"))
# flag=True
# if(a<2 and flag==True):
#     print("Not prime")
#     flag==True
# else:
#     for i in range (2, int(a**0.5)+1):
#         if(a%i==0):
#             flag=False
#             break
# if(flag==True):
#     print("Prime")
# else:
#     print("Not prime")


# Q15
# N= int(input("\nEnter a positive integer\n"))
# sum_squares=sum(i**2 for i in range(1,N+1))
# print("Sum of squares:", sum_squares)


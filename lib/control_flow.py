#!/usr/bin/env python3
      

def admin_login(username = "ADMIN",password = "12345"):

    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
print(admin_login("ADMIN","12345"))



def hows_the_weather(temperature):
       
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

print(hows_the_weather(33))

# FizzBuzz is a group word game often played by children to teach them about division. Players take turns counting incrementally, but with a twist:
#If a number is divisible by 3, they say "Fizz" instead of the number.
#If a number is divisible by 5, they say "Buzz" instead of the number.
#If a number is divisible by both 3 and 5, they say "FizzBuzz" instead of the number.

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz" 
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
fizzbuzz(15)   
   





def calculator(operation, num1, num2):
  
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2 
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2!= 0:  
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None
    


print(calculator("+",10,2))


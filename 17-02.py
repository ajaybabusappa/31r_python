#Arguments - Positional, keyword, default arguments
#Return statements


def find_greatest(number1, number2  = 0):
    #return 0
    if number1 > number2:
        return number1, 5, 10
    else:
        return number2
        print("Hello.....")

res = find_greatest(number1 = 10, number2 = 8)
print(res)

#Return statements - Returns values, It can return multiple values
#Return statements can be considered as end of function 


#Check if a number is multiple of 3...Return true or false

def check_3_multiples(num1):
    # if num1 % 3 == 0:
    #     return True
    # return False
    return num1 % 3 == 0

    
print(check_3_multiples(33))

#3 multiple then return 'Fizz', 5 multiple then 'buzz'
#15 multiple then return 'Fizz buzz' or return number

# def fizz_buzz_function(num1):
#     if num1 % 15 == 0:
#         return "Fizz Buzz"
#     elif num1 % 3 == 0:
#         return "Fizz"
#     elif num1 % 5 == 0:
#         return "Buzz"
#     else:
#         return num1

# print(fizz_buzz_function(30))



# #2 types of arguments
# #Arbitrary arguments and keyword arbitrary arguments

# def sum (a,b,c):
#     return a + b + c

# def sum (a,b,c, d):
#     return a + b + c + d

# print(sum(2, 5, 6, 7))
# print(sum(2, 5, 6))



#Arbitrary arguments

def sum(a, *b):
    sum = a
    for i in b:
        sum += i
    print(sum)
    return sum


sum(2, 5, 6, 7, 8, 10, 11, 12)
sum(2, 5, 6)



#Keyword arbitrary arguments
def sum(a, c, **b):
    sum = a + c
    for i, j in b.items():
        print(i, j)
        sum += j
    return sum


sum(2, 5, num1 = 6, num2 = 7,num3 =8, num4 = 10, password = 11, db_host = 12)
# sum(2, 5, 6)
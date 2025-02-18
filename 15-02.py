#Jump statements - Break, continue and pass
#Continue
#Pass


# num1 = 15
# if num1 % 2 == 0:
#     pass
# else:
#     print("Number is odd")



# def add_2_numbers(a, b):
#     pass

# class HumanBeing:
#     pass



#Functions - Specific task, Block of code
#Advantages of functions - Code reusability, File size, Maintanance
#Function definition. function call, parameters, arguments
#Types of arguments - Positional arguments, keyword arguments
#Default arguments

def example_function(num1, num2):
    print(num1 + num2)
    print(num1 * num2)
    print(num1 - num2)
    print(num1 / num2) 
    print(num1 ** num2)


a, b = 5, 8
example_function(5, 10)
example_function(num2 = 10, num1 = 5)


c , d = 10, 11
example_function(c, d)


def print_list(param_list):
    for i in param_list:
        print(i)

list1 = [1, 3, 0.5, [1, 2, 5], "Hi"]
print_list(list1)



def find_greatest(number1, number2  = 0):
    if number1 > number2:
        print(number1)
    else:
        print(number2)

find_greatest(number1 = 10)




#username, password, country, dob, gender, phone_number, status 
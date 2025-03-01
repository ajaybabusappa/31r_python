#Prime number -2 Divisors - one and itself
#1 to num - divide with all and count divisors
#check if equal to 2


num1 = int(input("Enter a number to check for prime"))

# count = 0
# for i in range(1, num1 + 1):
#     if num1 % i == 0:
#         print("Divisor", i)
#         count += 1


# print(count)
# if count == 2:
#     print("It is a prime number")
# else:
#     print("Not a prime number")



# #Approach 2

# spy = False
# if num1 in [0, 1]:
#     print("Not a prime")
# else:
#     for i in range(2, num1):
#         if num1 % i == 0:
#             spy = True
#             print("Not a prime number")
#             break

#     if spy == False:
#         print("Prime number")

#Approach 3


#20 - 1, 2, 4, 5, 10, 20 => 11
#28 - 1, 2, 4, 7, 14, 28 => 15 * 2
#9 - 1, 3, 9


#m = a * b => if b == 1 then a is m
#if b == 2 then a is m/ 2
#if b == 3 then a is m / 3



#Approach 3

spy = False
if num1 in [0, 1]:
    print("Not a prime")
else:
    #for 3? 
    for i in range(2, (num1//2) + 1):
        if num1 % i == 0:
            spy = True
            print("Not a prime number")
            break

    if spy == False:
        print("Prime number")




#64
#1 * 64 = 64
#2 * 32 = 64
#4 * 16 = 64
#8 * 8 = 64
#16 * 4 = 64
#32 * 2 = 64
#64 * 1 = 64


#n = a * b (if a == b then a value is square root n)
#Square root of n is m
#n = m * m



spy = False
if num1 in [0, 1]:
    print("Not a prime")
else:
    #for 3? 
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            spy = True
            print("Not a prime number")
            break

    if spy == False:
        print("Prime number")




#options - square, cube, exit
#picked square - take one more input
#5 => print 25
#options - square, cube, exit
#square - 4 => 16
#options -
#cube - 3 => 27
#options - exit



while True:
    print("Square - Cube - Exit")
    user_input = input("Enter option").lower()

    if user_input == 'square':
        user_sq_number = float(input("Enter num to square"))
        print(user_sq_number ** 2)

    elif user_input == 'exit':
        break
    else:
        print("Invalid input...Sariga chudu akkada emvundho")



db_username = "Sampoornesh Babu"
db_pasword = 'Hrudaya kaleyam'
total_rem_attempts = 3


while total_rem_attempts > 0:

    input_username = input("Enter username")
    input_password = input("Enter password")

    if db_username == input_username and db_pasword == input_password:
        print("Login succesful")
        break
    else:
        total_rem_attempts -= 1
        print("Login failed, you still have", total_rem_attempts, "attempts")
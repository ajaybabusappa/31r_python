
# def check_prime(input_num):
#     if input_num in [0, 1]:
#         return False
#     for i in range(2, input_num):
#         if input_num % i == 0:
#             return False
#     return True


# # num1 = 3443
# # output_sum = 0
# # while num1 > 0:
# #     digit = num1 % 10
# #     prime_res = check_prime(digit)
# #     if prime_res == False:
# #         output_sum += digit
# #     num1 = num1 // 10

# # print(output_sum)


# num1 = 200
# for i in range(1, num1 + 1):
#     if check_prime(i):
#         print(i, "Prime")
#     else:
#         print(i, "Not a prime")





#153 => 3 digits
#1 + 125 + 27 = 153

#9474 => 4 digits
#6561 + 256 + 2401 + 256 = 9474


# def check_amstrong(number):
#     sum=0
#     temp=number
#     string_num = str(number)
#     while number > 0:
#         digit = number % 10
#         sum = sum + digit ** len(string_num)
#         number = number // 10
#     if temp==sum:
#         return True
#     else:
#         return False


# min_number=int(input("enter your min number"))
# max_number = int(input("enter your max number"))
# for i in range(min_number, max_number + 1):
#     if check_amstrong(i):
#         print(i, "Is amstrong")




#15
#20 -> 19

#Assignment 2 = > Nearest prime on the greater side of a given number


#GCB, LCM
#LCM - 4 - 4, 8, 12, 16, 20, 24, 28, ..... 40
#5 - 5, 10, 15, 20, 25,..... 40

#2, 4 => 4
#7, 2 => 14
#max is a * b, min is max(a, b)

#LCM of 2 numbers will be always between greatest of the 2 numbers and product of 2 numbers


num1 = 2
num2 = 4

max_num = num1 if num1 > num2 else num2


for i in range(max_num, (num1 * num2)+1):
    if i % num1 == 0 and i % num2 == 0:
        print(i, "Is the LCM")
        break



#gcd * lcm = a * b

#GCD (a, b) - In what range
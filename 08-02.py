# #Bitwise operators

# print(~12)
# print(~-13)


# #Control statements - conditional statements, Loops, Jump statements

# #Conditional statements - If, else and elif
# #age > 18
# age = 17
# if age >= 18:
#     print("I can vote")
#     print("")
# else:
#     print("I cannot vote....Dabbulu ravu")
#     print("Eppudu peddha vadni evuthano")


# print(".......")
# print("Edho okati")




# num1 = int(input("Enter a number to check if it is positive or negative"))

# if num1 > 0:
#     print(num1, "is positive")
# else:
#     if num1 == 0:
#         print(num1) 
#     else:
#         print(num1, "Is negative")



# username = "Dj Tillu"
# password = "Radhika"


# input_username = input("Enter username")
# input_password = input("Enter password")


# if username == input_username:
#     if password == input_password:
#         print("Login succesful")
#     else:
#         print("Invalid Credentials")
# else:
#     print("Invalid credentials")



# is_admin = True

# if (username == input_username and password == input_password) or is_admin:
#     print("Login succesful")
# else:
#     print("Wrong username or password")


# num1 = int(input("Enter a number to check if it is positive or negative"))

# if num1 > 0:
#     print(num1, "is positive")
# else:
#     if num1 == 0:
#         print(num1) 
#     else:
#         if num1 == -1:
#             print(num1)
#         else:
#             print(num1, "Is negative")


# #elif
# if num1 >= 0:
#     print(num1, "is positive")
# elif num1 == 0:
#     print(num1)
# elif num1 == -1:
#     print(num1)
# else:
#     print(num1, "is negative")



# #Income tax
# input_income = int(input("Enter your salary"))

# if input_income <= 1200000:
#     print("Jai Modi")
# elif input_income > 1200000 and input_income <=1500000:
#     print(0.05 * input_income)
# elif input_income > 1500000 and input_income <= 2500000:
#     print(0.15 * input_income)
# else:
#     print(0.25 * input_income)
#     print("Jai Rahul")





#Loops - For loop and while loop

for j in range(1, 23):
    if j % 2 == 0:
        print(j, "Even")
    else:
        print(j, "Odd")

for i in range(1, 23):
    if i % 3 == 0:
        print(i)


list1 = [1, 2 , 10, [1, 2, 5], "String"]

for i in list1:
    print(i)


for i in range(0, len(list1)):
    print(i)
    print(list1[i])



str1 = "Go Live"
for i in str1:
    print(i)

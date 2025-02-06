#Strings are immutable in python
str1 = "Prabhas"
# str1[-3] = 'o'
# str1[-2] = 's'
print(str1)

str1 = "Praboss"
print(str1)


num1 = 5
num2 = 5
num3 = 5
print(id(num1))
print(id(num2))
print(id(num3))


num2 = 10


str1 = "NTR"
str2 = "NTR"

print(id(str1))
print(id(str2))



#Set - Unique, Unordered, Finite
set1 = {2, 2.0, 3, 4, 0.9,"String3", 2, 3, 4, True, 1, "String", "String2"}
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)


#Dictionary
dict1 = {1: 'Harsha', 2: 'Harsha', 3: 'Uday', 21: 'Kirsh', 21: 'Kamsa mama', 21: 'Radha' }
# set1 = {}
# print(type(dict1))
print(dict1)


dict1[21] = "Naradha"
print(dict1[21])



#None
str1 = None
print(type(str1))
print(str1)


print(1 + 1)


#Conversions
# num1 = 5
# print(float(num1))
# print(num1)

# num1 = float(num1)



num1 = 5.9
num1 = int(num1)
print(num1)
num1 = float(num1)
print(num1)


# list1 = [1, 2, 4]
# print(int(list1))



#         int float complex bool list
# int 

# float

# complex

# bool

# list   False



#print(int('21B'))


#String to list
str1 = "Koi koi....no violence"
print(list(str1))
print(type(str1))


#print(range(str1))



#Truthy values and Falsy values


print(bool(1))
print(bool(2))
print(bool(-1))
print(bool(str1))
print(str1)


print(bool(0))
print(bool(''))
print(bool([]))
print(bool(0 + 0j))


#

num1 = int(input("Enter a number"))
num2 = int(input("Enter 2nd number"))
print(num1 + num2)


print("ABC" + "CDE")




#Naming conventions
#Pascal case, camel case, snake case


#Pascal case - madhumanbeing -> MadHumanBeing
#Camel case - madHumanBeing
#Snake case - mad_human_being


database_password = 12345

#Constants - 

#const pie = 3.14



PIE = 3.14

PIE = 2.14


#Try to give meaningful names to variables


input_username = input("Username")
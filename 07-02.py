#Operators - 
#Arthematic operators - +, -, *, /, **, %, //
#Assignment operators - =, +=, -=, *=, /=, %=, //=, **=
#Relational operators - >, <, >=, <=, ==, !=
#Logical operators - and, or, not
#Bitwise operators - &, |, ^, >>, <<, ~


num1 = 50
num2 = 20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1**num2)
print(num1%num2)


#Bodmas rules 

print( 1 - 3 * 5)
print( (1 - 3**2) * -5)


#Assignment operators
num1 = 5

# print(num1 + 5)
# print(num1)

num1 = num1 + 5
#num1 += 5
print(num1)

num1 += 5 #num1 = num1 + 5

num1 = 2
num2 = 3
num1 += num2

num1 -= 5
print(num1)
num1 *=5
print(num1)

num1 %=5
print(num1)
num1 /=5
print(num1)
num1 //=5
print(num1)



#Relational operators

print( 3 > -5)
print(3 == 5)
print(3 >= 5)
print(3 <= 5)
print(3 != 5)
print(5<=10)

#Logical operators
print(True and True)
print(3 > 5 and 2 < 3)
print(False and (True and False and True and False and True and False))
print (True and (False and (True and False)))

print(2 and 3)
print(3 and 2)
print(0 and 2)
print(2 and 0)
print('' and True)
print(1 and [])
print(-1 and -2)

print('str1' and 'str2')

#Or gate

print(False or False)
print(True or False)
print(False or True)
print(2 or 3)
print(3 or 2)
print(0 or 2)
print(2 or 0)
print('' or True)
print(1 or [])
print(-1 or -2)



#Not operator.
print(not True)


#Bitwise operators - &, |, ^, ~, >>, <<

print(11 & 15)
print(bin(11))
print(bin(15))

print(12 & 23)

#1011 & 1111  - 1011 

#12 & 23
#01100
#10111

#00100 => 4

print(9 | 11)
#1001 
#1011
#1011

#xor - 1001 ^1011 => 0010




#Rightshift and Leftshift operators
#Leftshift operators


print(0b11011)

#000000000011011 -> 27
#1 * 1 + 1 * 2 + 0 * 4 + 1 * 8 + 1 * 16
#000000000110110 -> 54
#0 * 1 + 1 * 2 + 1 * 4 + 0 * 8 + 1 * 16 + 1 * 32
#2(0 + 1 + 2 + 0 + 8 + 16)
#2(27)

print( 27 << 2)
print(39 << 3)
print(41 << 1)
print(52 << 1)




#rightshift
#1011111 
#0101111

print(57 >> 1)
print(54 >> 1)
print(92 >> 2)
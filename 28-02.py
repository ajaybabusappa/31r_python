# num1 = int(input("Enter number"))

# #approach 1
# sum = 0 #O(1) memory complexity
# for i in range(1, num1 + 1):
#     sum += i

# print(sum)


# #approach 2 - O(1) space complexity
# print((num1 * (num1 + 1))/2)


# #O(1) T.c - Constant T.c
# #O(logn) - Binary search
# #O(n) T.C - Linear time complexity
# #O(nlogn)
# #O(n sqaure) - 
# #O(n cube) 



# for i in range(0, 100):  #100
#     for j in range(0, 100): #10000
#         print(i, j)



# for i in range(2, num1): #Worst case - O(n), Best case - O(1)
#     if num1 % i == 0:
#         print("Not a prime")
#         break

# #Print(prime) - some additional code





# #Memory complexity or space complexity
# #O(1) T.c - Constant T.c

# #O(n) T.C - Linear time complexity
# #O(n sqaure)


# list1 = [1, 2, 3.5, 0.6, -52, 64] #[1, 1, 1, 1, 1, 1,1]
# dup_list1 = []

# for i in list1:#Worst case s.c - O(n), O(1) best case
#     if i not in dup_list1:
#         dup_list1.append(i)
#     else:
#         print(i, "Got Repeated")

# print(dup_list1)


num2 = 12321
num1 = num2
rev_num = 0

while num1 > 0:
    rem = num1 % 10
    rev_num = rev_num * 10 + rem
    num1 = num1 // 10

print(rev_num)
print(num1)


if num2 == rev_num:
    print("Palindrome")
else:
    print("Not palindrome")





n = 25
total_budget = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total_budget += i * 100

print(total_budget)



#Perfect number - research and code
#GCD and LCM of 2 numbers
#Sum of non prime digits in a given number




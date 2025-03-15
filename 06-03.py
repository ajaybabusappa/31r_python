#return statments- 

#reverse number using functions


num1 = int(input("Enter number to reverse"))

# temp = num1 
# rev_num = 0
# while temp > 0:
#     digit = temp % 10
#     rev_num = rev_num * 10 + digit
#     temp = temp // 10

# print(rev_num)

def reverse_number(input_num):
    temp = input_num 
    rev_num = 0
    while temp > 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp = temp // 10
    return rev_num

res = reverse_number(num1)
print(res)
#print(reverse_number(num1))


def check_num_palin(input_num):
    temp = input_num 
    rev_num = 0
    while temp > 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp = temp // 10
    if rev_num == input_num:
        return True
    else:
        return False
    
if check_num_palin(12321):
    print("It is a palindrome")
else:
    print("Not a palindrome")



#
list1 = [1, 2.5, [1, 3, 5], "String", True, 35]

for i in list1:
    print(i)

for i in range(len(list1)):
    print(i)
    print(list1[i])


index = 0
while index < len(list1):
    print(index)
    print(list1[index])
    index += 1

list1 = [1, 2, 5, 0.5, -5, -71, -32]

sum = 0
for i in list1:
    sum += i

print(sum)


def check_prime(input_num):
    if input_num in [0, 1] or input_num < 0:
        return False
    for i in range(2, input_num):
        if input_num % i == 0:
            return False
    return True

primes_sum = 0
for i in list1:
    if check_prime(i) == True:
        primes_sum += i




sum_of_3_multiples = 0
for i in list1:
    if i % 3 == 0:
        sum_of_3_multiples += i

print(sum_of_3_multiples)





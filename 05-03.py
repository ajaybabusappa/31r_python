#22 - 23
#12 - 11, 13
#19 - 17

def check_prime(input_num):
    if input_num in [0, 1]:
        return False
    for i in range(2, input_num):
        if input_num % i == 0:
            return False
    return True


num1 = int(input("Enter a number"))
right_side_prime = -1
#right side first prime
temp = num1
while True:
    temp += 1
    # print(temp)
    if check_prime(temp):
        right_side_prime = temp
        break

print(right_side_prime)


temp2 = num1
left_side_prime = -1


while True:
    temp2 -= 1
    if temp2 <= 1:
        break
    if check_prime(temp2):
        left_side_prime = temp2
        break

print(left_side_prime)


left_side_distance = num1 - left_side_prime
right_side_distance = right_side_prime - num1


if left_side_prime == -1:
    print(right_side_prime)
elif left_side_distance < right_side_distance:
    print(left_side_prime)
elif right_side_distance < left_side_distance:
    print(right_side_prime)
else:
    print(left_side_prime, right_side_prime)




#17 20
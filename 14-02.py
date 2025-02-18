#Max element in a list

list1 = [1, 2, 4, 0.5, -1, -33, -72, 999]

max_value = list1[0]
min_value = list1[0]
sum = 0

for i in list1:
    sum = sum + i # sum += i
    if i > max_value: 
        max_value = i
    if i < min_value:
        min_value = i

print(max_value)
print(min_value)



list1 = [[1, 2, 4], [0.5, -1, -33], [-72, 999]]

sum = 0
for i in list1:
    for j in i:
        sum = sum + j

print(sum)


#For each list sum
for i in list1:
    sum = 0
    for j in i:
        sum = sum + j
    print(sum)



#Factorial of a number
num1 = 5
res = 1

for i in range(1, num1 + 1):
    res = res * i

print(res)






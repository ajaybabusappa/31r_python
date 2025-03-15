#max, min and sum
#reverse a list - [1, 2, True] => [True, 1, 2]
#Reverse only second half of the list => [1, 2, 3, 4, 5, 7]
#=> [1, 2, 3, 7, 5, 4]


list1 = [1, 2, 3, -4, 9.9, -32, 3.3]

sum = 0
min_value = float('inf') #list1[0]
max_value = float('-inf') #list1[0]
for i in list1:
    sum += i
    if i < min_value:
        min_value = i

print(sum)
print(min_value)


#Reverse a list

list1 = [1, 3, 5, 7, -32, 'True']
temp_list = []

for i in list1:
    temp_list.insert(0, i)

print(temp_list)
list1 = temp_list

#O(n) - both t.c and s.c 

# for i in range(len(list1)-1, -1, -1):
#     temp_list.append(list1[i])


list1 = list1[::-1]



low = 0
high = len(list1) - 1

while low < high:
    list1[low], list1[high] = list1[high], list1[low]
    low += 1
    high -= 1


print(list1)
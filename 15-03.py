

def bin_search(input_list, search_elem):
    low, high = 0, len(input_list) -1

    while low <= high:
        mid = (low + high) // 2

        if input_list[mid] == search_elem:
            return True
        elif input_list[mid] > search_elem:
            high = mid - 1
        else:
            low = mid + 1
    return False


list1 = [1, 5, 10, 11, 12, 19, 100, 111]
list2 = [4, 5, -2, 1]
output = []


for i in list2:
    output.append(bin_search(list1, i))

print(output)




#70234 - True
#2034 - False
# list1 = [] #[4, 3, 2, 0]
def dup(user_input):
    temp = user_input
    list1 = [] #[4, 3, 2, 0]
    while temp > 0:
        remen = temp % 10 #4 #3 #2 #0 #7
        if remen in list1:
            return True
        else:
            list1.append(remen)
        temp = temp // 10 #2023 #202 #20 #2 #0
    return False
        


# user_input = 20134
# result = dup(user_input)
# print(result)

output = []
list1 = [1234, 34, 56, 777]
for i in list1:
    output.append(dup(i))

print(output)



#Find the missing numbers
# 11) Find the missing numbers.
# Input: 34571      Outpur : 2, 6 missing


#[1, 7, 5, 4, 3] => max => 7
#min => 1
#for i in range(min, max + 1):

num1 = 2897


def missing_digits(input_num):

    temp = input_num
    list1 = [] #2, 8, 9,7

    while temp > 0:
        rem = temp % 10
        list1.append(rem)
        temp //= 10
    
    max_in_list = max(list1)
    min_in_list = min(list1)

    for i in range(min_in_list, max_in_list + 1):
        if i not in list1:
            print(i, end=' ')


# print(i)   
missing_digits(num1)



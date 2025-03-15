# #Function to find sum of digits in a number

# def sum_digits(input_num):
#     temp = input_num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         if digit % 2 == 0:
#             sum += digit
#         #sum += temp % 10 if (temp % 10) % 2 == 0 else 0
#         temp //= 10
#     return sum


# list1 = [202,89,122,88]
# output = []
# for i in list1:
#     temp_res = sum_digits(i)
#     output.append(temp_res)
#     #output.append(sum_digits(i))



# #Searching an element

# list1 = [1, 5, 5.5, -32, 444, 1010]
# search_elem = 5.5

# if search_elem in list1:
#     print("Element exists in list1")
# else:
#     print("Doesnot exists")


# def search_elem(input_list, search_elem):
#     if search_elem in input_list:
#         return True
#     return False


# def search_elem2(input_list, search_elem):
#     for i in input_list:
#         if i == search_elem:
#             return True
        
#     return False

# #

# def search_elem_index(input_list, search_elem):
#     for i in range(len(input_list)):
#         if search_elem == input_list[i]:
#             return i
        
#     return -1

# #Linear search algorithm - O(1) s.c, O(n) T.C

# list1 = [1,3,4,5,27]
# list2 = [2,4,3,1,7, 5, 15]


# # flag = True
# # for i in list1:
# #     if i not in list2:
# #         flag = False
# #         print("Not a subset")
# #         break

# # if flag == True:
# #     print("Subset")


# def check_subset(list1, list2):
#     for i in list1:
#         if i not in list2:
#             return False
#     return True


# print(check_subset(list1, list2))

#issubset - set approach




list1 = [1, 2]
list2 = []
def check_subset_without_in(list1, list2):
    for i in list1:
        #i = 1
        flag = False
        for j in list2:
            if i == j:
                flag = True
        
        if flag == False:
            return False
    
    return True
        

print(check_subset_without_in(list1, list2))

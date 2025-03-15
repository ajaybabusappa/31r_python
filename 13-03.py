# # list1 = [[1, 2, 3, 4], [61, 7.3, -34], [5]]

# # sum = 0
# # for i in list1:
# #     for j in i:
# #         sum += j

# # print(sum)


# #Binary search algorithm - Sorted is precondition

# list1 = [-4, -2, 6, 18, 20, 25, 49, 64]
# search_element = 18
# low = 0
# high = len(list1) - 1



# flag = False
# while low <= high:
#     mid = (low + high) // 2

#     if list1[mid] == search_element:
#         flag = True
#         print("Element found at", mid)
#         break
#     elif list1[mid] > search_element:
#         high = mid - 1
#     else: # list1[mid] < search_element
#         low = mid + 1

# if flag == False:
#     print("Element not found")



# def bin_search(input_list, search_elem):
#     low = 0
#     high = len(input_list) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if input_list[mid] == search_element:
#             return mid
#         elif input_list[mid] > search_element:
#             high = mid - 1
#         else: # list1[mid] < search_element
#             low = mid + 1
    
#     return -1



# #T.C O(1) < O(logn) < O(n)


# list1 = [1,1, 2, 3, 4, 5, 6, 7]


# def is_sorted_asc(list1): 
#     for i in range(1, len(list1)):
#         if list1[i] < list1[i-1]:
#             # print("List is not in sorted way")
#             # break 
#             return False
#     return True

# print(is_sorted_asc(list1))




#Duplicate elements in a list
list1 = [1, 1, 1,  2, 5, 2, 7, -9, -8, -8, -8]
#output= [1, 2, -8]
visited_ele = [] #1, 2, 5, 7, -9, -8
set1 = set()#1, 2, -8


for i in list1:
    if i in visited_ele:
        set1.add(i)
    else:
        visited_ele.append(i)

print(list(set1))




# {}
# {}
x = {}
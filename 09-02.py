# #Loops
# #For loop

# for clss in range(1, 11):
#     for roll in range(1, 31):
#         if clss <= 7:
#             print(clss, roll)


# count = 0
# for clss in range(1, 11):
#     if clss % 2 == 0:
#         for roll in range(1, 31):
#             count += 1
#             if roll < 15:
#                 print(clss, roll)

# print(count, "Count")

# count2 = 0
# for clss in range(1, 11):
#     for roll in range(1, 31):
#         count2 += 1
#         if clss % 2 == 0 and roll < 15:
#             print(clss, roll)

# print(count2, "Count2")

# # for i in range(1, 31):
# #     print(2, i)

# # for i in range(1, 31):
# #     print(3, i)


# #While loop

# # while condition:
# #     #loop body\



# num1 = 5
# # vishu_is_alive = True
# while num1 > 0:
#     num1 -= 1 # num1= 0
#     print(num1)
    


# # while vishu_is_alive:
# #     print("S.D.R is still fighting")
# #     vishu_is_alive = False

# # i = 1
# # while i <= 20:
# #     print(i)
# #     i = i + 1


# #for(init; conditio, updation)

# i = 0
# while i < 20:
#     i = i + 1
#     print(i)



# for clss in range(1, 11):
#     for roll in range(1, 31):
#         if clss <= 7:
#             print(clss, roll)


# clss = 1

# while clss <= 10:
#     for roll in range(1, 31):
#         if clss <= 7:
#             print(clss, roll)
#     clss += 1



clss = 1
while clss <= 10:
    roll = 1
    while roll < 31:
        if clss <= 7:
            print(clss, roll)
        roll += 1
    clss += 1

# clss = 1
# roll = 1
# while clss <= 10:
#     print(clss)
#     while roll < 31:
#         if clss <= 7:
#             print(clss, roll)
#         roll += 1
#     clss += 1
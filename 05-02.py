#Datatypes - 
#Numeric - int, float, complex, boolean
#Sequences - List, Tuple, String, Range
#Set
#Dictionary
#None


#3 ways to run a python code
#1 way - IDLE or CMD
#2 Way - Notepad
#3 way - 


print("Nidra Vasthundha?")

num1 = 2
num2 = 3

print(4/2)


#Complex numbers - m + in
#m + jn

cmp1 = 5 + 3j
cmp2 = 6 - 5j



print(cmp1 + cmp2)
print(cmp1*cmp2)
print(cmp1/cmp2)
print(cmp1-cmp2)
# print(cmp1//cmp2)
# print(cmp1%cmp2)
print(cmp1**cmp2)


#Boolean - True/False


print(2 > 3)
print (2 >= 3)
print (2 <= 3)

bool1 = True
print(type(bool1))
print(type(False))

print(int(True))
print(int(False))



#Sequences - List, Tuple, Strings, Range

#List - Collection of hetrogenous elements which are indexable and Mutable
list1 = [1, 2, 3, 4, 5, 10,-1, 'String', True, [1, 2, 6]]
print(type(list1))
print(list1)

print(list1[4])
print(list1[9])
print(list1[len(list1)-1])
print(list1[-1])


#Slicing
print("---Slicing---")
print(list1[1:4])
print(list1[4: 1: -1])
print(list1[2:8:2])
print(list1[-4])
print(list1[-4:-8: -2])



temp  = list1[9]
print(temp[2])
print(list1[9][2])



# for i in list1:
#     print(i)



list1[-3] = "Something something"
list1[-3], list1[-1] = 4, 5
a ,b = 2, 3
#list1[-3: -5] = 4, 5
print(list1[-3])
print(list1)



#Tuple - () - Immutable

tup1 = (1, 2, True, "Str1", 0.9)
tup1 = (1, 3)
print(tup1[1])
#tup1[1] = 5


#Tuple is faster than list


#range

print(list(range(0, 100)))
print(list(range(100, 0, -1)))
print(list(range(0, 100, 3)))



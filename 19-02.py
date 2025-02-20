#Scope - Lifetime
#Global
#Local


num1 = 10

def check():
    # num2 = 25
    # print(num2)
    # global num1
    # num1 = 35
    globals()['num1'] = 45
    print(num1)


check()
print(num1)



#Decorators - It is a function

def example_decorator(func1):
    def wrapper():
        print("Check cartridge")
        print("Check A4 sheets")
        func1()
        print("Thank you")
    return wrapper


@example_decorator
def printer():
    print("Printing in progress...Kasepu agu")

printer()



#
s={1,2,3,4}
s.discard(2)
print(s)

s.discard(2)
s.discard(2)
#s.remove(2)

a= [1, 2, 3,]
a.remove(2)
print(a)


a={"venky","venu","kasi"}
b=a.pop()
print(b,a)



#string replace method : it is used to replace the particular position value
#syntax: str.replace(oldvalue,newvalue,count)


txt = "i like bananas and also like banana jucie..banana"
txt1 = txt.replace("banana","apple")
print(txt1)
print(txt)



list1=[1,2,3,4,"ramu"]
list1.append("raju")
print(list1)

list2=[7,8,9]
list1.append(list2)
print(list1)

list1.append([2,3])
print(list1)  
  
fruits = ['banana', 'apple','cherry']
points = [1,2,3,4]
fruits.extend(points)
print(fruits)

str="This is my python program"
print(str.find("Python"))

s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1.union(s2))
print(s1&s2)

numbers=[1,3,4]
numbers.clear()
print(numbers)

#intersection 

x={'a','b','c'}
y={'c','d','e'}
z=x&y
print(z)

text1 = "hello mamabro"
print("hello" in text1)
print('2' in [1, 2, 3])

#endswith
str1="hello python..!!!"
print(str1.startswith("p",6))

#sort
list1=['b','cbbbbb','abc']
list1.sort(key=len)
print(list1)



#key
#reverse

#count
a=[1,2,3,2,4,3, [3, 4]]
c=a.count([3, 4])
print(c)

#insert
s=[102,104,101]
n=105
s.insert(1,n)
print(s)
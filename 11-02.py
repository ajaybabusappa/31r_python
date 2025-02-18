#Controls - conditional, loops and jump statements
#Jump statements - break, continue and pass

#Break



for i in range(0, 11):
    print(i)
    print(i)
    if i >= 5:
        break
    print(i)



for i in range(0, 1111):
    print("jhdbfjdkh")
    break


#Continue


for i in range(0, 11):
    if i >= 5:
        continue
    print(i)

count = 0
for i in range(0, 1721):
    count += 1
    continue

print(count)

for i in range(0, 1721):
    break
    continue




#Nested loops

for clss in range(1, 11):
    # if i == 5:
    #     break
    for roll in range(1, 31):
        if clss % 2 == 0 and roll > 15:
            continue
        print(clss, roll)


for clss in range(1, 11):
    for roll in range(1, 31):
        if clss == 5 or roll < 15:
            break
        print(clss, roll)
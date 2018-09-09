# 1
fruit = ['apple','banana','orange','grape','peach']

# 2
for fr in fruit:
    if fr is 'apple':
        print ('I found it!')

# 3
fruit.append('kiwi')
fruit.append('mango')

# 4
length = []
for fr in fruit:
    length.append(len(fr))

# 5
def half_squared(list):
    mid = []
    for i in list:
        mid.append(i*i/2)
    return mid

# 6
a = int(input("input first number: "))

if(a >= 90 & a <= 100):
    print('A')
elif(60 <= a & a < 90):
    print('B')
elif(0 <= a & a < 60):
    print('C')
else:
    print('ERROR!')

# 7
def revSort(a,b,c):
    a,b,c=c,a,b
    return a,b,c

# 8
list1 = [1,2,3]
list2 = [4,5,6]
array = [list1,list2]
for i in array:
    for g in i:
        print(g)

# 9
def num2str(value):
    return list(map(int, str(value)))

result = []
for i in range(101):
    mid = sum(num2str((i+1)**3))    
    if(i+1 == mid):   
        result.append(i+1)
print(result)

# 10
import random
x = random.randint(1,10)
y = random.randint(1,10)
print(x,y)
x,y=y,x
print(x,y)

# 11
for i in range(7):
    print('#',end='')
    if(i<4):
        for j in range(5-i):
            print(' ',end='')
        for k in range(2*i+1):
            print('*',end='')
    else:
        for j in range(i-1):
            print(' ',end='')
        for k in range(13-2*i):
            print('*',end='')
    print()

# 12
number = [1,2,3,4,5,6,1,2,3,4,5,6]
indicator = 0
for x in range(6):
    for i in range(6):
        print(number[i+x],end='')
    print()

# 13
players = ['charles','martina','michael','florence','eli']
for x in range(5):
    players[x] = players[x].capitalize()
print(players[1:4])
print(players[:2])
print(players[2:])
print(players[-3:-1])
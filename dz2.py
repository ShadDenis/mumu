#1
a=int(input())
b=int(input())
for i in range(a,b):
    if i % 7 == 0:
        print(i)

#2
c=int(input())
d=int(input())
e=0
for g in range(c,d):
    print(g)
print(d)
print()
x = d
while x>c:
    print(x)
    x-=1
# print(c)
print()

for i in range(c,d):
    if i % 7 == 0:
        print(i)
print()

for j in range(c,d):
    if j % 5 == 0:
        e+=1
print(e)

#3

f=int(input("Введите число от  1 до 100: "))
if f<0 or f>100:
    print("Error")
else:
    if f % 3==0 and f % 5 == 0:
        print("Fizz Buzz")
    elif f % 3 == 0:
         print("Fizz")
    elif f % 5 == 0:
         print("Bizz")
    else:
        print(f)






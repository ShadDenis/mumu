s1 = input().split(" ")
s2 = input().split(" ")
s = s1+s2
print(s)#1
num1 = []
num2 = []

print(list(set(s)))
for i in s1:
    num1.append(int(i))
for j in s2:
    num2.append(int(j))


#3
print(list(set(num1) & set(num2)))

#4
print(list(set(num1) ^ set(num2)))



#5
print("Минимальное число: " , min(num1), ";" , min(num2), ",Максимальное число: " ,  max(num1), ";" , max(num2))
from hohol import number

#5
# s = input().lower().replace(" ", "")
# print(s)
# reverse_s = s[::-1]
# print(reverse_s)
# if s == reverse_s:
#     print("Строка является полиндромом")
# else:
#     print("Строка является не полиндромом")

#6
s1 = input().split(" ")
s2 = input().split(" ")
s=s1+s2
numbers1 = []
numbers2=[]
numbers = []
for i in s:
    numbers.append(int(i))

print(numbers)
print(set(numbers))
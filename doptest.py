#найти наибольшее число в массиве, являющиеся полным квадратом некоторого числа


num = []
s = input().split(" ")
max_square = 0
for i in range(int(s[0]), int(s[1])):
    sqrt = int(abs(i) ** 0.5)
    # print(sqrt)
    if i == sqrt ** sqrt:
        num.append(i)
print(num)

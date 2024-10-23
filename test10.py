# while True:
#     chislo = int(input())
#     if chislo > 0:
#         print("Положительное")
#     if chislo < 0:
#         print("Отрицательное")
#     if chislo == 0:
#         print("Ноль")
#     if chislo == 7:
#         print("Good Bye")
#         break
from datetime import datetime

# print("Тили тили бом")
# input()
# print("Закрой глаза скорее")
# input()
# print("Кто-то ходит за окном и стучится в двери")
# input()
# print("БУ! Испугался?")



string = input().split(" ")
numbers = []
start_time = datetime.today()
for i in range(int(string[0]), int(string[1])):
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
        if count > 2:
            break
    if count == 2:
        numbers.append(i)
end_time=datetime.today()
delta = end_time - start_time
print("простые числа:",numbers , "\n", delta)



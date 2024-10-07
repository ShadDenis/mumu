string = input ("Введите 3 числа через пробел:\n")
print (string)

numbers = string.split(" ")
print (numbers)
if numbers [3] == "+":
    summa = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    print("Сумма", summa)

if numbers [3] == "*":
    summa = int(numbers[0]) * int(numbers[1]) * int(numbers[2])
    print("Умножение", summa)

# summa2=0
# for i in numbers:
#     summa2+=summa
#print(summa2)






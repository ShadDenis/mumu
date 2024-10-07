# string = input("Введите 3 числа:").split(" ")
# number = []
# for i in string:
#     number.append(int (i))
# print(max(number))
# print(min(number))
# print(sum(number) / len(number))



string = input().split(" ")
number1 = float(string[0])
znak = string[1]
if znak == "m":
    result = (number1 * 0.00062).__format__(".5f")
    print ("mile" , result)
elif znak == "d":
    result = (number1 * 39.3701).__format__(".5f")
    print("dume" , result)
elif znak == "y":
    result = (number1 * 1.09361).__format__(".5f")
    print("yard" , result)
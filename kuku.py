# string = input()
# numbers = string.split(" ")
# if len(numbers)==4:
#     result = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
#     print(result)
# elif len(numbers)==3:
#     result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
#     print(result)
# elif len(numbers) < 1:
#     print("данные не введены")
# else:
#     result = (float(numbers[0]) / float(numbers[1])).__format__(".4f")
#     print("/ " , result)
#     print("Введено 1 или 2 числа")


# numbers = string.split(" ")
# integer = len(numbers)
# print(integer)
# match numbers:
#     case 4:
#         result = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
#         print(result)
#     case 3:
#         result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
#         print (result)
#     case 2:
#         result = (float(numbers[0]) / float(numbers[1])).__format__(".4f")
#         print(result)
#     case 1: print("Введено 1 или 2 числа")

# a = 0
# while a <= 5:
#     # print("Мы в цикле")
#     print(a)
#     a +=1
#     if a == 3:
#         a+=1
# else:
#     print("Закончили выполнение цикла while")
#     b=10
#     while b > 0:
#         print(b)
#         b-=1


for i in range(-9,15):
    print(i,i%13)
    if i % 13 == 0 and i != 0:
        print("ytfyf",i)
        break



# else:
#     print("Завершение")



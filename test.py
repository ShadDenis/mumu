# string = (input().split(" "))
# numbers = []
# for i in string:
#     numbers.append(int(i))
#     numbers.sort()
# print(numbers)
#пузырьковая сортировка




# string = input("Введите число и степень: ").split(" ")
# number = int(string[0])
# stepen = int(string[1])
# if 0<= stepen <= 7: #stepen > 0 and stepen <=7:
#     result = number ** stepen
#     print(result)



#3
# string = input("Введите стоимость с кого звоним, куда звоним:").split(" ")
# price = float(string[0])
# # mtot = 0 # с мтс на теле 0.2 m
# # mtob = 1 # с мтс на билайн 0.3 b
# # ttob = 2 # с теле на билайн 0.4 t
# # mtom = 3 #  мтс 0.1
# # btob = 4 # билайн 0.1
# # ttot = 5 # теле 0.1
# if string[1] == "m" and string [2] == "t":
#     result = price * 0.2
#     print(result)




#4
string=input().split(" ")
# manager1 = int(string [0])
# manager2 = int(string [1])
# manager3 = int(string [2])
base = 200 #Базовая ставка 200
percent = 0
premiya = 0
status = 0
# zp_all = []
# for i in string:
#     zp_all.append(int(i))
# zp_all.sort(reverse = True)
# print(zp_all[0])
if int(string[0]) > int(string[1]) or int(string[0]) > int(string[2]):
    status = 0
elif int(string[1]) > int(string[2]) or int(string[1]) > int(string[0]):
    status = 1
elif int(string[2]) > int(string[1]) or int(string[2]) > int(string[0]):
    status = 2
print(status)

k=0

for i in string:
    zp = int(i)
    if 0 < zp < 500:
        percent = 0.03
    elif 500 <= zp  < 1000:
         percent = 0.05
    elif zp >= 1000:
         percent = 0.08

    if k -1 == status:
          print("Менеджер №: " , k,  base *(1+ percent) + premiya)
    else:
          print("Менеджер №: " , k , base *(1+ percent))
    k+=1
# чезабретто




    print(int(i))

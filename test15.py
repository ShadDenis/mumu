

# x = 5
# y = 5
# print(x is y)# is это ==



#треугольнички
#ж
# print(" " * 20, "_" * 43 )
# i = 1
# while i < 40:
#     print(" "*20 + "|" ,
#     "*" * i if i <=20 else "*" * (40 - i),
#     " " * (40-i) if i<= 20 else " " * i ,
#     "|")
#     i+=1
# print(" " * 20, "-" * 43 )


#е
# print(" " * 29, "_" * 45 )
# i = 1
# while i < 40:
#     if i <= 20:
#         print(" " * 20 + "|",
#         "*" * i, " " *(40 - i * 2), "*" * i , "|" )
#     else:
#         print(" " * 20 + "|",
#              "*" * (40-i),
#              " " * ((i - 20) * 2),
#              "*" * (40-i), "|")
#     i+=1
#
#     print(" " * 20, "-" * 43 )
    #не успел((((




#13
#№2
spisok = [-1, -2, -4, -5, 0, 3, 3, 5, 6, 63, 3, 4]
positive = 0
negative = 0
nulls = 0
s = 10
for x in spisok:
    try:                        #
      print(s / x)              #
    except:                     #
        print("деление на ноль")#
#     if x < 0:
#         negative+=1
#     if x > 0:
#         positive+=1
#     if x == 0:
#         nulls+=1
#
#
# print(max(spisok))
# print(min(spisok))
# print(positive, negative, nulls)
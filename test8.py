# a1=1
# a2=2
# a3=3
# # a=["мяу" , "гав" , "му" , "кря"]
# a=[1,2,3,4]
# print(len(a))
# b=[]
# print(b)
# for i in range(len(a)):
#     b.append(i+10)
# print(b)
# b.pop()
# print(b)
# b[2] = 300
# print(b)
# b.insert(1,340)
# b.pop




# list_1= [i*2 for i in range(100) if i%3 ==0]
# print(list_1 )
#
# list_2 =[]
# for i in range(100):
#     if i%3==0:
#         i*=2
#         list_2.append(i)
# print(list_2)



# costomers=["Bob", "Anna", "Joe", "Nick","Bill"]
# list2=[i for i in costomers if i!=costomers[1]]
# print(list2)




# string = input().split(" ")
#
# even = 0
# even_numbers = [0]
# odds = 0
# odds_numbers = [0]
# int9 = 0
# int9_numbers = [0]
#
# for i in range(int(string[0]), int(string[1])):
#     if i % 2 == 0:
#         even+=1
#         even_numbers.append(i)
#     if i % 2 != 0:
#         odds+=1
#         odds_numbers.append(i)
#     if i % 9 == 0:
#         int9 +=1
#         int9_numbers.append(i)
#
# print("Кол-во четных: " , even, "ср. арефм.: ",sum(even_numbers) / even )
# print("Кол-во нечетных: " , odds, "ср. арефм.: ",sum(odds_numbers) / odds )
# print("Кол-во кратных 9: " , int9, "ср. арефм.: ",sum(int9_numbers) / int9)


# string = input().split(" ")
# even = [i for i in range(int(string[0]), int(string[1])) if i%2==0]
# odds = [i for i in range(int(string[0]), int(string[1]))if i%2!=0]
# int9 = [i for i in range(int(string[0]), int(string[1])) if i%9==0]
# print("Кол-во четных: ", len(even), "ср. арефм.: ", sum(even) / len(even))
# print("Кол-во нечетных: ", len(odds), "ср. арефм.: ", sum(odds) / len(odds))
# print("Кол-во кратных 9: " , len(int9), "ср. арефм.: ",sum(int9) / len(int9))

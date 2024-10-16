string = input().split(" ")
number = []
zp = 200
premia = 0
volume_all = []
for i in string:
    volume_all.append(int(i))
print(string)
index_meneger = 0
max_volume = 0
for i in string:
    volume = int(i)
    #print(volume)
    max_volume = max(max_volume, volume) #
    # print("premia" , premia)
    # if max_volume >= volume:
    #     zp += premia
    if 0 < volume <500:
        zp *=1.03
    elif 500<=volume<=1000:
        zp*=1.05
    elif volume>1000:
        zp*=1.08
    #print(zp)
    number.append(zp)
    #print(number)

k=0
count_max = 0
for i in string:
    max_volume = max(volume_all)
    if max_volume == int(i):
        count_max += 1
print("кол-во максимальных значений:", count_max)


k=0
for i in string:
    max_volume = max(volume_all)
    print(max_volume)
    if max_volume == int(i):
        print("макс оъем:" , i)
        number [k] += premia /count_max
    k+=1


for j in string:
    max_volume = max(volume_all)
    print(max_volume)
    if max_volume == int(j):
        print("max volume" , j)
        number[k] += premia / count_max
    k+=1





#         print("max volume ",max_volume, "j ",int(j))
#         if max_volume == int(j):
#             print("нашли индекс менеджера")
#             number[j.index(j)] += premia
# print(max(number))


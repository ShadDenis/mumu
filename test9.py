# list4=[i*i for i in range(1,11)]
# print(list4)




# costomers = ["Bob", "Anna", "Joe", "Bob" ,"Nick"]
# result = ""
# for  i in costomers:
#     result += i + " "
#     print(i)
# # print(result.split("-")[:-1])
# print(result.rstrip(" ").split(" ")[:3])


a1=10
b1=20
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [a1,[13,14,[15,16,"OK"]],12,b1]]
# print(matrix[3][1][2][2])
search = "OK"
for i in matrix:
    print("Уровень 1", i)
    if search in i:
        print("Нашли  OK")
        break
    else:
        for vtoroy in i:
            print("2 уровень", vtoroy)
            if search == vtoroy:
                print("Нашли  OK")
                break
            else:
                if type(vtoroy) is list:
                    for tretiy in vtoroy:
                        print(tretiy)
                        if search == tretiy:
                            print("Нашли  OK")
                            break
                        else:
                            if type(tretiy) is list:
                                for chetv in tretiy:
                                    print(chetv)
                                    if search == chetv:
                                        print("Нашли  OK")
                                        break

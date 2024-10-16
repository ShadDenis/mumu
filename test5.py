# string = input().split(" ")
# begin = int(string [0])
# end = int(string[1])
# result = ""
# for j in range(begin, end + 1):
#     j = end
#     result += str(j) + " "
#     j-=2
#         # print(i)
# print(result)



string = input().split(" ")
begin = int(string [0])
end = int(string[1])
count = 0
for i in range(begin, end + 1):
    if i%5 == 0 and i !=0:
        count+=1
print(count)
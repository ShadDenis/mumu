string = input().split(" ")
begin = int(string [0])
end = int(string[1])
result = ""

for number in range(begin, end + 1):
    if number % 3 == 0 and number % 5 !=0:
        result += "Fizz" + str(number) + ", "
    elif number % 5 == 0 and number % 3 !=0:
        result += "Buzz" + str(number) + ",  "
    elif number % 15 == 0:
        result += "Fizz Buzz" + str(number) + ",  "
    else:
        result += "Число" + str(number) + ",  "
print(result)
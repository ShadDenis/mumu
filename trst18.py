import re
s = input()
operation = re.findall(r'[\-/\+*]' ,s)
print(operation)
numbers = re.split(r'[\-/\+*]',
                   s.replace(" ", ""))
nominal = ["*" , "/" , "**" , "-" , "+"]
print(numbers, operation)

for j in nominal:
    for k in range(operation.count(j)):
        i = 0
        finded = False
        while i < len(operation):
            temp = []
            if j == "*" and j == operation[i]:
                finded = True
                temp.append(float(numbers[i]) * float(numbers[i+1]))
            elif j == "/" and j == operation[i]:
                finded = True
                temp.append(float(numbers[i]) / float(numbers[i+1]))
            elif j == "**" and j == operation[i]:
                finded = True
                temp.append(float(numbers[i]) ** float(numbers[i+1]))
            elif j == "-" and j == operation[i]:
                finded = True
                temp.append(float(numbers[i]) - float(numbers[i+1]))
            elif j == "+" and j == operation[i]:
                finded = True
                temp.append(float(numbers[i]) + float(numbers[i+1]))
            if finded:
                numbers.pop(i)
                numbers.pop(i)
                numbers.insert(i, temp[0])
                operation.pop(i)
            i+=1
print(numbers)
print(eval("10 + 30"))


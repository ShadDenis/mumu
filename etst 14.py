#регулярные выражения
import re
s = input("введите логин: ")
# pattern = "(user)|(admin)+"
# pattern = "{3}[0-9]+"
pattern = r'\d\d\d'
st = re.findall(pattern, s)
# st = re.search(pattern, s)
# st = re.match(pattern, s)
# st = re.sub(pattern,"0000", s)
# st = re.split(pattern, s)
print(st)
if not st:
    print("логин верный:" , s)###пишем в базу

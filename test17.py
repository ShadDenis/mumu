#функции

# def test17(a, b):
#     print(a , b)
# test17("1" , "6")

# def test17(a =1, b =6):
#     c = a+b
#     print(a , b)
#     return c
# result = test17()
# print(result)

def test17(s = "", a =1 , b=1):
    if not s: s = "Пустая строка"
    d=s
    print(d)
    def sl(d = ""):
        e =d.lower()
        return e
    return sl(d)
test17("Lalala")

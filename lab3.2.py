a = input("Введите слово: ")
res = ""
while a != "stop":
    res = res + a + " "
    a = input("Введите слово: ")
print(res)
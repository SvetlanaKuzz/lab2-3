n = int(input("Введите количество слов: "))
res = ""
for i in range(n):
    a = input("Введите слово: ")
    res = res + a + " "
print(res)
a = input("Введите первый цвет: ")
b = input("Введите второй цвет: ")
if a.lower() != "красный" and a.lower() !="желтый" and a.lower() !="синий":
    print("Ошибка цвета")
elif b.lower() != "красный" and b.lower() !="желтый" and b.lower() !="синий":
    print("Ошибка цвета")
elif a.lower() == "красный" and b.lower() == "синий" or a.lower() == "синий" and b.lower() == "красный":
    print("фиолетовый")
elif a.lower() == "красный" and b.lower() == "желтый" or a.lower() == "желтый" and b.lower() == "красный":
    print("оранжевый")
elif a.lower() == "синий" and b.lower() == "желтый" or a.lower() == "желтый" and b.lower() == "синий":
    print("зеленый")
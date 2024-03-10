import random
correct_a = 0
wrong_a = 0
max_wrong = 3
while wrong_a < max_wrong:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = int(input(f"{a} + {b} = "))
    ans = a + b
    if c == ans:
        correct_a = correct_a + 1
        print("Правильно!")
    else:
        wrong_a = wrong_a + 1
        print("Неправильно!")
print("Игра окончена. Правильных ответов: ", correct_a)

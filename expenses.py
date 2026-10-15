a1 = int(input("введите первое число: "))
a2 = int(input("введите второе число: "))
a3 = int(input("введите третье число: "))
a4 = int(input("введите четвёртое число: "))
a5 = int(input("введите пятое число: "))
a6 = int(input("введите шестое число: "))
a7 = int(input("введите седьмое число: "))

things = [a1, a2, a3, a4, a5, a6, a7]

summ = sum(things)
sred = (summ / 7)
min = min(things)
max = max(things)

print(summ)
print(sred)
print(min)
print(max)

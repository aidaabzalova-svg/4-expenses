rub, cop = input("введите: РУБЛИ КОПЕЙКИ: ").strip().lower().split()

if len(cop)<2:
    cop = cop + "0000"
    cop = cop[:2]

try:
    if (int(rub) <= 0):
        print(f"0.{cop} ₽")

    if (int(rub) > 0):
        print(f"{rub}.{cop} ₽")

except (ValueError, IndexError):
    print("Некорректный формат суммы")

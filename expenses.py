def main() -> None:
    parts = input("Введите сумму: ").lower().split()
    rubles = {"руб", "рубль", "рубля", "рублей"}
    kopecks = {"коп", "копейка", "копейки", "копеек"}

    kopecks = kopecks[:2]

    if len(parts) == 2 and parts[1] in rubles:
        rubl2es = parts[0]
        kope2ckses = "0"
    elif (
        len(parts) == 4
        and parts[1] in rubles
        and parts[3] in kopecks
    ):
        rubl2es = parts[0]
        kope2ckses = parts[2]
    else:
        print("Некорректный формат суммы")
        return

    if not rubl2es.isdigit() or not kope2ckses.isdigit():
        print("Некорректный формат суммы")
        return

    rubles = int(rubl2es)
    kopecks = int(kope2ckses)
    if kopecks > 99:
        print("Некорректный формат суммы")
        return
    
    print(f"{rubles}.{kopecks} ₽")


if __name__ == "__main__":
    main()

# =====================================================
#  СВОЯ ИГРА (Jeopardy!)
#  Аналог задания "Coffee Shop System" - Хичээл 3
# =====================================================
#
#  Что нового по сравнению с кофейней:
#    у данных ДВА уровня иерархии - тема, а внутри темы цена.
#    Выбор идёт сверху вниз: тема -> цена -> вопрос -> вариант ответа.
#
#  Ашиглах зүйлс: жагсаалт, dictionary, for, if, while, open, функц
#  Ашиглахгүй зүйлс: import, class, try/except, list comprehension
#
#  Проверка:      python proverka.py
#  Запуск игры:   python svoya_igra.py
# =====================================================


FAIL = "voprosy.txt"
PROTOKOL_FAIL = "protokol.txt"


# -----------------------------------------------------
#  ВЕСЬ ТЕКСТ ИНТЕРФЕЙСА ЛЕЖИТ В ОДНОМ СЛОВАРЕ.
#  Чтобы перевести игру на другой язык - меняется только
#  этот словарь, ни одной строчки кода трогать не нужно.
# -----------------------------------------------------

TEKST = {
    "zagolovok": "=========  СВОЯ ИГРА  =========",
    "menu_1": "1 - Показать табло",
    "menu_2": "2 - Выбрать вопрос",
    "menu_3": "3 - Мой счёт и журнал",
    "menu_4": "4 - Список тем",
    "menu_5": "5 - Сохранить протокол и выйти",
    "menu_0": "0 - Выйти без сохранения",
    "vybor": "Ваш выбор: ",
    "nomer_temy": "Номер темы: ",
    "cena_voprosa": "Цена вопроса: ",
    "dostupno": "Доступные цены: ",
    "vash_otvet": "Ваш ответ (номер варианта): ",
    "verno": "ВЕРНО! Плюс",
    "neverno": "Неверно. Минус",
    "pravilno_bylo": "Правильный ответ: ",
    "schet": "Счёт: ",
    "ball": "балл(ов)",
    "net_temy": "Такой темы нет.",
    "net_ceny": "Такой цены в этой теме нет.",
    "uzhe_sygran": "Этот вопрос уже сыгран. Выберите другой.",
    "tolko_chislo": "Нужно ввести число.",
    "zhurnal_pust": "Вы ещё не ответили ни на один вопрос.",
    "igra_okonchena": "Все вопросы сыграны. Игра окончена.",
    "protokol_sohranen": "Протокол сохранён: ",
    "voprosy_ne_prochitany": "Вопросы не прочитаны. Проверьте функцию voprosy_prochitat.",
    "poka": "До встречи!",
    "za": " за ",
    "oshibka_vybora": "Неверный пункт меню.",
}


# -----------------------------------------------------
# 1. voprosy_prochitat(fail)
# -----------------------------------------------------
# Строка файла выглядит так:
#     КОСМОС|300|Кто первым полетел в космос?|А;Б;В;Г|4
#     тема | цена | вопрос | варианты через ; | номер верного
#
# Каждую строку превращаем в dictionary, все складываем в список.
#
# Возвращает:
#   [{"tema": "КОСМОС", "cena": 300, "vopros": "...",
#     "varianty": ["А", "Б", "В", "Г"], "verno": 4}, ...]

def voprosy_prochitat(fail):
    voprosy = []
    with open(fail, encoding="utf-8") as f:
        for stroka in f:
            stroka = stroka.strip()
            if stroka == "":
                continue
            chast = stroka.split("|")
            vopros = {
                "tema": chast[0],
                "cena": int(chast[1]),
                "vopros": chast[2],
                "varianty": chast[3].split(";"),
                "verno": int(chast[4]),
            }
            voprosy.append(vopros)
    return voprosy


# -----------------------------------------------------
# 2. temy_spisok(voprosy)  -  ПЕРВЫЙ УРОВЕНЬ ИЕРАРХИИ
# -----------------------------------------------------
# Список тем без повторов, в том порядке, в каком они идут в файле.
#
#   temy_spisok(voprosy) -> ["КОСМОС", "ГЕОГРАФИЯ", ...]

def temy_spisok(voprosy):
    temy = []
    for vopros in voprosy:
        if vopros["tema"] not in temy:
            temy.append(vopros["tema"])
    return temy


# -----------------------------------------------------
# 3. ceny_temy(voprosy, tema)  -  ВТОРОЙ УРОВЕНЬ ИЕРАРХИИ
# -----------------------------------------------------
# Все цены внутри одной темы.
#
#   ceny_temy(voprosy, "КОСМОС") -> [100, 200, 300, 400, 500]
#   ceny_temy(voprosy, "МУЗЫКА") -> []

def ceny_temy(voprosy, tema):
    ceny = []
    for vopros in voprosy:
        if vopros["tema"] == tema:
            ceny.append(vopros["cena"])
    return ceny


# -----------------------------------------------------
# 4. vopros_naiti(voprosy, tema, cena)
# -----------------------------------------------------
# Поиск по ДВУМ ключам сразу: тема и цена.
# Нашли - возвращаем сам dictionary, не нашли - None.

def vopros_naiti(voprosy, tema, cena):
    for vopros in voprosy:
        if vopros["tema"] == tema and vopros["cena"] == cena:
            return vopros
    return None


# -----------------------------------------------------
# 5. sygran(zhurnal, tema, cena)
# -----------------------------------------------------
# Был ли этот вопрос уже сыгран. True / False.
#
# Журнал - это список записей вида:
#   {"tema": "КОСМОС", "cena": 300, "verno": True}

def sygran(zhurnal, tema, cena):
    for zapis in zhurnal:
        if zapis["tema"] == tema and zapis["cena"] == cena:
            return True
    return False


# -----------------------------------------------------
# 6. tablo_pokazat(voprosy, zhurnal)
# -----------------------------------------------------
# Печатает игровое табло. Сыгранные клетки закрыты прочерком.
#
#   1. КОСМОС         ---   200   300   400   500
#   2. ГЕОГРАФИЯ      100   200   ---   400   500

def tablo_pokazat(voprosy, zhurnal):
    temy = temy_spisok(voprosy)
    nomer = 1
    for tema in temy:
        stroka = str(nomer) + ". " + tema.ljust(14)
        for cena in ceny_temy(voprosy, tema):
            if sygran(zhurnal, tema, cena):
                stroka = stroka + "   ---"
            else:
                stroka = stroka + "   " + str(cena).rjust(3)
        print(stroka)
        nomer = nomer + 1


# -----------------------------------------------------
# 7. vopros_pokazat(vopros)
# -----------------------------------------------------
# Печатает сам вопрос и пронумерованные варианты. Ничего не возвращает.

def vopros_pokazat(vopros):
    print()
    print(vopros["tema"] + TEKST["za"] + str(vopros["cena"]))
    print(vopros["vopros"])
    nomer = 1
    for variant in vopros["varianty"]:
        print("   " + str(nomer) + ") " + variant)
        nomer = nomer + 1


# -----------------------------------------------------
# 8. otvet_proverit(vopros, nomer)
# -----------------------------------------------------
# Верный ли номер варианта выбрал игрок. True / False.

def otvet_proverit(vopros, nomer):
    if nomer == vopros["verno"]:
        return True
    return False


# -----------------------------------------------------
# 9. ochki_podschitat(zhurnal)
# -----------------------------------------------------
# Счёт по правилам Jeopardy: верный ответ прибавляет цену,
# неверный - вычитает её.

def ochki_podschitat(zhurnal):
    ochki = 0
    for zapis in zhurnal:
        if zapis["verno"]:
            ochki = ochki + zapis["cena"]
        else:
            ochki = ochki - zapis["cena"]
    return ochki


# -----------------------------------------------------
# 10. protokol_sohranit(zhurnal, fail)
# -----------------------------------------------------
# Записывает ход игры в файл и возвращает имя файла.
#
# Содержимое файла:
#   КОСМОС,300,+
#   КИНО,200,-
#   ITOGO,100

def protokol_sohranit(zhurnal, fail):
    with open(fail, "w", encoding="utf-8") as f:
        for zapis in zhurnal:
            if zapis["verno"]:
                znak = "+"
            else:
                znak = "-"
            f.write(zapis["tema"] + "," + str(zapis["cena"]) + "," + znak + "\n")
        f.write("ITOGO," + str(ochki_podschitat(zhurnal)) + "\n")
    return fail


# =====================================================
#  ИГРА. Здесь собирается вся иерархия выбора:
#  меню -> тема -> цена -> вопрос -> вариант ответа.
# =====================================================

def igrat():
    voprosy = voprosy_prochitat(FAIL)

    if not voprosy:
        print(TEKST["voprosy_ne_prochitany"])
        return

    zhurnal = []

    while True:
        print()
        print(TEKST["zagolovok"])
        print(TEKST["menu_1"])
        print(TEKST["menu_2"])
        print(TEKST["menu_3"])
        print(TEKST["menu_4"])
        print(TEKST["menu_5"])
        print(TEKST["menu_0"])

        vybor = input(TEKST["vybor"]).strip()

        # ---------- табло ----------
        if vybor == "1":
            tablo_pokazat(voprosy, zhurnal)

        # ---------- выбор вопроса: тема -> цена -> ответ ----------
        elif vybor == "2":
            tablo_pokazat(voprosy, zhurnal)
            temy = temy_spisok(voprosy)

            # уровень 1: тема
            vvod = input(TEKST["nomer_temy"]).strip()
            if not vvod.isdigit():
                print(TEKST["tolko_chislo"])
                continue
            nomer_temy = int(vvod)
            if nomer_temy < 1 or nomer_temy > len(temy):
                print(TEKST["net_temy"])
                continue
            tema = temy[nomer_temy - 1]

            # уровень 2: цена
            ceny = ceny_temy(voprosy, tema)
            stroka = ""
            for cena in ceny:
                if not sygran(zhurnal, tema, cena):
                    stroka = stroka + str(cena) + " "
            if stroka == "":
                print(TEKST["uzhe_sygran"])
                continue
            print(TEKST["dostupno"] + stroka)

            vvod = input(TEKST["cena_voprosa"]).strip()
            if not vvod.isdigit():
                print(TEKST["tolko_chislo"])
                continue
            cena = int(vvod)
            if cena not in ceny:
                print(TEKST["net_ceny"])
                continue
            if sygran(zhurnal, tema, cena):
                print(TEKST["uzhe_sygran"])
                continue

            # уровень 3: сам вопрос
            vopros = vopros_naiti(voprosy, tema, cena)
            if vopros is None:
                print(TEKST["net_ceny"])
                continue
            vopros_pokazat(vopros)

            # уровень 4: вариант ответа
            vvod = input(TEKST["vash_otvet"]).strip()
            if not vvod.isdigit():
                print(TEKST["tolko_chislo"])
                continue
            nomer_otveta = int(vvod)

            if otvet_proverit(vopros, nomer_otveta):
                print(TEKST["verno"], cena)
                zhurnal.append({"tema": tema, "cena": cena, "verno": True})
            else:
                print(TEKST["neverno"], cena)
                print(TEKST["pravilno_bylo"] + vopros["varianty"][vopros["verno"] - 1])
                zhurnal.append({"tema": tema, "cena": cena, "verno": False})

            print(TEKST["schet"] + str(ochki_podschitat(zhurnal)))

            if len(zhurnal) == len(voprosy):
                print(TEKST["igra_okonchena"])
                fail = protokol_sohranit(zhurnal, PROTOKOL_FAIL)
                print(TEKST["protokol_sohranen"] + fail)
                break

        # ---------- журнал ----------
        elif vybor == "3":
            if not zhurnal:
                print(TEKST["zhurnal_pust"])
            else:
                for zapis in zhurnal:
                    if zapis["verno"]:
                        znak = "+"
                    else:
                        znak = "-"
                    print(" " + znak + " " + zapis["tema"] + TEKST["za"] + str(zapis["cena"]))
                print(TEKST["schet"] + str(ochki_podschitat(zhurnal)) + " " + TEKST["ball"])

        # ---------- список тем ----------
        elif vybor == "4":
            nomer = 1
            for tema in temy_spisok(voprosy):
                print(" " + str(nomer) + ". " + tema.ljust(14) + str(len(ceny_temy(voprosy, tema))))
                nomer = nomer + 1

        # ---------- сохранить и выйти ----------
        elif vybor == "5":
            if not zhurnal:
                print(TEKST["zhurnal_pust"])
            else:
                fail = protokol_sohranit(zhurnal, PROTOKOL_FAIL)
                print(TEKST["protokol_sohranen"] + fail)
            break

        elif vybor == "0":
            print(TEKST["poka"])
            break

        else:
            print(TEKST["oshibka_vybora"])


if __name__ == "__main__":
    igrat()

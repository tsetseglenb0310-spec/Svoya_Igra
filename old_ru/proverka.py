# =====================================================
#  Файл проверки. ЕГО НЕ МЕНЯЕМ.
#  Запуск:  python proverka.py
# =====================================================

import svoya_igra as si

dun = 0
niit = 0


def shalga(ner, garsan, huleesen):
    global dun, niit
    niit = niit + 1
    if garsan == huleesen:
        dun = dun + 1
        print("  OK     ", ner)
    else:
        print("  ОШИБКА ", ner)
        print("          получено :", garsan)
        print("          ожидалось:", huleesen)


def heseg(ner):
    print()
    print("---", ner, "---")


V = [
    {"tema": "КОСМОС", "cena": 100, "vopros": "Ближайшая к Солнцу планета?",
     "varianty": ["Венера", "Меркурий", "Марс", "Земля"], "verno": 2},
    {"tema": "КОСМОС", "cena": 200, "vopros": "Наша галактика?",
     "varianty": ["Андромеда", "Треугольник", "Млечный Путь", "Сомбреро"], "verno": 3},
    {"tema": "КИНО", "cena": 100, "vopros": "Режиссёр Титаника?",
     "varianty": ["Спилберг", "Кэмерон", "Скотт", "Нолан"], "verno": 2},
    {"tema": "КИНО", "cena": 300, "vopros": "Кто сыграл Нео?",
     "varianty": ["Круз", "Питт", "Ривз", "Смит"], "verno": 3},
]

ZHURNAL = [
    {"tema": "КОСМОС", "cena": 100, "verno": True},
    {"tema": "КИНО", "cena": 300, "verno": False},
]

print("=========================================")
print("  СВОЯ ИГРА - проверка")
print("=========================================")

# ---------- 1 ----------
heseg("1. voprosy_prochitat")
v = si.voprosy_prochitat("voprosy.txt")
shalga("вопросы прочитаны", len(v), 25)
if v:
    shalga("цена это число", type(v[0]["cena"]), int)
    shalga("варианты это список", type(v[0]["varianty"]), list)
    shalga("вариантов четыре", len(v[0]["varianty"]), 4)
    shalga("номер верного это число", type(v[0]["verno"]), int)
    shalga("первая тема", v[0]["tema"], "КОСМОС")
else:
    print("  ОШИБКА  список пуст, дальше проверять нечего")
    niit = niit + 5

# ---------- 2 ----------
heseg("2. temy_spisok")
shalga("темы без повторов", si.temy_spisok(V), ["КОСМОС", "КИНО"])
shalga("пустой список", si.temy_spisok([]), [])

# ---------- 3 ----------
heseg("3. ceny_temy")
shalga("цены темы КОСМОС", si.ceny_temy(V, "КОСМОС"), [100, 200])
shalga("цены темы КИНО", si.ceny_temy(V, "КИНО"), [100, 300])
shalga("темы нет", si.ceny_temy(V, "МУЗЫКА"), [])

# ---------- 4 ----------
heseg("4. vopros_naiti")
shalga("вопрос есть", si.vopros_naiti(V, "КИНО", 300), V[3])
shalga("цены нет в этой теме", si.vopros_naiti(V, "КИНО", 200), None)
shalga("темы нет", si.vopros_naiti(V, "МУЗЫКА", 100), None)

# ---------- 5 ----------
heseg("5. sygran")
shalga("уже сыгран", si.sygran(ZHURNAL, "КОСМОС", 100), True)
shalga("ещё не сыгран", si.sygran(ZHURNAL, "КОСМОС", 200), False)
shalga("пустой журнал", si.sygran([], "КИНО", 300), False)

# ---------- 6 ----------
heseg("6. tablo_pokazat")
print("  (ниже должно быть 2 строки, закрытые клетки с прочерком)")
si.tablo_pokazat(V, ZHURNAL)

# ---------- 7 ----------
heseg("7. vopros_pokazat")
print("  (ниже должен быть вопрос и 4 пронумерованных варианта)")
si.vopros_pokazat(V[0])

# ---------- 8 ----------
heseg("8. otvet_proverit")
shalga("верный ответ", si.otvet_proverit(V[0], 2), True)
shalga("неверный ответ", si.otvet_proverit(V[0], 1), False)

# ---------- 9 ----------
heseg("9. ochki_podschitat")
shalga("пустой журнал", si.ochki_podschitat([]), 0)
shalga("плюс и минус", si.ochki_podschitat(ZHURNAL), -200)
shalga("три записи", si.ochki_podschitat(ZHURNAL + [{"tema": "КИНО", "cena": 100, "verno": True}]), -100)

# ---------- 10 ----------
heseg("10. protokol_sohranit")

with open("test_protokol.txt", "w", encoding="utf-8") as f:
    f.write("")

fail = si.protokol_sohranit(ZHURNAL, "test_protokol.txt")
shalga("вернул имя файла", fail, "test_protokol.txt")

aguulga = open("test_protokol.txt", encoding="utf-8").read().strip()
if aguulga == "":
    print("  ОШИБКА  файл пустой, protokol_sohranit ничего не записал")
    niit = niit + 3
else:
    stroki = aguulga.split("\n")
    shalga("три строки", len(stroki), 3)
    shalga("первая строка", stroki[0].strip(), "КОСМОС,100,+")
    shalga("последняя строка", stroki[-1].strip(), "ITOGO,-200")

# ---------- итог ----------
print()
print("=========================================")
print("  ИТОГ:", dun, "/", niit)
if dun == niit:
    print("  Всё верно. Запускай:  python svoya_igra.py")
else:
    print("  Есть незаконченные функции. Смотри строки ОШИБКА выше.")
print("=========================================")

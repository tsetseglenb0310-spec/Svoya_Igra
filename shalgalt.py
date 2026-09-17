# =====================================================
#  Шалгалтын файл. ҮҮНИЙГ ӨӨРЧЛӨХГҮЙ.
#  Ажиллуулах:  python shalgalt.py
# =====================================================

import togloom as tg

dun = 0
niit = 0


def shalga(ner, garsan, huleesen):
    global dun, niit
    niit = niit + 1
    if garsan == huleesen:
        dun = dun + 1
        print("  OK     ", ner)
    else:
        print("  АЛДАА  ", ner)
        print("          гарсан  :", garsan)
        print("          хүлээсэн:", huleesen)


def heseg(ner):
    print()
    print("---", ner, "---")


A = [
    {"sedev": "PYTHON ҮНДЭС", "une": 100, "asuult": "Python-г хэн зохиосон бэ?",
     "songolt": ["Торвальдс", "ван Россум", "Гослинг", "Ричи"], "zov": 2},
    {"sedev": "PYTHON ҮНДЭС", "une": 200, "asuult": "Хэвлэх функц?",
     "songolt": ["echo()", "write()", "print()", "cout()"], "zov": 3},
    {"sedev": "МАШИН СУРГАЛТ", "une": 100, "asuult": "Машин сургалтын сан?",
     "songolt": ["scikit-learn", "requests", "flask", "pygame"], "zov": 1},
    {"sedev": "МАШИН СУРГАЛТ", "une": 300, "asuult": "Хэт цээжлэхийг юу гэх вэ?",
     "songolt": ["Underfitting", "Overfitting", "Dropout", "Backprop"], "zov": 2},
]

BURTGEL = [
    {"sedev": "PYTHON ҮНДЭС", "une": 100, "zov": True},
    {"sedev": "МАШИН СУРГАЛТ", "une": 300, "zov": False},
]

print("=========================================")
print("  ОЮУНЫ ТОГЛООМ - шалгалт")
print("=========================================")

# ---------- 1 ----------
heseg("1. asuult_unshih")
a = tg.asuult_unshih("asuultuud.txt")
shalga("асуултууд уншигдсан", len(a), 25)
if a:
    shalga("үнэ нь тоо", type(a[0]["une"]), int)
    shalga("сонголт нь жагсаалт", type(a[0]["songolt"]), list)
    shalga("сонголт дөрөв", len(a[0]["songolt"]), 4)
    shalga("зөв хариултын дугаар тоо", type(a[0]["zov"]), int)
    shalga("эхний сэдэв", a[0]["sedev"], "PYTHON ҮНДЭС")
else:
    print("  АЛДАА   жагсаалт хоосон, цааш шалгах зүйл алга")
    niit = niit + 5

# ---------- 2 ----------
heseg("2. sedev_jagsaalt")
shalga("сэдэв давхардаагүй", tg.sedev_jagsaalt(A), ["PYTHON ҮНДЭС", "МАШИН СУРГАЛТ"])
shalga("хоосон жагсаалт", tg.sedev_jagsaalt([]), [])

# ---------- 3 ----------
heseg("3. sedev_une")
shalga("PYTHON ҮНДЭС сэдвийн үнэ", tg.sedev_une(A, "PYTHON ҮНДЭС"), [100, 200])
shalga("МАШИН СУРГАЛТ сэдвийн үнэ", tg.sedev_une(A, "МАШИН СУРГАЛТ"), [100, 300])
shalga("байхгүй сэдэв", tg.sedev_une(A, "ХӨГЖИМ"), [])

# ---------- 4 ----------
heseg("4. asuult_haih")
shalga("асуулт олдсон", tg.asuult_haih(A, "МАШИН СУРГАЛТ", 300), A[3])
shalga("энэ сэдэвт тийм үнэ алга", tg.asuult_haih(A, "МАШИН СУРГАЛТ", 200), None)
shalga("байхгүй сэдэв", tg.asuult_haih(A, "ХӨГЖИМ", 100), None)

# ---------- 5 ----------
heseg("5. toglson")
shalga("аль хэдийн тоглогдсон", tg.toglson(BURTGEL, "PYTHON ҮНДЭС", 100), True)
shalga("хараахан тоглогдоогүй", tg.toglson(BURTGEL, "PYTHON ҮНДЭС", 200), False)
shalga("хоосон бүртгэл", tg.toglson([], "МАШИН СУРГАЛТ", 300), False)

# ---------- 6 ----------
heseg("6. sambar_haruulah")
print("  (доор 2 мөр, тоглогдсон нүд зураастай байх ёстой)")
tg.sambar_haruulah(A, BURTGEL)

# ---------- 7 ----------
heseg("7. asuult_haruulah")
print("  (доор асуулт ба дугаарласан 4 сонголт байх ёстой)")
tg.asuult_haruulah(A[0])

# ---------- 8 ----------
heseg("8. hariult_shalgah")
shalga("зөв хариулт", tg.hariult_shalgah(A[0], 2), True)
shalga("буруу хариулт", tg.hariult_shalgah(A[0], 1), False)

# ---------- 9 ----------
heseg("9. onoo_bodoh")
shalga("хоосон бүртгэл", tg.onoo_bodoh([]), 0)
shalga("нэмэх ба хасах", tg.onoo_bodoh(BURTGEL), -200)
shalga("гурван бичлэг", tg.onoo_bodoh(BURTGEL + [{"sedev": "МАШИН СУРГАЛТ", "une": 100, "zov": True}]), -100)

# ---------- 10 ----------
heseg("10. temdeglel_hadgalah")

with open("test_temdeglel.txt", "w", encoding="utf-8") as f:
    f.write("")

fail = tg.temdeglel_hadgalah(BURTGEL, "test_temdeglel.txt")
shalga("файлын нэрийг буцаасан", fail, "test_temdeglel.txt")

aguulga = open("test_temdeglel.txt", encoding="utf-8").read().strip()
if aguulga == "":
    print("  АЛДАА   файл хоосон, temdeglel_hadgalah юу ч бичсэнгүй")
    niit = niit + 3
else:
    moruud = aguulga.split("\n")
    shalga("гурван мөр", len(moruud), 3)
    shalga("эхний мөр", moruud[0].strip(), "PYTHON ҮНДЭС,100,+")
    shalga("сүүлийн мөр", moruud[-1].strip(), "NIIT,-200")

# ---------- дүн ----------
print()
print("=========================================")
print("  ДҮН:", dun, "/", niit)
if dun == niit:
    print("  Бүгд зөв. Ажиллуул:  python togloom.py")
else:
    print("  Дуусаагүй функц байна. Дээрх АЛДАА мөрүүдийг хар.")
print("=========================================")

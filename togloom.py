# =====================================================
#  ОЮУНЫ ТОГЛООМ (Jeopardy!)
#  Сэдэв: ХИЙМЭЛ ОЮУН БА PYTHON
#  "Coffee Shop System" даалгаврын аналог - Хичээл 3
# =====================================================
#
#  Кофе шопоос юугаараа ялгаатай вэ:
#    өгөгдөл ХОЁР шатлалтай - эхлээд сэдэв, сэдвийн дотор үнэ.
#    Сонголт дээрээс доош явна: сэдэв -> үнэ -> асуулт -> хариултын дугаар.
#
#  Тоглолтын дараалал:
#    тоглогч нэрээ оруулна -> 5 асуултад хариулна (сэдэв, үнээ өөрөө сонгоно)
#    -> шинэ тоглогч бүртгүүлэх эсвэл тоглоом дуусгах
#    -> төгсгөлд бүх тоглогчийн оноог бодож, дүнгийн хүснэгт гаргана.
#
#  Ашиглах зүйлс: жагсаалт, dictionary, for, if, while, open, функц
#  Ашиглахгүй зүйлс: import, class, try/except, list comprehension
#
#  Шалгах:           python shalgalt.py
#  Тоглоом эхлүүлэх:  python togloom.py
# =====================================================


FAIL = "asuultuud.txt"
TEMDEGLEL_FAIL = "temdeglel.txt"
ASUULT_TOO = 5          # нэг тоглогч хэдэн асуултад хариулах вэ


# -----------------------------------------------------
#  ИНТЕРФЕЙСИЙН БҮХ ТЕКСТ НЭГ Л DICTIONARY дотор байна.
#  Тоглоомыг өөр хэл рүү хөрвүүлэхийн тулд зөвхөн энэ
#  dictionary-г солино, кодын нэг ч мөрийг хөдөлгөх шаардлагагүй.
# -----------------------------------------------------

TEKST = {
    "garchig": "=====  ОЮУНЫ ТОГЛООМ: AI ба PYTHON  =====",
    "ner_oruulah": "Тоглогчийн нэр: ",
    "ner_hooson": "Нэрээ оруулна уу.",
    "ner_davhardsan": "Ийм нэртэй тоглогч бүртгэлтэй байна. Өөр нэр оруулна уу.",
    "eelj": "Ээлж: ",
    "asuult_dugaar": "Асуулт ",
    "eelj_duussan": "Ээлж дууслаа. Оноо: ",
    "menu_shine": "1 - Шинэ тоглогч бүртгүүлэх",
    "menu_duusgah": "0 - Тоглоом дуусгах",
    "songoh": "Таны сонголт: ",
    "dun_garchig": "=====  ТОГЛООМЫН ДҮН  =====",
    "dun_tolgoi": "№   Нэр                 Зөв   Оноо",
    "yalagch": "Ялагч: ",
    "songolt_baihgui": "Ийм дугаартай сонголт алга.",
    "sedev_dugaar": "Сэдвийн дугаар: ",
    "asuult_une": "Асуултын үнэ: ",
    "bolomjtoi": "Боломжтой үнэ: ",
    "tanii_hariult": "Таны хариулт (сонголтын дугаар): ",
    "zov": "ЗӨВ! Нэмэгдэх оноо:",
    "buruu": "Буруу. Хасагдах оноо:",
    "zov_hariult": "Зөв хариулт: ",
    "onoo": "Оноо: ",
    "onoo_ug": "оноо",
    "sedev_baihgui": "Ийм сэдэв алга.",
    "une_baihgui": "Энэ сэдэвт ийм үнэ алга.",
    "toglogdson": "Энэ асуулт аль хэдийн тоглогдсон. Өөрийг сонгоно уу.",
    "zovhon_too": "Зөвхөн тоо оруулна уу.",
    "temdeglel_hadgalagdsan": "Тэмдэглэл хадгалагдлаа: ",
    "asuult_unshigdaagui": "Асуулт уншигдсангүй. asuult_unshih функцээ шалгана уу.",
    "bayartai": "Дараа уулзая!",
    "zai": " - ",
    "buruu_songolt": "Цэсний буруу сонголт.",
}


# -----------------------------------------------------
# 1. asuult_unshih(fail)
# -----------------------------------------------------
# Файлын нэг мөр иймэрхүү харагдана:
#     PYTHON ҮНДЭС|100|Python хэлийг хэн зохиосон бэ?|А;Б;В;Г|2
#     сэдэв | үнэ | асуулт | сонголтууд ; тэмдэгээр | зөв хариултын дугаар
#
# Мөр бүрийг dictionary болгоод бүгдийг нь жагсаалтад хийнэ.
#
# Буцаана:
#   [{"sedev": "PYTHON ҮНДЭС", "une": 100, "asuult": "...",
#     "songolt": ["А", "Б", "В", "Г"], "zov": 2}, ...]

def asuult_unshih(fail):
    asuultuud = []
    with open(fail, encoding="utf-8") as f:
        for mor in f:
            mor = mor.strip()
            if mor == "":
                continue
            heseg = mor.split("|")
            asuult = {
                "sedev": heseg[0],
                "une": int(heseg[1]),
                "asuult": heseg[2],
                "songolt": heseg[3].split(";"),
                "zov": int(heseg[4]),
            }
            asuultuud.append(asuult)
    return asuultuud


# -----------------------------------------------------
# 2. sedev_jagsaalt(asuultuud)  -  НЭГДҮГЭЭР ШАТЛАЛ
# -----------------------------------------------------
# Давхардаагүй сэдвүүдийн жагсаалт, файлд байгаа дарааллаараа.
#
#   sedev_jagsaalt(asuultuud) -> ["PYTHON ҮНДЭС", "МАШИН СУРГАЛТ", ...]

def sedev_jagsaalt(asuultuud):
    sedevuud = []
    for asuult in asuultuud:
        if asuult["sedev"] not in sedevuud:
            sedevuud.append(asuult["sedev"])
    return sedevuud


# -----------------------------------------------------
# 3. sedev_une(asuultuud, sedev)  -  ХОЁРДУГААР ШАТЛАЛ
# -----------------------------------------------------
# Нэг сэдвийн доторх бүх үнэ.
#
#   sedev_une(asuultuud, "PYTHON ҮНДЭС") -> [100, 200, 300, 400, 500]
#   sedev_une(asuultuud, "ХӨГЖИМ") -> []

def sedev_une(asuultuud, sedev):
    unenuud = []
    for asuult in asuultuud:
        if asuult["sedev"] == sedev:
            unenuud.append(asuult["une"])
    return unenuud


# -----------------------------------------------------
# 4. asuult_haih(asuultuud, sedev, une)
# -----------------------------------------------------
# ХОЁР түлхүүрээр нэг дор хайна: сэдэв ба үнэ.
# Олдвол dictionary-г нь буцаана, олдохгүй бол None.

def asuult_haih(asuultuud, sedev, une):
    for asuult in asuultuud:
        if asuult["sedev"] == sedev and asuult["une"] == une:
            return asuult
    return None


# -----------------------------------------------------
# 5. toglson(burtgel, sedev, une)
# -----------------------------------------------------
# Энэ асуулт аль хэдийн тоглогдсон эсэх. True / False.
#
# Бүртгэл гэдэг нь иймэрхүү бичлэгүүдийн жагсаалт:
#   {"sedev": "PYTHON ҮНДЭС", "une": 100, "zov": True}

def toglson(burtgel, sedev, une):
    for bichleg in burtgel:
        if bichleg["sedev"] == sedev and bichleg["une"] == une:
            return True
    return False


# -----------------------------------------------------
# 6. sambar_haruulah(asuultuud, burtgel)
# -----------------------------------------------------
# Тоглоомын самбарыг хэвлэнэ. Тоглогдсон нүд зурааснаар хаагдана.
#
#   1. PYTHON ҮНДЭС        ---   200   300   400   500
#   2. МАШИН СУРГАЛТ       100   200   ---   400   500

def sambar_haruulah(asuultuud, burtgel):
    sedevuud = sedev_jagsaalt(asuultuud)
    dugaar = 1
    for sedev in sedevuud:
        mor = str(dugaar) + ". " + sedev.ljust(18)
        for une in sedev_une(asuultuud, sedev):
            if toglson(burtgel, sedev, une):
                mor = mor + "   ---"
            else:
                mor = mor + "   " + str(une).rjust(3)
        print(mor)
        dugaar = dugaar + 1


# -----------------------------------------------------
# 7. asuult_haruulah(asuult)
# -----------------------------------------------------
# Асуулт болон дугаарласан сонголтуудыг хэвлэнэ. Юу ч буцаахгүй.

def asuult_haruulah(asuult):
    print()
    print(asuult["sedev"] + TEKST["zai"] + str(asuult["une"]))
    print(asuult["asuult"])
    dugaar = 1
    for songolt in asuult["songolt"]:
        print("   " + str(dugaar) + ") " + songolt)
        dugaar = dugaar + 1


# -----------------------------------------------------
# 8. hariult_shalgah(asuult, dugaar)
# -----------------------------------------------------
# Тоглогч зөв дугаар сонгосон эсэх. True / False.

def hariult_shalgah(asuult, dugaar):
    if dugaar == asuult["zov"]:
        return True
    return False


# -----------------------------------------------------
# 9. onoo_bodoh(burtgel)
# -----------------------------------------------------
# Jeopardy-н дүрмээр оноо бодно: зөв хариулт үнийг нэмнэ,
# буруу хариулт үнийг хасна.

def onoo_bodoh(burtgel):
    onoo = 0
    for bichleg in burtgel:
        if bichleg["zov"]:
            onoo = onoo + bichleg["une"]
        else:
            onoo = onoo - bichleg["une"]
    return onoo


# -----------------------------------------------------
# 10. temdeglel_hadgalah(burtgel, fail)
# -----------------------------------------------------
# Тоглоомын явцыг файлд бичээд файлын нэрийг буцаана.
#
# Файлын агуулга:
#   PYTHON ҮНДЭС,100,+
#   МАШИН СУРГАЛТ,300,-
#   NIIT,-200

def temdeglel_hadgalah(burtgel, fail):
    with open(fail, "w", encoding="utf-8") as f:
        for bichleg in burtgel:
            if bichleg["zov"]:
                temdeg = "+"
            else:
                temdeg = "-"
            f.write(bichleg["sedev"] + "," + str(bichleg["une"]) + "," + temdeg + "\n")
        f.write("NIIT," + str(onoo_bodoh(burtgel)) + "\n")
    return fail


# -----------------------------------------------------
# 11. zov_too(burtgel)
# -----------------------------------------------------
# Хэдэн асуултад зөв хариулсныг тоолно.

def zov_too(burtgel):
    too = 0
    for bichleg in burtgel:
        if bichleg["zov"]:
            too = too + 1
    return too


# -----------------------------------------------------
# 12. ner_burtgeltei(toglogchid, ner)
# -----------------------------------------------------
# Ийм нэртэй тоглогч аль хэдийн байгаа эсэх. True / False.
#
# Тоглогч гэдэг нь иймэрхүү dictionary:
#   {"ner": "Бат", "burtgel": [{"sedev": ..., "une": ..., "zov": ...}, ...]}

def ner_burtgeltei(toglogchid, ner):
    for toglogch in toglogchid:
        if toglogch["ner"] == ner:
            return True
    return False


# -----------------------------------------------------
# 13. eremblel(toglogchid)
# -----------------------------------------------------
# Тоглогчдыг оноогоор нь ихээс бага руу эрэмбэлсэн ШИНЭ жагсаалт.
# Үлдсэн тоглогчдоос хамгийн их оноотойг нь олж шинэ жагсаалт руу зөөнө.

def eremblel(toglogchid):
    uldsen = []
    for toglogch in toglogchid:
        uldsen.append(toglogch)

    erembe = []
    while uldsen:
        hamgiin = uldsen[0]
        for toglogch in uldsen:
            if onoo_bodoh(toglogch["burtgel"]) > onoo_bodoh(hamgiin["burtgel"]):
                hamgiin = toglogch
        erembe.append(hamgiin)
        uldsen.remove(hamgiin)
    return erembe


# -----------------------------------------------------
# 14. dun_haruulah(toglogchid)
# -----------------------------------------------------
# Тоглоомын эцсийн дүнгийн хүснэгт ба ялагчийг хэвлэнэ.
#
#   №   Нэр                 Зөв   Оноо
#   1   Бат                   4    900
#   2   Дорж                  2   -100
#   Ялагч: Бат (900 оноо)

def dun_haruulah(toglogchid):
    erembe = eremblel(toglogchid)
    print()
    print(TEKST["dun_garchig"])
    print(TEKST["dun_tolgoi"])
    dugaar = 1
    for toglogch in erembe:
        mor = str(dugaar).ljust(4) + toglogch["ner"].ljust(20)
        mor = mor + str(zov_too(toglogch["burtgel"])).rjust(3)
        mor = mor + str(onoo_bodoh(toglogch["burtgel"])).rjust(7)
        print(mor)
        dugaar = dugaar + 1

    # Тэнцсэн бол хэд хэдэн ялагч байж болно
    deed_onoo = onoo_bodoh(erembe[0]["burtgel"])
    yalagchid = ""
    for toglogch in erembe:
        if onoo_bodoh(toglogch["burtgel"]) == deed_onoo:
            if yalagchid != "":
                yalagchid = yalagchid + ", "
            yalagchid = yalagchid + toglogch["ner"]
    print(TEKST["yalagch"] + yalagchid + " (" + str(deed_onoo) + " " + TEKST["onoo_ug"] + ")")


# -----------------------------------------------------
# 15. toglogchid_hadgalah(toglogchid, fail)
# -----------------------------------------------------
# Бүх тоглогчийн тэмдэглэлийг нэг файлд бичээд файлын нэрийг буцаана.
#
# Файлын агуулга:
#   TOGLOGCH,Бат
#   PYTHON ҮНДЭС,100,+
#   МАШИН СУРГАЛТ,300,-
#   NIIT,-200
#   TOGLOGCH,Дорж
#   ...

def toglogchid_hadgalah(toglogchid, fail):
    with open(fail, "w", encoding="utf-8") as f:
        for toglogch in toglogchid:
            f.write("TOGLOGCH," + toglogch["ner"] + "\n")
            for bichleg in toglogch["burtgel"]:
                if bichleg["zov"]:
                    temdeg = "+"
                else:
                    temdeg = "-"
                f.write(bichleg["sedev"] + "," + str(bichleg["une"]) + "," + temdeg + "\n")
            f.write("NIIT," + str(onoo_bodoh(toglogch["burtgel"])) + "\n")
    return fail


# =====================================================
#  НЭГ ТОГЛОГЧИЙН ЭЭЛЖ. Энд сонголтын бүх шатлал нийлнэ:
#  сэдэв -> үнэ -> асуулт -> хариултын дугаар.
#  Тоглогч ASUULT_TOO асуултад хариулмагц ээлж дуусна.
# =====================================================

def toglogchiin_eelj(asuultuud, ner):
    burtgel = []
    niit_asuult = ASUULT_TOO
    if len(asuultuud) < niit_asuult:
        niit_asuult = len(asuultuud)

    print()
    print(TEKST["eelj"] + ner)

    while len(burtgel) < niit_asuult:
        print()
        print(TEKST["asuult_dugaar"] + str(len(burtgel) + 1) + "/" + str(niit_asuult)
              + "   " + TEKST["onoo"] + str(onoo_bodoh(burtgel)))
        sambar_haruulah(asuultuud, burtgel)
        sedevuud = sedev_jagsaalt(asuultuud)

        # 1-р шат: сэдэв
        oruulga = input(TEKST["sedev_dugaar"]).strip()
        if not oruulga.isdigit():
            print(TEKST["zovhon_too"])
            continue
        sedev_dugaar = int(oruulga)
        if sedev_dugaar < 1 or sedev_dugaar > len(sedevuud):
            print(TEKST["sedev_baihgui"])
            continue
        sedev = sedevuud[sedev_dugaar - 1]

        # 2-р шат: үнэ (тоглогч өөрөө сонгоно)
        unenuud = sedev_une(asuultuud, sedev)
        mor = ""
        for une in unenuud:
            if not toglson(burtgel, sedev, une):
                mor = mor + str(une) + " "
        if mor == "":
            print(TEKST["toglogdson"])
            continue
        print(TEKST["bolomjtoi"] + mor)

        oruulga = input(TEKST["asuult_une"]).strip()
        if not oruulga.isdigit():
            print(TEKST["zovhon_too"])
            continue
        une = int(oruulga)
        if une not in unenuud:
            print(TEKST["une_baihgui"])
            continue
        if toglson(burtgel, sedev, une):
            print(TEKST["toglogdson"])
            continue

        # 3-р шат: асуулт өөрөө
        asuult = asuult_haih(asuultuud, sedev, une)
        if asuult is None:
            print(TEKST["une_baihgui"])
            continue
        asuult_haruulah(asuult)

        # 4-р шат: хариултын дугаар.
        # Асуултыг харсан тул зөв дугаар оруултал дахин асууна,
        # өөр асуулт руу шилжих боломжгүй.
        hariult_dugaar = 0
        while hariult_dugaar == 0:
            oruulga = input(TEKST["tanii_hariult"]).strip()
            if not oruulga.isdigit():
                print(TEKST["zovhon_too"])
            elif int(oruulga) < 1 or int(oruulga) > len(asuult["songolt"]):
                print(TEKST["songolt_baihgui"])
            else:
                hariult_dugaar = int(oruulga)

        if hariult_shalgah(asuult, hariult_dugaar):
            print(TEKST["zov"], une)
            burtgel.append({"sedev": sedev, "une": une, "zov": True})
        else:
            print(TEKST["buruu"], une)
            print(TEKST["zov_hariult"] + asuult["songolt"][asuult["zov"] - 1])
            burtgel.append({"sedev": sedev, "une": une, "zov": False})

    print()
    print(ner + TEKST["zai"] + TEKST["eelj_duussan"] + str(onoo_bodoh(burtgel)))
    return burtgel


# =====================================================
#  ТОГЛООМ. Нэр оруулах -> ээлж -> шинэ тоглогч эсвэл дуусгах -> дүн.
# =====================================================

def toglooh():
    asuultuud = asuult_unshih(FAIL)

    if not asuultuud:
        print(TEKST["asuult_unshigdaagui"])
        return

    toglogchid = []

    while True:
        print()
        print(TEKST["garchig"])

        # ---------- тоглогч бүртгүүлэх ----------
        ner = input(TEKST["ner_oruulah"]).strip()
        if ner == "":
            print(TEKST["ner_hooson"])
            continue
        if ner_burtgeltei(toglogchid, ner):
            print(TEKST["ner_davhardsan"])
            continue

        # ---------- тоглогчийн ээлж ----------
        burtgel = toglogchiin_eelj(asuultuud, ner)
        toglogchid.append({"ner": ner, "burtgel": burtgel})

        # ---------- шинэ тоглогч эсвэл дуусгах ----------
        songolt = ""
        while songolt != "1" and songolt != "0":
            print()
            print(TEKST["menu_shine"])
            print(TEKST["menu_duusgah"])
            songolt = input(TEKST["songoh"]).strip()
            if songolt != "1" and songolt != "0":
                print(TEKST["buruu_songolt"])

        if songolt == "0":
            break

    # ---------- эцсийн дүн ----------
    dun_haruulah(toglogchid)
    fail = toglogchid_hadgalah(toglogchid, TEMDEGLEL_FAIL)
    print(TEKST["temdeglel_hadgalagdsan"] + fail)
    print(TEKST["bayartai"])


if __name__ == "__main__":
    toglooh()
    
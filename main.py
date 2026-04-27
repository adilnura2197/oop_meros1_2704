#16
class Dars:
    def __init__(self, nomi):
        self.nomi = nomi

    def oqish(self):
        print("dars o'tilmoqda", end=" ")

class InglizTili(Dars):
    def oqish(self):
        super().oqish()
        print(", Ingliz tili darsi")


d1 = Dars("Algebra")
i1 = InglizTili("Ingliz tili")

d1.oqish()
i1.oqish()


#17
class Bank:
    def __init__(self, nomi):
        self.nomi = nomi

    def xizmat(self):
        print("Xizmat ko'rsatilmoqda", end=" ")

class Onlaynbank(Bank):
    def xizmat(self):
        super().xizmat()
        print(", Onlayn xizmat")


b1 = Bank("Xalq banki")
o1 = Onlaynbank("Agro bank")

b1.xizmat()
o1.xizmat()

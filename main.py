import json


class Gramata:
    def __init__(self, nosaukums, autors, gads):
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads
        self.ir_aiznemta = False

    def __str__(self):
        statuss = "Aizņemta" if self.ir_aiznemta else "Pieejama"
        return f"{self.nosaukums} ({self.autors}, {self.gads}) – {statuss}"


class Biblioteka:
    def __init__(self):
        self.gramatas = []

    def pievienot_gramatu(self, gramata):
        self.gramatas.append(gramata)
        print(f" Grāmata '{gramata.nosaukums}' pievienota bibliotēkai!")

    def paradit_gramatas(self):
        if not self.gramatas:
            print("Bibliotēkā vēl nav grāmatu.")
        else:
            print("\n=== BIBLIOTĒKAS GRĀMATAS ===")
            for i, g in enumerate(self.gramatas, 1):
                print(f"{i}. {g}")

    def meklēt_gramatu(self, nosaukums):
        atrastas = [g for g in self.gramatas if nosaukums.lower() in g.nosaukums.lower()]
        if not atrastas:
            print(" Grāmata netika atrasta.")
        else:
            print("\n Atrastās grāmatas:")
            for g in atrastas:
                print(g)

    def dzest_gramatu(self, nosaukums):
        for g in self.gramatas:
            if g.nosaukums.lower() == nosaukums.lower():
                self.gramatas.remove(g)
                print(f"🗑️ Grāmata '{nosaukums}' dzēsta.")
                return
        print("Grāmata netika atrasta.")

    def statistika(self):
        if not self.gramatas:
            print("Nav datu statistikai.")
            return
        vid_gads = sum(int(g.gads) for g in self.gramatas) / len(self.gramatas)
        jaunaka = max(self.gramatas, key=lambda g: g.gads)
        vecaka = min(self.gramatas, key=lambda g: g.gads)
        print("\n=== STATISTIKA ===")
        print(f" Kopā grāmatu: {len(self.gramatas)}")
        print(f" Vidējais izdošanas gads: {vid_gads:.1f}")
        print(f" Jaunākā grāmata: {jaunaka.nosaukums} ({jaunaka.gads})")
        print(f" Vecākā grāmata: {vecaka.nosaukums} ({vecaka.gads})")


    def saglabat_faila(self, faila_nosaukums="biblioteka.json"):
        dati = [g.__dict__ for g in self.gramatas]
        with open(faila_nosaukums, "w", encoding="utf-8") as f:
            json.dump(dati, f, ensure_ascii=False, indent=4)
        print("Dati saglabāti failā!")

    def nolasit_no_faila(self, faila_nosaukums="biblioteka.json"):
        try:
            with open(faila_nosaukums, "r", encoding="utf-8") as f:
                dati = json.load(f)
                self.gramatas = [Gramata(**g) for g in dati]
            print("Dati nolasīti no faila!")
        except FileNotFoundError:
            print("Failu neizdevās atrast – sākam ar tukšu bibliotēku.")



    def galvena_izvelne(self):
        biblioteka = Biblioteka()
        biblioteka.nolasit_no_faila()

        while True:
            print("\n===== BIBLIOTĒKAS SISTĒMA =====")
            print("1. Pievienot grāmatu")
            print("2. Parādīt visas grāmatas")
            print("3. Meklēt grāmatu")
            print("4. Dzēst grāmatu")
            print("5. Parādīt statistiku")
            print("6. Saglabāt datus")
            print("0. Iziet")
            izvēle = input("Izvēlies darbību: ")

            if izvēle == "1":
                nosaukums = input("Grāmatas nosaukums: ")
                autors = input("Autors: ")
                gads = input("Izdošanas gads: ")
                biblioteka.pievienot_gramatu(Gramata(nosaukums, autors, gads))
            elif izvēle == "2":
                biblioteka.paradit_gramatas()
            elif izvēle == "3":
                nosaukums = input("Ievadi meklējamo nosaukumu: ")
                biblioteka.meklēt_gramatu(nosaukums)
            elif izvēle == "4":
                nosaukums = input("Ievadi dzēšamās grāmatas nosaukumu: ")
                biblioteka.dzest_gramatu(nosaukums)
            elif izvēle == "5":
                biblioteka.statistika()
            elif izvēle == "6":
                biblioteka.saglabat_faila()
            elif izvēle == "0":
                biblioteka.saglabat_faila()
                print("Programma beidza darbu.")
                break
            else:
                print(" Nepareiza izvēle. Mēģini vēlreiz.")

if __name__ == "__main__":
    biblioteka = Biblioteka()
    biblioteka.galvena_izvelne()
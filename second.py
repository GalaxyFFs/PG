
def cislo_text(cislo):

    jednotky = ("nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět")

    teen = ("deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct")

    desitky = ("", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát", "sto")

    cislo = int(cislo)

    if cislo > 100:
        return "Číslo je mimo rozsah."

    elif cislo <= 9:
        return jednotky[cislo]

    elif 10 <= cislo <= 19:
        cislo %= 10
        return teen[cislo]

    else:
        destitka = cislo // 10
        jednotka = cislo % 10

        if jednotka == 0:
            return desitky[destitka]
            
        else:
            return desitky[destitka] + " " + jednotky[jednotka]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
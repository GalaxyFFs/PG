def je_tah_mozny_pesec(figurka, cilova_pozice, obsazene_pozice):
    pozice = figurka["pozice"]
    if pozice[0] + 1 == cilova_pozice[0] and pozice[1] == cilova_pozice[1]:
        return True 
    # Dvoupolní první tah: musí být z výchozího řádku (2) a mezilehlé pole musí být volné
    elif pozice[0] == 2 and pozice[0] + 2 == cilova_pozice[0] and pozice[1] == cilova_pozice[1] and (pozice[0] + 1, pozice[1]) not in obsazene_pozice:
        return True
    return False

def je_tah_mozny_jezdec(figurka, cilova_pozice, obsazene_pozice):
    pozice = figurka["pozice"]
    if (pozice[0] + 2 == cilova_pozice[0] or pozice[0] - 2 == cilova_pozice[0]) and (pozice[1] + 1 == cilova_pozice[1] or pozice[1] - 1 == cilova_pozice[1]):
        return True
    elif (pozice[0] + 1 == cilova_pozice[0] or pozice[0] - 1 == cilova_pozice[0]) and (pozice[1] + 2 == cilova_pozice[1] or pozice[1] - 2 == cilova_pozice[1]):
        return True
    return False

def je_tah_mozny_vez(figurka, cilova_pozice, obsazene_pozice):
    pozice = figurka["pozice"]
    if pozice[0] == cilova_pozice[0]:
        # Pohyb horizontálně
        zacatecni_sloupec = min(pozice[1], cilova_pozice[1]) + 1
        konecny_sloupec = max(pozice[1], cilova_pozice[1])
        for sloupec in range(zacatecni_sloupec, konecny_sloupec):
            if (pozice[0], sloupec) in obsazene_pozice:
                return False
        # Pokud jsme nenašli žádnou překážku mezi startem a cílem, tah je možný
        return True
    elif pozice[1] == cilova_pozice[1]:
        # Pohyb svisle
        zacatecni_radek = min(pozice[0], cilova_pozice[0]) + 1
        konecny_radek = max(pozice[0], cilova_pozice[0])
        for radek in range(zacatecni_radek, konecny_radek):
            if (radek, pozice[1]) in obsazene_pozice:
                return False
        return True
    return False

def je_tah_mozny_kral(figurka, cilova_pozice, obsazene_pozice):
    pozice = figurka["pozice"]
    dx = abs(cilova_pozice[0] - pozice[0])
    dy = abs(cilova_pozice[1] - pozice[1])

    # žádný pohyb
    if dx == 0 and dy == 0:
        return False

    # povolen pouze 1 krok v libovolném směru
    if dx <= 1 and dy <= 1:
        return True

    return False

def je_tah_mozny_strelec(figurka, cilova_pozice, obsazene_pozice):
    pozice = figurka["pozice"]
    pohyb_x = 0
    pohyb_y = 0

    if abs(cilova_pozice[0] - pozice[0]) == abs(cilova_pozice[1] - pozice[1]):

        if cilova_pozice[0] > pozice[0]:
            pohyb_x = 1  # Pohyb nahoru
        else:
            pohyb_x = -1  # Pohyb dolů

        if cilova_pozice[1] > pozice[1]:    
            pohyb_y = 1  # Pohyb vpravo
        else:
            pohyb_y = -1  # Pohyb vlevo

        x = pozice[0] + pohyb_x
        y = pozice[1] + pohyb_y

        while (x, y) != cilova_pozice:
            if (x, y) in obsazene_pozice:
                return False
            x += pohyb_x
            y += pohyb_y

        return True

    return False

def je_tah_mozny_dama(figurka, cilova_pozice, obsazene_pozice):
    if je_tah_mozny_vez(figurka, cilova_pozice, obsazene_pozice) == True or je_tah_mozny_strelec(figurka, cilova_pozice, obsazene_pozice) == True:
            return True
    return False


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Je na šachovnici?
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False
    
    # Kontrola pohybu figurgy

    typ = figurka["typ"]

    # Pěšec
    if typ == "pěšec":
        return je_tah_mozny_pesec(figurka, cilova_pozice, obsazene_pozice)
    
    # Jezdec
    elif typ == "jezdec":
        return je_tah_mozny_jezdec(figurka, cilova_pozice, obsazene_pozice)

    # Věž 
    elif typ == "věž":
        return je_tah_mozny_vez(figurka, cilova_pozice, obsazene_pozice)

    # Střelec
    elif typ == "střelec":
        return je_tah_mozny_strelec(figurka, cilova_pozice, obsazene_pozice)

    # Dáma
    elif typ == "dáma":
        return je_tah_mozny_dama(figurka, cilova_pozice, obsazene_pozice)

    # Král
    elif typ == "král":
        return je_tah_mozny_kral(figurka, cilova_pozice, obsazene_pozice)

    # Pokud typ není rozpoznán nebo není povolený tah
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4),}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True


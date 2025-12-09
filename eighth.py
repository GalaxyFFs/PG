def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    binarni_cislo_list = []
    binarni_cislo = str(binarni_cislo)

    for cislo in binarni_cislo:
        binarni_cislo_list.append(int(cislo))

    binarni_cislo_list.reverse()

    vysledek = 0
    for index, cislo in enumerate(binarni_cislo_list):
        vysledek += cislo * (2 ** index)

    return vysledek

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    
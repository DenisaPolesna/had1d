from random import randrange

had = [(0, 0),(1,0),(2,0)] #[x,y]
ovoce =  [(7,0),(2,3),(7,8)]

def zadej_velikost_hraciho_pole():
    """Funkce, ktera nastavi velikost hraciho pole, podle vstupu uzivatele."""
    while True:
        try:
            hraci_pole_vyska = int(input("Zadej vysku hraciho pole (10,30): ")) #uzivatel zada vysku hraciho pole
            hraci_pole_delka = int(input("Zadej delku hraciho pole (10,30): ")) #uzivatel zada delku hraciho pole
            if hraci_pole_delka < 4 or hraci_pole_delka > 30:
                print("Minimalni delka hraciho pole je 10 a max. 30.")
                continue
            if hraci_pole_vyska < 1 or hraci_pole_vyska > 30:
                print("Minimalni vyska hraciho pole je 10 a max. 30.")
                continue
        except ValueError:
            print ("Zadavej pouze cisla, ne znaky!")
        else:
            return hraci_pole_vyska, hraci_pole_delka

def zadej_stranu():
    """Funkce, ktera se zepta uzivatele na kterou stranu, chce hada posunout."""
    while True:
        strana_uzivatel = input("Zadej starnu -v,z,s,j: ") #strana zadana uzivatelem

        if strana_uzivatel != "v" and strana_uzivatel != "z" and strana_uzivatel != "s" and strana_uzivatel != "j": #pokud zada neexistujici stranu, zepta se znovu
            return False
        else:
            return strana_uzivatel


def pohyb(souradnice, svetova_strana, hraci_pole_delka, hraci_pole_vyska, ovoce):
    """Funkce, ktera posune hada ve zvolenem smeru. Pokud bude had narazi na jidlo, zvetsi se o jedna."""

    #nastaveni pro vychodni smer
    if svetova_strana == "v":
        posledni_souradnice = souradnice[-1] #ulozi posledni souradnici hada
        prvni_souradnice = souradnice[0] #ulozi prvni souradnici hada
        x_posledni_souradnice = posledni_souradnice[0] #ulozi x-kovou souradnici posledni souradnice hada


        souradnice.append((x_posledni_souradnice + 1 ,posledni_souradnice[1])) #prida souradnici do hada - zvetsi se o 1
        posledni_po_pridani = souradnice[-1] #ulozi posledni souradnici hada


        if posledni_po_pridani[0] == hraci_pole_delka:
            return False
        else:

            obsahuje_ovoce = ovoce.count(posledni_po_pridani) #spocita zda ovoce obsahuje posledni souradnici hada(hlava) - vrati index

            if obsahuje_ovoce > 0: #pokud obsahuje ovoce stejnou souradnici jako je hlava hada
                index_ovoce = ovoce.index((posledni_po_pridani)) #nalezne index ovoce shodny s hlavou hada
                ovoce.pop(index_ovoce)  #odstrani hledanou polozku ze seznamu ovoce s indexem nalezenym o krok vyse - ovoce zmizi z herniho pole

            if obsahuje_ovoce == 0: #pokud ovoce neobsahuje stejnou souradnici jako je hlava hada
                souradnice.pop(0) #odstrani posledni polozku ze seznamu had - had se pohybuje

    #nastaveni pro jizni smer
    if svetova_strana =="j":
        posledni_souradnice = souradnice[-1] #ulozi posledni souradnici hada
        prvni_souradnice = souradnice[0] #ulozi prvni souradnici hada
        jih_y_posledni_souradnice = posledni_souradnice[1] #ulozi y souradnici posledni souradnice hada


        souradnice.append((posledni_souradnice[0],jih_y_posledni_souradnice + 1)) #prida souradnici do hada - zvetsi se o 1
        posledni_po_pridani = souradnice[-1] #ulozi posledni souradnici hada


        if posledni_po_pridani[1] == hraci_pole_vyska:
            return False
        else:
            obsahuje_ovoce = ovoce.count(posledni_po_pridani) #spocita zda ovoce obsahuje posledni souradnici hada(hlava) - vrati index

            if obsahuje_ovoce > 0:  #pokud obsahuje ovoce stejnou souradnici jako je hlava hada
                index_ovoce = ovoce.index((posledni_po_pridani)) #nalezne index ovoce shodny s hlavou hada
                ovoce.pop(index_ovoce)  #odstrani hledanou polozku ze seznamu ovoce s indexem nalezenym o krok vyse - ovoce zmizi z herniho pole

            if obsahuje_ovoce == 0: #pokud ovoce neobsahuje stejnou souradnici jako je hlava hada
                souradnice.pop(0) #odstrani posledni polozku ze seznamu had - had se pohybuje

    #nastaveni pro severni_smer
    if svetova_strana =="s":
        posledni_souradnice = souradnice[-1] #ulozi posledni souradnici hada
        sever_y_posledni_souradnice = posledni_souradnice[1] #ulozi druhou souradnici posledni souradnice hada

        souradnice.append((posledni_souradnice[0],sever_y_posledni_souradnice - 1))  #prida souradnici do hada - zvetsi se o 1

        posledni_po_pridani = souradnice[-1]  #ulozi posledni souradnici hada


        if posledni_po_pridani[1] < 0:
            return False
        else:

            obsahuje_ovoce = ovoce.count(posledni_po_pridani) #spocita zda ovoce obsahuje posledni souradnici hada(hlava) - vrati index

            if obsahuje_ovoce > 0: #pokud obsahuje ovoce stejnou souradnici jako je hlava hada
                index_ovoce = ovoce.index((posledni_po_pridani)) #nalezne index ovoce shodny s hlavou hada
                ovoce.pop(index_ovoce) #odstrani hledanou polozku ze seznamu ovoce s indexem nalezenym o krok vyse - ovoce zmizi z herniho pole

            if obsahuje_ovoce == 0: #pokud ovoce neobsahuje stejnou souradnici jako je hlava hada
                souradnice.pop(0) #odstrani posledni polozku ze seznamu had - had se pohybuje

    #nastaveni pro zapadni smer
    if svetova_strana =="z":
        posledni_souradnice = souradnice[-1] #ulozi posledni souradnici hada
        zapad_x_posledni_souradnice = posledni_souradnice[0] #ulozi prvni souradnici posledni souradnice hada

        souradnice.append((zapad_x_posledni_souradnice - 1, posledni_souradnice[1])) #prida souradnici do hada - zvetsi se o 1

        posledni_po_pridani = souradnice[-1] #ulozi posledni souradnici hada


        if posledni_po_pridani[0] < 0:
            return False
        else:

            obsahuje_ovoce = ovoce.count(posledni_po_pridani) #spocita zda ovoce obsahuje posledni souradnici hada(hlava) - vrati index

            if obsahuje_ovoce > 0: #pokud obsahuje ovoce stejnou souradnici jako je hlava hada
                index_ovoce = ovoce.index((posledni_po_pridani)) #nalezne index ovoce shodny s hlavou hada
                ovoce.pop(index_ovoce) #odstrani hledanou polozku ze seznamu ovoce s indexem nalezenym o krok vyse - ovoce zmizi z herniho pole

            if obsahuje_ovoce == 0: #pokud ovoce neobsahuje stejnou souradnici jako je hlava hada
                souradnice.pop(0) #odstrani posledni polozku ze seznamu had - had se pohybuje





def mapa_souradnic():
    """Funkce, ktera vytvori matici o zadane velikosti. Vykresli hada a ovoce podle zadanych souradnic. """

    hraci_pole_vyska, hraci_pole_delka = zadej_velikost_hraciho_pole()

    pocet_tahu_uzivatele = 0

    obsahuje_had_hada = 0

    while True:

        strana_uzivatel = zadej_stranu() #vyzve uzivatele k zadani smeru hada


        if strana_uzivatel == False:
            print("Zadej pouze povolene znaky: v, z, s, j!")
            continue
        else:
            if pocet_tahu_uzivatele == 30:
                pocet_tahu_uzivatele = 0
            else:
                pocet_tahu_uzivatele = pocet_tahu_uzivatele + 1


        overeni = pohyb(had,strana_uzivatel, hraci_pole_delka, hraci_pole_vyska, ovoce)

        seznam_radku = [] #seznam radku herniho pole

        if overeni == False:   #overi zda funkce pohyb nevratile False - pokud ano hra se ukonci - had narazil do steny
            print("Konec hry! Had narazil do steny.")
            break


        for i in range(0,hraci_pole_vyska):#pro kazdy radek seznamu proved

            radek = [] #jednotlive radky herniho pole

            for j in range(0,hraci_pole_delka): #vytvori matici slozenou pouze z tecek o zadane velikosti

                radek.append(".")


            for c in had: #vykresli souradnice pro znak X ze seznamu had
                x_c = c[0] #pozice
                y_c = c[1] #cislo radku

                obsahuje_had_hada = had.count((x_c,y_c)) #overi zda nova souradnice hada uz neni obsazena v hadovi - pokud ano hra se ukonci

                if i == y_c: #pokud bude cislo radku odpovidat, hodnote y - potom vlozi znak X na index[x] na danem radku
                    radek.pop(x_c) #smaze danou pozici - jinak by se radek zvysil o jeden znak
                    radek.insert(x_c, "X") #vlozi x na danou pozici

            for d in ovoce: #vykresli ovoce na mape jako ?
                x_d = d[0] #pozice na radku
                y_d = d[1] #cislo radku

                if i == y_d:
                    radek.pop(x_d)
                    radek.insert(x_d, "?")

            seznam_radku.append(radek) #prida radek do seznamu radku

        pocet_jidla_na_radku = False
        celkovy_pocet_jidla = False

        for k in range(0, len(seznam_radku)): #cyklus, ktery kontroluje zda je na kazdem radku jidlo

            if seznam_radku[k].count("?") > 0:
                pocet_jidla_na_radku = True
                celkovy_pocet_jidla = True

        if celkovy_pocet_jidla == False: #pokud neni na hracim poli zadne jilo, prida jidlo na nahodne neobsazene souradnice
            nahodne_souradnice_x = randrange(0, hraci_pole_delka) #vygeneruje nahodnou souradnici x
            nahodne_souradnice_y = randrange(0, hraci_pole_vyska) #vygeneruje nahodnou souradnici y

            je_pozice_obsazena = had.count((nahodne_souradnice_x,nahodne_souradnice_y)) #prohleda seznam hada, zda obsahuje nove vygenerovane ovoce

            if je_pozice_obsazena > 0: #pokud je obsazene, generuj znovu
                continue

            if je_pozice_obsazena == 0: #pokud neni obsazene pridej souradnici
                ovoce.append((nahodne_souradnice_x,nahodne_souradnice_y))

        if pocet_tahu_uzivatele == 30 : #jidlo se generuje kazych 30 tahu
            nahodne_souradnice_x = randrange(0, hraci_pole_delka) #vygeneruje nahodnou souradnici x
            nahodne_souradnice_y = randrange(0, hraci_pole_vyska) #vygeneruje nahodnou souradnici y
            print(nahodne_souradnice_x, nahodne_souradnice_y)

            je_pozice_obsazena = had.count((nahodne_souradnice_x,nahodne_souradnice_y)) #prohleda seznam hada, zda obsahuje nove vygenerovane ovoce

            if je_pozice_obsazena > 0: #pokud je obsazene, generuj znovu
                continue

            if je_pozice_obsazena == 0: #pokud neni obsazene pridej souradnici
                ovoce.append((nahodne_souradnice_x,nahodne_souradnice_y))


        for radek in seznam_radku: #vypise polozky seznamu po radcich s mezerami mezi znaky
            print(" ".join(radek))

        if obsahuje_had_hada ==  2: #pokud had kousne sam sebe, hra se ukonci
            print("Konec hry! Had kousnul sam sebe.")
            break



mapa_souradnic()

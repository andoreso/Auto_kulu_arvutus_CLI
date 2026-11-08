################### Arvu küsimine, kontrollimine ja koma sisestuse korrektuur ###################
def kusi_arv(kusimus):
    while True:
        try:
            sisend = input(kusimus).strip().replace(",", ".")
            arv = float(sisend)

            if arv < 0:
                print("Arv ei tohi olla negatiivne!")
                continue
            return arv
        except ValueError:
            print("Palun sisesta arv, näiteks 65 või 6,5 või 6.5!")

################### Peamenüü ###################
def main():
    auto_andmed = False
    auto_andmed_2 = False
    auto_kalk = False
    while True:
        print("\nAUTO KULUDE KALKULAATOR")
        print("1. Sisesta esimese auto andmed")
        print("2. Sisesta teise auto andmed")
        print("3. Määra aasta läbisõit")
        print("4. Näita autode kulusid")
        print("5. Võrdle autosid")
        print("0. Välju")
        alg = input("Sisesta valik: ").strip()

#################### Auto 1 Andmete sisestamine ###################
        if alg == "1":
            print("Sisesta esimese auto andmed: ")
            auto_nimi = str(input("Auto 1 nimi:"))
            while True:
                energia_liik = str(input("Energia liik (b/d/e):")).strip().lower()
                if energia_liik == "b": 
                    energia_liik = "Bensiin"
                    break 
                elif energia_liik == "d": 
                    energia_liik = "Diisel"
                    break
                elif energia_liik == "e": 
                    energia_liik = "Elekter"
                    break
                else: print("Vale valik :) Sisesta b, d või e")
            tarbimine = kusi_arv("Energia vajadus 100 km-le:")
            energia_hind = kusi_arv("Energia hind: €/l või €/kWh: ")
            liising = kusi_arv("Liising €/kuu: ")
            kindlustus = kusi_arv("Liikluskindlustus €/kuu: ")
            kasko = kusi_arv("Kaskokindlustus €/kuu: " )
            hooldus = kusi_arv("Aasta hooldus €/aasta: ")
            automaks = kusi_arv("Automaks €/aasta: ")
            remondifond = kusi_arv("Remondifond €/aasta: ")
            auto_andmed = True
            auto_kalk = False
################## Auto 2 andmete sisestamine ################

        elif alg == "2":
            print("Sisesta teise auto andmed: ")
            auto_nimi_2 = str(input("Auto 2 nimi:"))
            while True:
                energia_liik_2 = str(input("Energia liik (b/d/e):")).strip().lower()
                if energia_liik_2 == "b": 
                    energia_liik_2 = "Bensiin"
                    break 
                elif energia_liik_2 == "d": 
                    energia_liik_2 = "Diisel"
                    break
                elif energia_liik_2 == "e": 
                    energia_liik_2 = "Elekter"
                    break
                else: print("Vale valik :) Sisesta b, d või e")
            tarbimine_2 = kusi_arv("Keskmine energia kulu 100 km-le:")
            energia_hind_2 = kusi_arv("Energia hind: €/l või €/kWh: ")
            liising_2 = kusi_arv("Liising €/kuu: ")
            kindlustus_2 = kusi_arv("Liikluskindlustus €/kuu: ")
            kasko_2 = kusi_arv("Kaskokindlustus €/kuu: " )
            hooldus_2 = kusi_arv("Aasta hooldus €/aasta: ")
            automaks_2 = kusi_arv("Automaks €/aasta: ")
            remondifond_2 = kusi_arv("Remondifond €/aasta: ")
            auto_andmed_2 = True
            auto_kalk = False
################# Menüü 3 läbisõidu sisestus ja kulude arvestus ###############
        elif alg == "3":
            if not auto_andmed or not auto_andmed_2:
                print("Sisesta enne mõlema auto andmed!")
                continue
            labisoit = int(input("Auto läbisõit aastas: "))
            if labisoit <= 0:
                print("Läbisõit peab olema suurem kui null!")
                continue
################ Kulude kalkuleerimine ###################
            energia_kulu = (labisoit/100)*(tarbimine*energia_hind)
            aasta_kulu = (energia_kulu)+(liising*12)+(kindlustus*12)+(kasko*12)+(hooldus)+(automaks)+(remondifond)
            kuu_energia_kulu = (energia_kulu/12)
            kuu_kulu = (aasta_kulu/12)
            kulu_km = (aasta_kulu/labisoit)
            energia_kulu_2 = (labisoit/100)*(tarbimine_2*energia_hind_2)
            aasta_kulu_2 = (energia_kulu_2)+(liising_2*12)+(kindlustus_2*12)+(kasko_2*12)+(hooldus_2)+(automaks_2)+(remondifond_2)
            kuu_energia_kulu_2 = (energia_kulu_2/12)
            kuu_kulu_2 = (aasta_kulu_2/12)
            kulu_km_2 = (aasta_kulu_2/labisoit)
            auto_kalk =True

################# Menüü 4 Andmed ##########################
        elif alg == "4":
            if not auto_andmed or not auto_andmed_2:
                print("Sisesta enne läbisõit!")
                continue
            print ("\nAutode kulud: ")
            print ("-" * 74)
            print (f"{'Nimi: ':<35} {auto_nimi:>18} {auto_nimi_2:>18}")
            print (f"{'Energia liik':<35} {energia_liik:>18} {energia_liik_2:>18}")
            print (f"{'Keskmine energia kulu kuus':<35} {kuu_energia_kulu:>18.2f} {kuu_energia_kulu_2:>18.2f}")
            print (f"{'Liisingu kulu':<35} {liising:>18} {liising_2:>18}")
            print (f"{'Liikluskindlustus':<35} {kindlustus:>18} {kindlustus_2:>18}")
            print (f"{'Kaskokindlustus':<35} {kasko:>18} {kasko_2:>18}")
            print (f"{'Korraline aastahooldus':<35} {hooldus:>18} {hooldus_2:>18}")
            print (f"{'Automaks aastas':<35} {automaks:>18} {automaks_2:>18}")
            print (f"{'Remondifond':<35} {remondifond:>18} {remondifond_2:>18}")
            print ("-" * 74)
            print (f"{' Kogu kulu aastas':<35} {aasta_kulu:>18.2f} {aasta_kulu_2:>18.2f}" )
            print (f"{' Keskmine kuu kulu':<35} {kuu_kulu:>18.2f} {kuu_kulu_2:>18.2f}")
            print (f"{' Keskmine kilomeeteri kulu':<35} {kulu_km:>18.2f} {kulu_km_2:>18.2f}")

#################### Menüü 5 võrdlus ########################
        elif alg == "5":
            if not auto_kalk:
                print("Sisesta enne läbisõit!")
                continue
            vordsed = ("Võrdsed")
            print ("\nAutode võrdlus: ")
            print ("-" * 87)
            print (f"{'Nimi':<35} {auto_nimi:>18} {auto_nimi_2:>18} {'Soodsam on':>12}")
            print (f"{'Energia liik':<35} {energia_liik:>18} {energia_liik_2:>18}")
            if (kuu_energia_kulu) > (kuu_energia_kulu_2) : soodsam = (auto_nimi_2)
            elif (kuu_energia_kulu) < (kuu_energia_kulu_2) : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Keskmine energia kulu kuus':<35} {kuu_energia_kulu:>18.2f} {kuu_energia_kulu_2:>18.2f} {soodsam:>12}")
            if liising > liising_2 : soodsam = (auto_nimi_2)
            elif liising < liising_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Liisingu kulu':<35} {liising:>18} {liising_2:>18} {soodsam:>12}")
            if kindlustus > kindlustus_2 : soodsam = (auto_nimi_2)
            elif kindlustus < kindlustus_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Liikluskindlustus':<35} {kindlustus:>18} {kindlustus_2:>18} {soodsam:>12}")
            if kasko > kasko_2 : soodsam = (auto_nimi_2)
            elif kasko < kasko_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Kaskokindlustus':<35} {kasko:>18} {kasko_2:>18} {soodsam:>12}")
            if hooldus > hooldus_2 : soodsam = (auto_nimi_2)
            elif hooldus < hooldus_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Korraline aastahooldus':<35} {hooldus:>18} {hooldus_2:>18} {soodsam:>12}")
            if automaks > automaks_2 : soodsam = (auto_nimi_2)
            elif automaks < automaks_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Automaks aastas':<35} {automaks:>18} {automaks_2:>18} {soodsam:>12}")
            if remondifond > remondifond_2 : soodsam = (auto_nimi_2)
            elif remondifond < remondifond_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Remondifond':<35} {remondifond:>18} {remondifond_2:>18} {soodsam:>12}")
            print ("-" * 87)
            if aasta_kulu > aasta_kulu_2 : soodsam = (auto_nimi_2)
            elif aasta_kulu < aasta_kulu_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Kogu kulu aastas':<35} {aasta_kulu:>18.2f} {aasta_kulu_2:>18.2f} {soodsam:>12}" )
            if kuu_kulu > kuu_kulu_2 : soodsam = (auto_nimi_2)
            elif kuu_kulu < kuu_kulu_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Keskmine kuu kulu':<35} {kuu_kulu:>18.2f} {kuu_kulu_2:>18.2f} {soodsam:>12}")
            if kulu_km > kulu_km_2 : soodsam = (auto_nimi_2)
            elif kulu_km < kulu_km_2 : soodsam = (auto_nimi)
            else: soodsam = vordsed
            print (f"{'Keskmine kilomeeteri kulu':<35} {kulu_km:>18.2f} {kulu_km_2:>18.2f} {soodsam:>12}")
     
################### Programmi lõpetamine  ###############
        elif alg == "0":
            print ("Programm lõpetatud.")
            break
        else:
            print("Vigane valik! Sisesta number 0–6.")

if __name__ == "__main__":
    main()   
import random

points_goal = int(input("\nZadej počet bodů, kterého se budeš snažit dosáhnout: "))
cont_end = ""
turns_count = 0
celkove_body = 0
body_min = int(input("Urči si minimální počet bodů za kolo: "))

## Průběh hry
while celkove_body < points_goal:
    print(f"\nMáš celkem {celkove_body} bodů.")
    pocet_kostek = 6
    ## Průběh kola
    body_kola = 0
    turns_count += 1
    while not cont_end:
        ## Průběh hodu
        print(f"Za toto kolo máš zatím {body_kola} bodů.")
        hod = [random.randint(1,6) for _ in range(pocet_kostek)] # generuje hod kostkami
        while True:
            print("Tvůj hod:",hod)
            vybrat = input("Vyber kostky, které chceš odebrat ze hry. Napiš jejich pořadí, odděluj čárkou: ").split(",")
            body_vyberu = 0
            if vybrat == [""]:
                print("Nevybral jsi žádné kostky. Tvoje kolo končí a žádné body se ti nepřičítají.")
                cont_end = "no points"
                body_kola = 0
                break
            vybrane_kostky = []
            for kostka in vybrat:
                vybrane_kostky.append(hod[int(kostka)-1])
            vybrane_kostky.sort()
            nezhodnocene_kostky = vybrane_kostky.copy()
            if nezhodnocene_kostky == [1,2,3,4,5,6]:
                body_vyberu = 1500
                nezhodnocene_kostky = []
            else:
                for i in range(1,7):
                    if vybrane_kostky.count(i) >= 3:
                        body_vyberu += (vybrane_kostky.count(i)-2)*(1000,200,300,400,500,600)[i-1]
                        while i in nezhodnocene_kostky:
                            nezhodnocene_kostky.remove(i)
                while 1 in nezhodnocene_kostky:
                    body_vyberu += 100
                    nezhodnocene_kostky.remove(1)
                while 5 in nezhodnocene_kostky:
                    body_vyberu += 50
                    nezhodnocene_kostky.remove(5)
            if not nezhodnocene_kostky:
                print(f"Za tyto kostky dostaneš {body_vyberu} bodů.")
                print(f"Při ukončení hodu bys tak měl {body_kola+body_vyberu} bodů.")
                print(f"Kdybys ukončil toto kolo, měl bys {body_kola+body_vyberu+celkove_body} bodů.")
                while not cont_end in {"1","2","3"}:
                    cont_end = input("Chceš výběr potvrdit a 1) Pokračovat dalším hodem, 2) Ukončit kolo a přičíst si body, 3) Zrušit výběr a vybrat znovu: ")
                if cont_end == "3":
                    cont_end = ""
                else:
                    body_kola += body_vyberu
                    pocet_kostek -= len(vybrane_kostky)
                    if pocet_kostek <= 0:
                        pocet_kostek = 6
                    break
            else:
                print("Tyto kostky nemůžeš vybrat.")
        if cont_end == "1":
            cont_end = ""
    if body_kola < body_min:
        body_kola = 0
    celkove_body += body_kola
    print(f"Momentálně máš {celkove_body} bodů.")
    cont_end = ""
print("Vyhrál jsi!","\nZvládl jsi naplnit cíl za",turns_count,"kol.")
input()


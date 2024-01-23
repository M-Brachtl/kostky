import random

player_stats = dict()
with open("player_stats.txt","r") as stat_file:
    player_stats = {
        "highest_global": int(stat_file.readline().removesuffix('\n')),
        "game_highest": 0,
        "average_global": int(stat_file.readline().removesuffix('\n')),
        "average_turn": 0,
        "global_turns_num": int(stat_file.readline().removesuffix('\n'))
    }
print(f"\nTvoje maximální rekord: {player_stats['highest_global']} \nTvoje průměrné kolo: {player_stats['game_highest']}")

points_goal = int(input("\nZadej počet bodů, kterého se budeš snažit dosáhnout: "))
cont_end = ""
turns_count = 0
celkove_body = 0
body_min = int(input("Urči si minimální počet bodů za kolo: "))

## Průběh hry
while celkove_body < points_goal or points_goal == 0:
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
            print("\tTvůj hod:",hod)
            vybrat = input("Vyber kostky, které chceš odebrat ze hry. Napiš jejich pořadí, odděluj čárkou: ").split(",")
            body_vyberu = 0
            if vybrat == [""]:
                print("\nNevybral jsi žádné kostky. Tvoje kolo končí a žádné body se ti nepřičítají.")
                cont_end = "no points"
                body_kola = 0
                break
            elif vybrat == ["konec"]:
                exit()
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
                print(f"\nZa tyto kostky dostaneš {body_vyberu} bodů.")
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
    if body_kola > player_stats["game_highest"]: #nejvyšší za hru
        player_stats["game_highest"] = body_kola
    player_stats["average_turn"] = (player_stats["average_turn"]*turns_count + body_kola)/turns_count # výpočet průměru ve hře
    celkove_body += body_kola
    print(f"\nMomentálně máš {celkove_body} bodů.")
    print(f"Tvoje nejvyšší skóre za tuto hru je {player_stats['game_highest']} bodů.")
    print(f"Tvoje průměrné skóre v této hře je {player_stats['average_turn']} bodů.\n")
    cont_end = ""
print("\nVyhrál jsi!","\nZvládl jsi naplnit cíl za",turns_count,"kol.")

## aktualizace statistik
player_stats["highest_global"] = player_stats["game_highest"] if player_stats["game_highest"] > player_stats["highest_global"] else player_stats["highest_global"]
player_stats["global_turns_num"] += turns_count
player_stats["average_global"] = (player_stats["average_turn"]*turns_count + player_stats["average_global"]*(player_stats["global_turns_num"]-turns_count))/player_stats["global_turns_num"]

with open("player_stats.txt","w") as stat_file:
    for key in ("highest_global","average_global","global_turns_num"):
        stat_file.write(str(player_stats[key])+"\n")
##

print("Tvoje současné rekordní kolo:",player_stats["highest_global"])
print("Tvůj současný celkový průměr na kolo:",player_stats["average_global"])

input()


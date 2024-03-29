# Hra Kostky
Verze:
* [Python](#python)
* [Web](#webová-verze)

## Pravidla hry
* Postupka je hodnocena 1500 body
* Kombinace tří stejných čísel je hodnocena 100násobkem čísla kostky
* Při kobinaci čtyř a více stejných čísel 100násobky sčítají s každou další kostkou
* Jedničky nejsou násobeny stovkou, ale tisícovkou
* V ostatních případech má 1 hodnotu 100 a 5 hodnotu 50. Ostatní kostky nemají hodnotu a proto je takto nelze odejmout ze hry
* Při odejmutí všech 6 kostek hráč opět dostává šest kostek
* Pokud se nepodaří vybrat platné kostky v daném hodu, nezískáte za toto kolo žádné body.
Pravidla jsou stejná napříč verzemi

## Python
Tato verze ukládá statistiku vašich her do souboru player_stats.txt. Cílem hry je dosáhnout předem nastaveného skóre.
### Jak hrát
* Zadejte cílové skóre, které chcete dosáhnout. (pro nekonečnou hru zadejte 0)
* Nastavte minimální skóre požadované pro každé kolo.
* Během každého kola hodíte sadu kostek a akumulujete body na základě kombinací, které získáte.
* Zvolte, zda chcete pokračovat v hodu pro další body, nebo ukončit kolo a přidat si aktuální body k celkovému skóre. Také se můžete rozhodnout změnit výběr kostek
* Hra pokračuje, dokud nedosáhnete nebo nepřekročíte cílové skóre.
* **Pokud chcete hru ukončit před řádným skočením hry (u nekonečné hry nutnost), napište při výběru kostek "konec".**
### Ukázka hraní
```
Zadej počet bodů, kterého se budeš snažit dosáhnout: 5000
Urči si minimální počet bodů za kolo: 300

Máš celkem 450 bodů.
Za toto kolo máš zatím 0 bodů.
    Tvůj hod: [2, 4, 1, 3, 1, 5]
Vyber kostky, které chceš odebrat ze hry. Napiš jejich pořadí, odděluj čárkou: 3,5,6
Za tyto kostky dostaneš 250 bodů.
Při ukončení hodu bys tak měl 250 bodů.
Kdybys ukončil toto kolo, měl bys 700 bodů.
```
## Webová verze

Webová verze hry se nacházi ve složce [kostky_js](./kostky_js)
Cílem hry je získat co nejvíce bodů v hráčem nastaveném limitu kol.

### Jak hrát
* Určete si minimální počet bodů za kolo a počet kol (pro nekonečnou hru zadejte 0)
* Kostky, které chcete odebrat ze hry označte kliknutím

### Spuštění
Webovou verzi si můžete vyzkoušet na odkaze [zde](https://m-brachtl.github.io/kostky/kostky_js/)

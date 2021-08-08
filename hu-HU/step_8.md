## Küldd be a munkádat!

Van egy pár olyan szabály, amelynek a kódodnak meg kell felelnie ahhoz, hogy beküldhesd a Nemzetközi Űrállomáson való futtatásra. Ha a kódod betartja őket, akkor a [Sense HAT emulátor](https://trinket.io/mission-zero) alján a szabályok zölddel villannak fel, amikor futtatod a programodat.

![Képernyőkép a Mission Zero Trinket oldalakról, amelyen a beküldő gomb a bal oldalon, a feltételek ellenőrzése a jobb oldalon látható. A felső kettő ("olvasd be a páratartalmat" és "használd a LED-eket") narancssárga színű, az alsó ("hiba nélkül lefut") pedig zöld ](images/validation.png)

1. Mérd meg a páratartalmat!
1. Kapcsold be a LED-eket!
1. Győződj meg arról, hogy a kódod hiba nélkül fut végig! Ne hagyj benn `while True` ciklust a kódodban, mert ettől a kódod a végtelenségig fut és nem fejeződik be.
1. Teszteld a kódodat több különböző páratartalom-beállítással (ehhez mozgasd a csúszkát), hogy megbizonyosodj róla, mindig helyesen fut-e.

Ellenőrizd, hogy ezeknek a feltételeknek is eleget tettél:

1. Ellenőrizd, hogy az űrhajósoknak szóló üzeneted nem hosszabb 30 másodpercnél, mert ennyi ideig fut majd a Nemzetközi Űrállomáson
1. Kerüld el a bevitelt igénylő függvényeket (pl. `input`)
1. Csak a `sense_hat`, `time` és `random` modulokból importálj
1. Semmiképp ne használj káromkodást

Ha minden szabály zöld, készen állsz a beküldésre.

--- task ---

Írd be az osztálytermi kódodat a lenti mezőbe. A tanárod vagy mentorod mondja meg majd a kódod.

**A tanárok és mentorok részére szóló jegyzetek** a [Bevezető](https://projects.raspberrypi.org/hu-HU/projects/astro-pi-mission-zero/1) lépésben találhatók meg.

--- /task ---

--- task ---

Megjelenik a tanárod neve. Ha ez a helyes név, kattints a zöld **Continue to form** (Tovább az űrlaphoz) gombra.

![Tovább az űrlaphoz](images/continue-to-form.png)

--- /task ---

--- task ---

Írd be a csapatod nevét és a csapattagok neveit. Ezek a tanúsítványra is rákerülnek, miután a kódod az űrben futott, úgyhogy ellenőrizd, hogy helyesen írtad őket!

--- /task ---

--- task ---

Nyomd meg a **Submit** (Küldés) gombot a kódod beküldéséhez. A tanárod vagy mentorod egy e-mailt kap majd a jelentkezésedről.

--- /task ---

--- task ---

Ha szerenéd, akár meg is oszthatod a kódodhoz tartozó linket a közösségi oldalakon, hogy elújságold az embereknek, hogy a kód, amit írtál, az űrben fog futni!

--- /task ---

## Skicka ditt bidrag

Det finns några regler som din kod måste följa för att du ska kunna skicka den så att den körs på den internationella rymdstationen. Om din kod följer dem kommer reglerna längst ner i [Sense HAT-emulator](https://trinket.io/mission-zero) att lysa grönt när du kör programmet.

![En skärmdump av Mission Zero Trinket -sidorna som visar inlämningsknappen och kriteriekontrollerna till vänster. De två översta ("läs fuktighet" och "använd lysdioderna") är i orange text, den nedre ("körningar utan fel") är grön ](images/validation.png)

1. Avläs luftfuktigheten.
1. Tänd lysdioderna
1. Kontrollera att din kod körs hela vägen till slutet utan att några fel inträffar. Du bör inte inkludera någon `while True` loopar i din kod eftersom detta kommer förhindra den från att slutföras.
1. Testa din kod med några olika fuktinställningar (med reglaget) för att se till att den alltid kommer att köras korrekt.

Kontrollera även att följande kriterier är uppfyllda:

1. Kontrollera att ditt meddelande till astronauterna inte körs längre än 30 sekunder, eftersom detta är den tid som din kod kommer att köras på ISS
1. Undvik att använda metoder som kräver inmatning
1. Importera bara från modulerna `sense_hat`, `time` och `random`
1. Se till att du inte inkluderar några svordomar

När alla regler är gröna, är du redo att skicka.

--- task ---

Ange din klassrumskod i rutan längst ner – din lärare eller mentor berättar vad din kod är.

**Noteringar för lärare och mentorer** finns i steget [Introduktion](https://projects.raspberrypi.org/sv-SE/projects/astro-pi-mission-zero/1).

--- /task ---

--- task ---

Din lärares namn kommer att visas. Om det är rätt namn, klickar du på den gröna knappen **Continue to form** (Fortsätt till formulär).

![Fortsätt till formulär](images/continue-to-form.png)

--- /task ---

--- task ---

Ange ditt lagnamn och namnen på dina lagmedlemmar. Dessa kommer att skrivas ut på certifikatet när din kod har körts i rymden, så se till att du stavar dem rätt!

--- /task ---

--- task ---

Tryck på **Submit** (Skicka) för att ange din kod. Din lärare eller mentor får ett e-postmeddelande som bekräftar ditt bidrag.

--- /task ---

--- task ---

Om du vill kan du dela länken till din kod på sociala medier för att berätta för folk att koden som du skrev kommer att köras i rymden!

--- /task ---

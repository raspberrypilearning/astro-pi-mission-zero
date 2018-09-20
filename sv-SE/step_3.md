## Visa ett meddelande

--- task ---

Öppna [Sense HAT-emulatorn](https://trinket.io/mission-zero){:target="_blank"} för projektet Mission Zero.

Du kommer att se tre rader kod som har lagts till åt dig automatiskt:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat-emulator](images/sense-hat-emulator2.png)

Den här koden ansluter till Astro Pi och ser till att LED-displayen i Astro PI visas åt rätt håll. Lämna kvar koden där, för du kommer att behöva den.

--- /task ---

--- task ---

Du kanske kan skicka en trevlig hälsning till de astronauter på ISS som arbetar i närheten av Astro Pi? Låt oss rulla meddelandet över displayen.

Lägg till den här raden under de andra kodraderna:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Tryck på knappen **Run** (Kör) och titta när meddelandet `Astro Pi` rullar över LED-displayen.

![visa meddelandekod klicka på kör](images/show-message-code-annotated.PNG)

--- /task ---

![Rullande meddelande](images/scroll-message.gif)

För att visa ett annat meddelande, kan du skriva vad du vill mellan citationstecknen (`""`).

--- collapse ---
---
title: Vilka tecken går att använda?
---
Sense HAT kan bara visa teckenuppsättningen Latin 1, vilket innebär att följande tecken är tillgängliga. Övriga tecken kommer att visas som ett `?`.

    +-*/!"#$><0123456789.=)(
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    abcdefghijklmnopqrstuvwxyz
    
    ?,;:|@%[&_']~
    

--- /collapse ---

--- task ---

Du kan också ändra hastigheten på meddelandet som rullar över skärmen. Lägg till `scroll_speed` på raden i den kod som du redan har skrivit, så här:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Standardhastigheten för meddelandet är `0.1`. Om du väljer ett mindre tal blir meddelandet snabbare och väljer du ett större gör det att meddelandet rullar långsammare.

--- /task ---
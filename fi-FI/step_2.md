## Mikä on Astro Pi?

Astro Pi on Raspberry Pi -tietokone, jonka kotelo on erityisesti suunniteltu avaruusolosuhteisiin. Siinä on myös lisäkortti nimeltä Sense HAT, joka on tehty erityisesti Astro Pi -tehtävää varten. The Sense HAT has a joystick; an LED display; and sensors for recording the lighting conditions, temperature, humidity, pressure, colour, and orientation.

Tässä on alkuperäinen I-mallin Astro Pi -yksikkö Kansainvälisellä avaruusasemalla suorittamassa opiskelijoiden kirjoittamaa koodia. Koodisi tullaan lopulta suorittamaan Astro Pi -tietokoneen uudessa versiossa!


<iframe width="560" height="315" src="https://www.youtube.com/embed/4ykbAJeGPMM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>>

Tätä tehtävää varten tulet käyttämään Sense HAT -emulaattoria. Emulaattori on ohjelma, joka simuloi kaikkia Astro Pi -toimintoja verkkoselaimessasi.
<mark>change screenshot of emulator</mark> ![A labelled screenshot of the Sense HAT emulator with the code window on the left and the emulator on the right.](images/sense-hat-emulator.png)

There are a few differences between the real and the emulated Sense HAT:
<mark>CHeck this is still correct</mark>
- Emulaattorissa voit asettaa lämpötilan, paineen ja kosteuden käyttämällä liukusäätimiä, kun taas Astro Pissä oleva oikea Sense HAT käyttää antureita näiden parametrien mittaamiseen sen ympäristössä.

- Voit hiirellä napsauttaa ja vetää emuloitua Sense HATiä siirtääksesi ja pyörittääksesi sitä ja näin simuloida sen suunnan muutoksia; oikea Astro Pi (ja sen Sense HAT) voi liikkua oikeassa maailmassa, ja Sense HATin suunta-anturit tunnistavat milloin ja miten se on liikkunut.

## Mikä Astro Pi on?

Astro Pi on Raspberry Pi -tietokone, jonka kotelo on erityisesti suunniteltu avaruusolosuhteisiin. Siinä on myös lisäosa nimeltä Sense HAT, joka on tehty nimenomaan Astro Pi -tehtävää varten. Sense HAT -laitteessa on ohjaussauva, LED-näyttö ja anturit lämpötilan, kosteuden, paineen ja suunnan tallentamiseksi.

Tässä on oikea Astro Pi -yksikkö Kansainvälisellä avaruusasemalla, jolla suoritetaan opiskelijoiden kirjoittamaa koodia. Täällä koodisi lopulta suoritetaan! <iframe width="560" height="315" src="https://www.youtube.com/embed/4ykbAJeGPMM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen mark="crwd-mark"></iframe> 

>

For this mission, you will be using the Sense HAT emulator. The emulator is a piece of software which simulates all of the functions of the Astro Pi in your web browser.

![Sense HAT emulator](images/sense-hat-emulator.png)

There are a few differences between the real and the emulated Sense HAT:

- Emulaattorissa voit asettaa lämpötilan, paineen ja kosteuden käyttämällä liukusäätimiä, kun taas Astro Pissä oleva oikea Sense HAT käyttää antureita näiden parametrien mittaamiseen sen ympäristössä.

- Voit hiirellä napsauttaa ja vetää emuloitua Sense HATiä siirtääksesi ja pyörittääksesi sitä ja näin simuloida sen suunnan muutoksia; oikea Astro Pi (ja sen Sense HAT) voi liikkua oikeassa maailmassa, ja Sense HATin suunta-anturit tunnistavat milloin ja miten se on liikkunut.
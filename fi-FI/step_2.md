## Mikä Astro Pi on?

Astro Pi on Raspberry Pi -tietokone, jonka kotelo on erityisesti suunniteltu avaruusolosuhteisiin. Siinä on myös lisäosa nimeltä Sense HAT, joka on tehty nimenomaan Astro Pi -tehtävää varten. Sense HAT -laitteessa on ohjaussauva, LED-näyttö ja anturit lämpötilan, kosteuden, paineen ja suunnan tallentamiseksi.

Tässä on oikea Astro Pi -yksikkö Kansainvälisellä avaruusasemalla, jolla suoritetaan opiskelijoiden kirjoittamaa koodia. Täällä koodisi lopulta suoritetaan! <iframe width="560" height="315" src="https://www.youtube.com/embed/4ykbAJeGPMM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen mark="crwd-mark"></iframe> 

>

Tätä tehtävää varten tulet käyttämään Sense HAT -emulaattoria. Emulaattori on ohjelma, joka simuloi kaikkia Astro Pi -toimintoja verkkoselaimessasi.

![Sense HAT -emulaattori](images/sense-hat-emulator.png)

Oikean ja emuloidun Sense HATin välillä on muutamia eroavaisuuksia:

- Emulaattorissa voit asettaa lämpötilan, paineen ja kosteuden käyttämällä liukusäätimiä, kun taas Astro Pissä oleva oikea Sense HAT käyttää antureita näiden parametrien mittaamiseen sen ympäristössä.

- Voit hiirellä napsauttaa ja vetää emuloitua Sense HATiä siirtääksesi ja pyörittääksesi sitä ja näin simuloida sen suunnan muutoksia; oikea Astro Pi (ja sen Sense HAT) voi liikkua oikeassa maailmassa, ja Sense HATin suunta-anturit tunnistavat milloin ja miten se on liikkunut.
## Mikä Astro Pi on?

Astro Pi on Raspberry Pi -tietokone, jonka kotelo on erityisesti suunniteltu avaruusolosuhteisiin. Siinä on myös lisäosa nimeltä Sense HAT, joka on tehty nimenomaan Astro Pi -missiota varten. Sense HAT -laitteessa on ohjaussauva, LED-näyttö ja anturit lämpötilan, kosteuden, paineen ja suunnan tallentamiseksi.

Tässä on oikea Astro Pi-yksikkö kansainvälisellä avaruusasemalla, jolla suoritetaan opiskelijoiden kirjoittamia koodeja. Täällä koodisi lopulta suoritetaan! <iframe src="https://player.vimeo.com/video/172737314" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen mark="crwd-mark"></iframe> 

Tätä tehtävää varten tulet käyttämään Sense HAT -emulaattoria. Emulaattori on ohjelmisto, joka simuloi kaikkia Astro Pi -toimintoja selaimessasi.

![Sense HAT-emulaattori](images/sense-hat-emulator.png)

Oikean ja emuloidun Sense HAT:n välillä on muutamia eroavaisuuksia:

- Emulaattorissa voit asettaa lämpötilan, paineen ja kosteuden käyttämällä liukusäätimiä, kun taas Astro Pi:ssä reaalinen Sense HAT käyttää antureita näiden parametrien mittaamiseen sen ympäristössä.

- Voit käyttää hiirtä napsauttamalla ja vetämällä emuloidun Sense HATin siirtämään ja pyörittämään sitä, simuloimalla muutoksia sen suuntaan; todellinen Astro Pi (ja sen Sense HAT) voivat liikkua reaalimaailmassa, ja Sense HATin suuntausanturit tunnistavat, milloin ja miten se on liikkunut.
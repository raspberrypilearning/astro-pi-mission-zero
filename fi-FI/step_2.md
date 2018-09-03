## Mikä Astro Pi on?

Astro Pi on Rasberry Pi -tietokone, joka on koteloitu sunniteltuna erityisesti olsuhteisiin avaruudessa. Siinä on myös lisäosa nimeltä Sense HAT, joka on tehty nimenomaan Astro Pi -missiota varten. The Sense HAT käsittää ohjaussauvan, LED-näytön ja antureita lämpötilan, koskeuden, paineen ja sunnan tallentamiseksi.

Tässä on Astro Pi-reaaliyksikkö kansainvälisellä ISS-avaruusasemalla, joka käyttää tiettyjä oiskelijoiden kirjoittamia koodeja. Koodiasi käytetään lopulta tässä! <iframe src="https://player.vimeo.com/video/172737314" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen mark="crwd-mark"></iframe> 

Tätä tehtävää varten tulet käyttämään Sense HAT -emulaattoria. Emulaattori on ohjelmisto, joka simuloi kaikkia Astro Pi -toimintoja selaimessasi.

![Sense HAT-emulaattori](images/sense-hat-emulator.png)

Reaalisen ja emuloidun Sense HATin välillä on muutamia eroavaisuuksia:

- Emulaattorissa voit asettaa lämpötilan, paineen ja kosteuden käyttämällä liukusäätimiä, kun taas Astro Pi:ssä reaalinen Sense HAT käyttää antureita näiden parametrien mittaamiseen sen ympäristössä.

- Voit käyttää hiirtä napsauttamalla ja vetämällä emuloidun Sense HATin siirtämään ja pyörittämään sitä, simuloimalla muutoksia sen suuntaan; todellinen Astro Pi (ja sen Sense HAT) voivat liikkua reaalimaailmassa, ja Sense HATin suuntausanturit tunnistavat, milloin ja miten se on liikkunut.
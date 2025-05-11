# Ohjelmistotekniikan harjoitustyö

**BlockDrop**

*BlockDrop* on peli, jossa tavoitteena on täyttää vaaka ja pystyrivejä ruudukossa. Jokaisesta täyteen saadusta rivistä saa pisteen. Peli päättyy, kun uusia palikoita ei enää mahdu ruudukkoon.


## Dokumentaatio

- [Loppupalautus](https://github.com/juhok00/ot-harjoitustyo/releases/tag/loppupalautus)

- [Käyttöohje](./blockgame/dokumentaatio/kayttoohje.md)
- [Työaikakirjanpito](./blockgame/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](./blockgame/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./blockgame/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./blockgame/dokumentaatio/testaus.md)
- [Changelog](./blockgame/dokumentaatio/changelog.md)


## Asentaminen

1. Asenna poetry:

```
poetry install
```

2. Käynnistä sovellus:
```
poetry run invoke start
```


## Testaus ja testikattavuusraportti

Komento testaukselle:

```
poetry run invoke test
```

Komento testikattavuusraportin luonnille:

```
poetry run invoke coverage-report
```


Komento pylint-tarkistukselle:

```
poetry run invoke lint
```






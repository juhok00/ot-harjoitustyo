# Ohjelmistotekniikan harjoitustyö

**Suunnitelma**

Alustava idea on tehdä *peli*


## Dokumentaatio

- [Työaikakirjanpito](./blockgame/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](./blockgame/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./blockgame/dokumentaatio/arkkitehtuuri.md)
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






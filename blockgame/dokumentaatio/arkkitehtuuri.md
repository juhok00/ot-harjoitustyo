# Arkkitehtuurikuvaus

## Rakenne



![Pakkauskaavio](kuvat/blockdrop_pakkauskaavio.jpg)



## Käyttöliittymä

Käyttöliittymä koostuu toistaiseksi kahdesta näkymästä:

- Aloitusnäkymä, jossa käyttäjä syöttää nimensä.

- Pelinäkymä, jossa peliä pelataan.

- Tulostaulukkonäkymä, jossa näkee tulokset ja voi aloittaa uuden pelin tai vaihtaa pelaajaa.


Kaikki näkymät ovat omissa luokissa ja omissa tiedostoissa "views" kansion sisällä. Käyttöliittymä on selkeästi eriytetty sovelluslogiikasta omilla metodeillaan.


## Sovelluslogiikka

Sovelluksen loogisen titomallin muodostaa GameView, StartView ja LeaderboardView -luokat, nämä vastaavat pelin näkymistä ja toiminnallisuuksista. Siirtyminen näkymien välillä tapahtuu Display luokan kautta main.py:ssä.

```mermaid
classDiagram
    Display --> StartView
    Display --> GameView
    Display --> LeaderboardView
    class Display {
        switch_start_view()
        switch_game_view(player_name)
        switch_leaderboard_view()
        restart_game()
    }
    class StartView {
        draw()
        handle_event(event)
    }
    class GameView {
        draw()
        handle_event(event)
        init_block()
        clear_full_row_or_column()
        check_if_block_can_fit()
    }
    class LeaderboardView {
        draw()
        handle_event(event)
    }
```


## Toiminnallisuuksia


### Nimen syöttö

Kun alussa pelaaja syöttää nimensä ja painaa Enter, niin sovellus etenee pelinäkymään seuraavasti:

```mermaid
sequenceDiagram
  actor Player
  participant StartView
  participant Display
  Player->>StartView: type name and press Enter
  StartView->>Display: switch_game_view(player_name)
  Display->>GameView: initialize game view with player_name
  GameView->>GameView: draw game grid
```


### Blokin sijoittaminen ruudukkoon

Ohessa sekvenssikaaviolla kuvattuna blokin asettaminen peliruudukkoon.

```mermaid
sequenceDiagram
  actor Player
  participant GameView

  Player->>GameView: click and drag block
  GameView->>GameView: update block position
  Player->>GameView: button release
  GameView->>GameView: validate location and lock the block
  GameView->>GameView: draw game view again
```

Kun pelaaja painaa ja raahaa palikkaa, päivittyy palikan sijainti hiiren sijainnin perusteella. Hiiren napin vapauttamisen jälkeen varmistetaan palikan sallittava sijainti ja lukitaan se ruudukkoon.


### Häviäminen

Kun seuraava palikka ei enään mahdu ruudukkoon, niin tapahtuu seuraavasti:

```mermaid
sequenceDiagram
  participant GameView
  participant Display
  GameView->>GameView: check_if_block_can_fit()
  GameView->>Display: switch_leaderboard_view()
  Display->>LeaderboardView: show leaderboard
```

Tarkistetaan siis mahtuuko palikka, jos ei niin edetään pistetaulukkoon.


## Heikkoudet

- Käyttöliittymän koodissa toistuvuutta luokissa, kun mm. piirtäminen on samanlaisia.




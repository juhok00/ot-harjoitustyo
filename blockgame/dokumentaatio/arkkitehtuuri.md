![Pakkauskaavio](kuvat/blockdrop_pakkauskaavio.jpg)



## Toiminnallisuuksia

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
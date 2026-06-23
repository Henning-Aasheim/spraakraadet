# Språkrådet
Dette er bare litt morsom nettskraping? for å øve litt:)

## Ordsky for spørsmål og svar siden til Språkrådet
Dette er ordene som brukes mest i tekstene på Språkrådets spørsmål og svar sider. "Ord", "bruke" og "norsk" er visst de viktigste ordene, noe som for så vidt gir veldig mye mening. Her har jeg fjernet stoppord og kontrollert for lemmatisering,[^1] Dette er gjort med spaCy,[^2] et biblioteket for naturlig språkbehandling, som heldigvis har en "pipeline" for norsk. Jeg tror ikke den fungerer helt på nynorsk, men dette er sikkert noe som kommer.

<p align='center'>
  <img src='/figures/word_cloud.png' width=50%>
  <br>
  <i>Figur 1: Språkrådspørsmåls ordbruk</i>
</p>

## Språk
Dette er et plott som viser hvor mange av artiklene som er skrevet på bokmål og nynorsk. Problemet er at jeg ikke har en god nok måte å skille mellom språkene. Hadde jeg hatt tid hadde det vært mulig å bruke en eksisterende språkmodell (fastText) eller trene en egen modell, kanskje på Wikipedia.

<p align='center'>
  <img src='/figures/articles.png' width=50%>
  <br>
  <i>Figur 1: Språkrådspørsmåls ordbruk</i>
</p>

[^1]: "Lemmatisere er i morfologi og leksikografi å samle bøyingsformer i grupper som høyrer til det same oppslagsordet i ei ordbok — til dømes bok, boka, bøker, bøkene." - Rolf Theil. Store Norske Leksikon (2025). https://snl.no/lemmatisere 
[^2]: https://spacy.io/usage/models

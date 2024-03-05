# Användningsfall Transkribering uppteckningsblankett
# Syfte
Transkribera uppteckningar med enhetlig struktur som försöker följa layouten i en "uppteckningsblankett"

# Mål

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp "uppteckningsblankett"

# Huvudflöde
1. I Vänster panel visa: Inmatningsfält för uppgifter
- Fält i första raden:
  - Berättat av:
  - Född år:
  - Född i:
- Fält som egna rader:
  - Fält under berättat av:
  - Titel:
  - Text:
  - Kommentar till avskriften om inte "sida för sida":
    - Om inte supertranskriberare: till transcription_comment som inte publiceras direkt
    - Om supertranskriberare: till comment som publiceras direkt
  - Kommentar till avskriften om "sida för sida":
    - Fältet töms efter varje Skicka, för att minska risk att dubblettexter sparas
	- Texten läggs ihop, förutom text som redan sparats ner, alltså inga "textdubbletter" sparas
    - Om inte supertranskriberare: till transcription_comment på huvudpost som inte publiceras direkt
    - Om supertranskriberare: till comment på huvudpost som publiceras direkt

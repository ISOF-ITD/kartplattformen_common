# Användningsfall Transkribering fritext
# Syfte
Transkribera uppteckningar med fri struktur som fritext

# Mål

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp "fritext"

# Huvudflöde
1. I Vänster panel visa: Inmatningsfält för uppgifter
- Fält som egna rader:
  - Text: Text är skriven på sidan
  - Kommentar till avskriften om inte "sida för sida":
    - Om inte supertranskriberare: till transcription_comment som inte publiceras direkt
    - Om supertranskriberare: till comment som publiceras direkt
  - Kommentar till avskriften om "sida för sida":
    - Fältet töms efter varje Skicka, för att minska risk att dubblettexter sparas
	- Texten läggs ihop, förutom text som redan sparats ner, alltså inga "textdubbletter" sparas
    - Om inte supertranskriberare: till transcription_comment på huvudpost som inte publiceras direkt
    - Om supertranskriberare: till comment på huvudpost som publiceras direkt

# Användningsfall Transkribera uppteckning
# Syfte
Transkribera uppteckning med alla sidor i uppteckningen inom en transkriberingssession.

# Mål

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp som inte är "sida för sida"

# Huvudflöde
1. Höger panel: Bilder att transkribera
- Över: Visa aktuell sida att transkribera som stor bild, typ 2/3 i bredd och höjd
  - Möjligt att zooma in i bilden med t.ex. + och - knappar
- Under: Visa lista på övriga sidor i uppteckningen som ska transkriberas.
2. Vänster panel: Inmatningsfält för uppgifter
- Om transkriberingstyp "uppteckningsblankett": **Användningsfall Transkribering uppteckningsblankett** 
- Om transkriberingstyp "fritext": **Användningsfall Transkribering fritext** 
- Kommentar till avskriften:
- Text: Vill du att vi anger att det är du som har skrivit av uppteckningen? Ange i så fall ditt namn och din e-postadress nedan. E-postadressen publiceras inte.
Vi hanterar personuppgifter enligt dataskyddsförordningen. Läs mer. "Pekar på": https://www.isof.se/vart-uppdrag/om-myndigheten/om-webbplatsen/hantering-av-personuppgifter
- Fält som egna rader:
  - Ditt namn (frivilligt):
  - Din e-post adress (frivilligt):
- Knapp "Skicka"
3. Vid tryck på "Skicka":
- Uppteckningen skickas till server
- Svar om ok: "Tack för din avskrift..."
- Svar om fel: Felmeddelande

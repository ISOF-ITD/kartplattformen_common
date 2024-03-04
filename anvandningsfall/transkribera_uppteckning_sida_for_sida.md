# Användningsfall Transkribera uppteckning sida för sida
# Syfte
Transkribera uppteckning med varje sida i uppteckningen som en egen transkriberingssession.

# Mål

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp "sida för sida"

# Huvudflöde
1. Höger panel: Bilder att transkribera
- Över: Visa aktuell sida att transkribera som stor bild, typ 2/3 i bredd och höjd
  - Möjligt att zooma in i bilden med t.ex. + och - knappar
  - Första sida inom uppteckningen som inte är transkriberad visas här 
- Under: Visa lista på övriga sidor i uppteckningen som ska transkriberas.
- Knappar visas:
  - "Föregående sida"
  - "Nästa sida" (oavsett transkriptionsstatus då användaren kan behöva läsa redan transkriberad sida)
  - "Föregående sida att skriva av"
  - "Nästa sida att skriva av"
  - För förflytningsknapparna:
    - Lås ny sida för transkribering och lås upp gammal sida 
2. Vänster panel: Inmatningsfält för uppgifter
- Om transkriberingstyp "uppteckningsblankett": **Användningsfall Transkribering uppteckningsblankett** 
- Om transkriberingstyp "fritext": **Användningsfall Transkribering fritext** 
- Kommentar till avskriften:
- Text: Vill du att vi anger att det är du som har skrivit av uppteckningen? Ange i så fall ditt namn och din e-postadress nedan. E-postadressen publiceras inte.
Vi hanterar personuppgifter enligt dataskyddsförordningen. Läs mer. "Pekar på": https://www.isof.se/vart-uppdrag/om-myndigheten/om-webbplatsen/hantering-av-personuppgifter
- Fält som egna rader:
  - Ditt namn (frivilligt):
  - Din e-post adress (frivilligt):
- Inlämningsknapp(ar) - (bättre här under själva inmatningen?):
  - "Skicka" (visas om sidan inte avskriven)
  - _"Spara och fortsätt"? Behövs kanske inte när det bara är en sida att transkribera inom en transkriberingssession!_
3. Vid tryck på "Skicka":
- Uppteckningen skickas till server
- Svar om ok: "Tack för din avskrift..."
- Svar om fel: Felmeddelande

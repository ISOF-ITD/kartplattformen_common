# Användningsfall Transkribera uppteckning
# Syfte
Transkribera uppteckning med alla sidor i uppteckningen inom en transkriberingssession.
Mer lämpligt för accessioner/uppteckningar som består av ett mindre antal sidor.

Fördelar:
- Godkännande kan gå lite snabbare: Färre rader i databasen att godkänna
- UI för godkännande lite enklare

Nackdelar:
- Transkribering blir inte direkt vid sparning kopplad till sin sida: i stället radbrytningstecken som kan missas och placeras fel
- Längre tid innan transkribering sparas: Att transkribera många sidor tar tid
  - Mer behov av "Spara och fortsätt"

# Mål

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp som inte är "sida för sida"

# Huvudflöde
1. Höger panel: Bilder att transkribera
- Överdel Visningsläge: Visa aktuell sida att transkribera som stor bild, typ 2/3 i bredd och höjd
  - Möjligt att zooma in i bilden med t.ex. "mus-rulle" och + och - knappar
- Underdel "Lista över filer"-läge: Visa lista på övriga sidor i uppteckningen som ska transkriberas.
2. Vänster panel: Inmatningsfält för uppgifter
- Om transkriberingstyp "uppteckningsblankett": **Användningsfall Transkribering uppteckningsblankett** 
- Om transkriberingstyp "fritext": **Användningsfall Transkribering fritext** 
- Kommentar till avskriften:
- Text visas: "Vill du att vi anger att det är du som har skrivit av uppteckningen? Ange i så fall ditt namn och din e-postadress nedan. E-postadressen publiceras inte.
Vi hanterar personuppgifter enligt dataskyddsförordningen. Läs mer." "Pekar på": https://www.isof.se/vart-uppdrag/om-myndigheten/om-webbplatsen/hantering-av-personuppgifter
- Fält som egna rader:
  - Ditt namn (frivilligt):
  - Din e-post adress (frivilligt):
- Inlämningsknapp(ar):
  - "Skicka"
  - _"Spara och fortsätt"? Finns behov att spara emellanåt när det är många sidor att transkribera inom en transkriberingssession!_
    - Uppteckningar med många sidor kan göras som transkribera "sida för sida"
3. Vid tryck på "Skicka":
- Uppteckningens transkription och övriga uppgifter skickas till server
- Svar om ok: "Tack för din avskrift..."
- Svar om fel: Felmeddelande

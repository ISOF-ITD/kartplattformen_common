# Användningsfall Transkribera uppteckning sida för sida
# Syfte
Transkribera uppteckning med varje sida i uppteckningen som en egen transkriberingssession.
Mer lämpligt för accessioner/uppteckningar som består av många sidor.

Fördelar:
- Transkribering blir direkt vid sparning kopplad till sin sida
- Kortare tid innan transkribering sparas: Att transkribera bara en sida går hyfsat snabbt
  - Mindre behov av "Spara och fortsätt"

Nackdelar:
- Godkännande kan ta mer tid: Fler rader i databasen att godkänna
- UI för godkännande lite mer komplext

# Mål

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp "sida för sida"

# Huvudflöde
1. Höger panel: Bilder att transkribera ✅
- Överdel Visningsläge: Visa aktuell sida att transkribera som stor bild, typ 2/3 i bredd och höjd ✅
  - Möjligt att zooma in i bilden med t.ex. "mus-rulle" och + och - knappar ✅
  - Första sida inom uppteckningen som inte är transkriberad visas här  ✅
- Mellandel: Panel med knappar i följd vågrätt visas:
  - "Föregående sida" (oavsett transkriptionsstatus då användaren kan behöva läsa tidigare sida)
  - "Nästa sida" (oavsett transkriptionsstatus då användaren kan behöva läsa nästa sida)
  - "Nästa sida att skriva av" (visa nästa sida som har transkriptionsstatus "publicerad för transkribering")
  - För förflytningsknapparna:
    - Lås ny sida för transkribering och lås upp gammal sida 
- Underdel "Lista över filer"-läge: Visa lista på övriga sidor i uppteckningen som ska transkriberas, max 5 stycken. Ett tryck på en sida lägger den sidan i Visningsläge.
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
  - "Skicka in aktuell sida och gå vidare till nästa sida att skriva av".
	- Vid sista sida: ligg kvar på sista sida.
  - INTE AKTUELLT: "Spara och fortsätt"? Behövs kanske inte när det bara är en sida att transkribera inom en transkriberingssession!-
3. Vid tryck på "Skicka":
- Uppteckningens transkription och övriga uppgifter skickas till server
- Svar om ok: "Tack för din avskrift...". Längst upp på den "nya" sidan, inte overlay som behöver "klickas bort"
- Svar om fel: Felmeddelande (500, för få tecken)

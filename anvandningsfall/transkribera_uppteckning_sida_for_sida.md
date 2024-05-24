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

# Testa med:
- https://garm-test.isof.se/demo/folke-sida-for-sida/www/#/transcribe/records/liu00198_194713_1
- https://garm-test.isof.se/TradarkAdmin/admin/TradarkAdmin/records/liu00198_5F194713_5F1/

# Förutsättningar
Användaren har valt en uppteckning att transkribera som har transkriberingstyp "sida för sida"

# Huvudflöde
1. Höger panel: Bilder att transkribera
  - ✅ Överdel Visningsläge: Visa aktuell sida att transkribera som stor bild, typ 2/3 i bredd och höjd
  - ✅ Möjligt att zooma in i bilden med t.ex. "mus-rulle" och + och - knappar
  - ✅ Första sida inom uppteckningen som inte är transkriberad visas här
  - ✅ Mellandel: Panel med knappar i följd vågrätt visas:
    - ✅ "Föregående sida" (oavsett transkriptionsstatus då användaren kan behöva läsa tidigare sida)
    - ✅ "Nästa sida" (oavsett transkriptionsstatus då användaren kan behöva läsa nästa sida)
    - ✅ "Nästa sida att skriva av" (visa nästa sida som har transkriptionsstatus "publicerad för transkribering")
  - ✅ Underdel "Lista över filer"-läge: Visa lista på övriga sidor i uppteckningen som ska transkriberas, max 5 stycken. Ett tryck på en sida lägger den sidan i Visningsläge.
2. Vänster panel: Inmatningsfält för uppgifter
  - ✅ Om transkriberingstyp "uppteckningsblankett": **Användningsfall Transkribering uppteckningsblankett**
  - ✅ Om transkriberingstyp "fritext": **Användningsfall Transkribering fritext**
  - ✅ Kommentar till avskriften:
    - ✅ Kommentar ska kopplas till en sida
    - ✅ Text: "Kommentar till sida 15 av 30" (skriv "av 30" på alla ställen där sidnummer nämns. enhetligt!)
  - ✅ Text: Vill du att vi anger att det är du som har skrivit av uppteckningen? Ange i så fall ditt namn och din e-postadress nedan. E-postadressen publiceras inte. Vi hanterar personuppgifter enligt dataskyddsförordningen. Läs mer. "Pekar på": https://www.isof.se/vart-uppdrag/om-myndigheten/om-webbplatsen/hantering-av-personuppgifter
  - ✅ Fält som egna rader:
    - ✅ Ditt namn (frivilligt):
    - ✅ Din e-post adress (frivilligt):
  - ✅ Inlämningsknapp - (bättre här under själva inmatningen?):
    - ✅ "Skicka in aktuell sida och gå vidare till nästa sida att skriva av".
    - ✅ Vid sista sida: ligg kvar på sista sida.


- ✅ Navigation mellan sidor: Användaren bör kunna navigera mellan olika sidor utan att vara tvungen att skicka in dem för godkännande.
- ✅ Låsning av dokumentet: När en användare påbörjar transkriberingen av en sida, låses hela dokumentet för andra användare. Detta förhindrar att flera personer arbetar på samma dokument samtidigt, vilket minimerar risken för konflikter.
- ✅ Hantering av inskickade sidor: När en sida har skickats in, blir den låst och kan inte redigeras vidare. Användaren kan dock fortfarande se vad de har skrivit. Detta ger möjlighet att granska sitt eget arbete samtidigt som man fortsätter transkribera andra sidor.
- ✅ Upplåsning vid avslut: När användaren lämnar transkriberingsvyn, upplåses hela dokumentet automatiskt. Detta gör det möjligt för andra användare att gå in och transkribera de sidor som inte har blivit behandlade.
- ✅ Vi behöver bara låsning på recordnivå.
- ✅ När vi skickar in /transcribe så måste vi kolla om record får editeras
- ✅ OBS! Kontroller! man måste ha en markering vilka sidor som inte sparats. man behöver också få ett meddelande när man vill lämna sidan!
- ✅ Olika ramfärger, beroende på status på sidan (osparat, sparat, annan har skrivit av)
- ☐ Avancerat: Lägg till en extra knapp "Skicka in alla sidor"
  - ☐ lägg till förhandsvisning av det man skickar in. man behöver scrolla ända längst ner, först sen kan man godkänna inskickandet
- ✅ lägg till de 3 hjälp-knapparna i mörkgröna huvudpanelen även i denna vy
- ☐ Knappen "skriva av" i record-vyn: Ändra text till "skriv av uppteckning" eller "skriv av sida för sida"
- ☐ Samma uppe i den gröna panelen

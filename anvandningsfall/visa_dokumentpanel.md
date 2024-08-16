# Användningsfall Visa dokumentpanel
# Syfte
Visa dokument (uppteckning eller inspelning)

# Mål

# Förutsättningar
Användaren har valt ett dokument i en dokumentlista (huvudlista, ortlista, personlista)

# Huvudflöde
1. Visa huvuduppgifter
- Record titel
- Accessionsnummer 
- Antal uppteckningar
- Materialtyp
  - Arkiv
  - Tryckt
  - Fler?
2. Visa material
- Om text/bild: Visa bildfiler
  - Alla visas (_Dölj frågelistor bakom "Visa frågelista?"_)
- Om ljud: Visa lista på ljudfiler
  - Kolumner:
  - Play-knapp (Visar och startar ljudspelaren)
  - Ljudfilstitel efter tillgång: 1) Titel 2) Text efter filnamn i Innehåll 3) Interjuad person + År
3. Beroende på record_type
- Om one_accession_row och inget material digitaliserat (och Göteborg/Lund): **EJ IDAG**
    - Den här uppteckningen är inte publikt tillgänglig digitalt.
    - Vill du att den ska bli det!
    - Knapp: "Tillgängliggör på Folke"
- Om one_record, transkriberingstyp inte "sida för sida" och avskriven:
    - text
	  - visas sida för sida med "ram" runt varje sida
- Om one_record, transkriberingstyp "sida för sida" och avskrift publicerad:
  - För varje media.text:
    - visa sida för sida med "ram" runt varje sida med text tillsammans med sin jpg-fil
    - AVVAKTAR tills stort behov finns: sidor som inte transkriberats än: "Ej transkiberad"
- Om one_record och inte avskriven:
    - Den här uppteckningen är inte avskriven.
    - AVVAKTAR tills stort behov finns: Om "sida för sida" och sida finns kvar att skriva av: Den här uppteckningen är bara delvis avskriven.
    - Vill du vara med och tillgängliggöra samlingarna för fler? Hjälp oss att skriva av berättelser!
    - Knapp: "Skriv av"
4. Visa uppgifter:
- Kopiera länk
- Källhänvisning
- Licens
5. Om accession: Lista på Uppteckningar (dokumentlista)
6. Visar "Personlista":
- Namn (Länk till personpanel)
- Födelseår
- Födelseort
- Roll
7. Platslista med platsnamn, med länk till platspanel, och enkel karta som visar markörer för varje plats (SimpleMap)
8. Visa uppgifter:
- Arkiv
- Materialtyp
- År
- Acc. nr
- Sidnummer
9. Visa arkivets logga



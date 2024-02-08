# Användingsfall Visa sökpanel
# Syfte
Visa lista över dokument (uppteckning eller inspelning)

# Mål

# Förutsättningar
Användaren har valt filter

# Huvudflöde
1. "Sökträffar som lista"
2. Visa tidsdiagram över år (year = insamlings eller inlämningsår)
3. Visar X-Y av Z (Visar 1-8 av 8)
4. Knappar: "Föregående" "Nästa"
5. Visa lista över dokument. Hierarkiskt:
- accessionsrad (one_accession_row)
- recordrader som hör till accessionsraden (one_record)
- Kolumner:
  - Titel
  - Arkivnummer (sorterbar)
  - Ort (länk till ort)
  - Insamlare (länk till person som är insamlare)
  - År
  - Avskriven
6. Expandera "Uppteckningar i den här accessionen"
- Alla tillhörande one_record visas i lista med sidnummer
7. Filtera i tidsdiagrammet genom att välja tidsperiod grafiskt från-till



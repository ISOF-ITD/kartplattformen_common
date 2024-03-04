# Användningsfall Visa huvudpanel
# Syfte
Hitta material genom att välj funktion och utval (sökning)

# Mål

# Förutsättningar
Användaren har vänsterpanelen (huvudpanelen) expanderad och aktiv

# Huvudflöde
1. Visa funktioner att välja mellan:
- Arkivmaterial
- Skriv av (accessioner/one_accession_row som har one_records)
2. Visa filter med avbockning på mediatyp med antal träffar på varje
- Text (default)
- Ljud
- Bild
- **Fler ej idag:**
- Ljud med transkribering
- _"Digitaliserad och tillgänglig publik" (i stället för aldrig visa icke-digitaliserat)_
- Fler från formtyp, t.ex. teckning?
3. För liten mängd värden som filter: Visa lista med avbockning (med antal träffar på varje?) **EJ IDAG**
- Kategorier: alla tradark?
- Importerade kategorier från t.ex. matkartan, sägenkartan
- Realkatalog-kategorier
- Språk som kategorityp language (eller physical_media.language)
4. För stor mängd värden: Visa lista i t.ex. rullgardinsmeny som filter **EJ IDAG**
- Frågelista i kategorityp (eller physical_media.questionnaire)? Alla som finns i Folke?
5. Knapp: "Skriv av slumpmässig uppteckning"
- 
6. Visa sökfält för fritextsök
7. För varje tecken i fritextsök: Sökförslag som börjar på angivna tecken för:
- Sök på personer
- Sök på orter (socken) 
8. Knapp: Sök
9. Vid tryck på knapp sök:
- Sökning utförs
    - Med requiredParams:
        - // transcriptionstatus: 'readytotranscribe,undertranscription,transcribed,reviewing,needsimprovement,approved,published',
        - mark_metadata: 'transcriptionstatus', _Varför? Kanske föra att icke-folke kan sakna denna_
        - materialtyp type: arkiv, _Även tryckt? För tidningsurklipp?_
        - categorytypes: 'tradark'. Obligatoriskt att tradark är med.
        - publishstatus: 'published'. Bara publicerat utifall icke-publicerat av misstag hamnar i sökdatabasen
        - has_media: 'true', // **TODO: Bekräfta att vi ska använda detta**


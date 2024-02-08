# Användingsfall Visa dokumentpanel
# Syfte
Visa plats (Lantmäteriet sockenstad inom Sverige)

# Mål

# Förutsättningar
Användaren har valt en plats i kartan eller en dokumentlista (huvudlista, ortlista, personlista)

# Huvudflöde
1. Visa huvuduppgifter
- Socken/Stad namn
- Geografisk indelning:
  - Sverige: Härad, län, landskap
  - Finland/Estland: attribut fylke som egentligen är någon sorts "region"
  - Norge: fylke
- Kommentar, t.ex. "Även Öm socken ingår" (socken.comment)
- Enkel karta som visar markörer för varje plats (SimpleMap)
- Lista på filter: 1) Allt (default) 2) Accessioner 3) Uppteckningar
2. Om användaren inte gjort filter/sökning 
- Visa huvudlista utifrån filter
  - Förutom: Visa tidsdiagram
3. Om användaren gjort filter/sökning 
- Sökträffar. Visa huvudlista utifrån filter
  - Förutom: Visa tidsdiagram
- Samtliga accessioner och uppteckningar från orten. Visa huvudlista utifrån filter
  - Förutom: Visa tidsdiagram



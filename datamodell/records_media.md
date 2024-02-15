# Datamodell records_media
Mediafiler kopplade till en records_media

Unik verksamhetsnyckel: Record?, Source?

|Attribut|Datatyp|Verksamhets-begrepp|Beskrivning|
|---|---|---|---|
|Record|Text|Record-id|Foreign key till records
|Archive_row|Int|Radnummer i arkiv|Unikt radnummer i arkiv \\(accessionsregister eller liknande)|
|media|Int||Ingen funktion TAS BORT! Samma id som unik-nyckel! \\Oklart vad används till.|
|media_type\\(purpose)|Text|Media typ|


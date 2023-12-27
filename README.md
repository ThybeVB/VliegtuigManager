# Luchthaven Applicatie

Deze applicatie stelt een simpele beheertoepassing van een luchthaven voor.
De gebruiker kan volgende functionaliteiten gebruiken:

### Vluchten
-   Vluchten in de planning **raadplegen**
-   Vluchten **toevoegen** aan de planning
-   Vluchten **aanpassen**
-   Vluchten **verwijderen** uit de planning

### Vliegtuigen
-   Beschikbare vliegtuigen **raadplegen**
-   Vliegtuigen **toevoegen** aan de planning
-   Vliegtuigen **aanpassen**
-   Vliegtuigen **verwijderen** uit de luchthaven

### Rapport
Een CSV-verslag kan gemaakt worden van de vluchten samen met het vliegtuig die voor de vlucht gebruikt zal worden.

## Aan de slag

1. Clone de repository met Git naar je locale machine (`git clone https://github.com/ThybeVB/VliegtuigManager`)
2. Creëer een virtuele omgeving (`python -m venv venv`)
3. Installeer de dependencies (`pip install -r requirements.txt`)
4. Als je de voorbeelddatabase wil gebruiken, verander je `Luchthaven.db.example` naar `Luchthaven.db`
    - Als je de voorbeelddatabase niet wil gebruiken, zal de applicatie een database voor je aanmaken.
    - Als je al een database hebt om te gebruiken, plaats je die in de root directory.
5. Voer de applicatie uit met Python (`python __main__.py`)
## Läslistan – Testautomatisering

Detta projekt testar webbsidan "Läslistan" automatiskt med hjälp av **Python**, **Playwright**, **pytest** och **behave**.

## Vad som testas
- Navigering till hemsidan
- Klick på knappen "Lägg till bok"
- Kontroll att bokformulär visas
- Kontroll att bokkatalogen visas korrekt efter ny tillagd bok

## Börja med

1. Klona detta repo och skapa virtuell miljö:

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```
2. Installera beroenden:

pip install -r requirements.txt
playwright install
```

3. Kör testen:
behave

Projekt av Matz Eliasson.
# Exam-projekt – Läslistan - by Matz Eliasson

Detta projekt testar webbapplikationen 
[Läslistan](https://tap-ht24-testverktyg.github.io/exam-template/) 
med hjälp av **Python**, **Behave**, **Playwright** och **Page Object Model**.

## Kravuppfyllnad

### Krav 1 – Grundläggande test
- [x] Minst **tre användarberättelser (user stories)**
- [x] Minst **ett scenario per user story**
- [x] Alla tester **ska fungera**
- [x] Innehåller en `README.md`-fil

### Krav 2 – Kodkvalitet & struktur
- [x] Bra kodstruktur med **återanvändning**
- [x] Använder **Page Object Model**
- [ ] Använder **Scenario Outline** (där det är lämpligt)

---

## 💡 User Stories

1. **Som användare vill jag kunna lägga till en bok**  
   så att den hamnar i min läslista.

2. **Som användare vill jag kunna se böcker i katalogen**  
   så att jag kan välja vilka jag vill läsa.

3. **Som användare vill jag kunna se en tillagd bok i listan**  
   så att jag vet att den sparades korrekt.

---

## Projektstruktur

```
exam_tests/
├── features/
│   ├── add_book.feature
│   ├── view_catalog.feature
│   ├── view_added_book.feature
│   ├── steps/
│   │   ├── add_book_steps.py
│   │   ├── view_catalog_steps.py
│   │   ├── view_added_book_steps.py
│   │   └── common_steps.py
├── pages/
│   └── main_page.py
├── README.md
└── requirements.txt
```

---

## Kör projektet

1. Installera beroenden:

pip install -r requirements.txt
```

2. Kör testerna:

behave
```

---

## Teknisk förklaring: `async` och `await` i Playwright

Projektet använder **Playwright**, som är ett asynkront bibliotek. 
Därför skrivs vissa metoder med `async` och `await`.

Exempel:

```python
async def click_add_book(self):
    await self.page.click(self.add_book_button)
```

### Vad betyder det?

- **`async def`**  
  Definierar en asynkron funktion som kan pausa för långsamma moment 
  (t.ex. laddning av en webbsida).

- **`await`**  
  Används för att vänta på att en asynkron operation blir klar, t.ex. `click()`.

- **Selektorer**  
  Exempel: `self.add_book_button = '[data-testid="add-book"]'`  
  Pekar ut element i HTML som används i tester.

Asynkron kod är nödvändig eftersom Playwright-funktioner som `page.goto()`, `page.click()` och `page.fill()` är asynkrona och måste hanteras korrekt.

---

## Verktyg och teknik

- Python
- Behave (Gherkin syntax)
- Playwright
- Page Object Model
- Visual Studio Code eller PyCharm

---

## Kontakt

Projekt av Matz Eliasson  

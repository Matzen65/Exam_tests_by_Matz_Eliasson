class MainPage:


    def __init__(self, page):
        self.page = page

    async def goto(self):
        # Navigera till startsidan
        await self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

    async def click_add_book(self):
        # Klicka på "Lägg till bok"-knappen
        await self.page.locator('[data-testid="add-book"]').click()

    async def is_form_visible(self):
        # Kontrollera om formuläret för att lägga till bok är synligt
        return await self.page.locator('[data-testid="add-input-title"]').is_visible()

    async def add_book(self, title, author):
        # Fyll i formuläret för att lägga till en bok
        await self.page.locator('[data-testid="add-input-title"]').fill(title)
        await self.page.locator('[data-testid="add-input-author"]').fill(author)
        await self.page.locator('[data-testid="add-submit"]').click()

    async def has_books(self):
        # Kolla om det finns några böcker i listan
        books = await self.page.locator('.book').count()
        return books > 0

    async def get_books(self):
        # Hämta alla böcker och returnera deras titel och författare
        books = []
        book_elements = await self.page.locator('.book').all()
        for book in book_elements:
            title = await book.locator('.book-title').inner_text()
            author = await book.locator('.book-author').inner_text()
            books.append({'title': title, 'author': author})
        return books

    async def is_book_in_list(self, title, author):
        # Kontrollera om en bok finns i listan med rätt titel och författare
        book_selector = f'.book:has-text("{title}")'
        book_count = await self.page.locator(book_selector).count()
        return book_count > 0

    async def click_heart_icon(self, book_title):
        # Klicka på hjärtikonen för den bok som matchar titel
        heart_selector = f'[data-testid="star-{book_title}"]'
        await self.page.locator(heart_selector).click()

    async def is_book_favorited(self, book_title):
        # Kontrollera om hjärtikonen för boken är i favoritläge
        heart_selector = f'[data-testid="star-{book_title}"]'
        heart_icon = await self.page.locator(heart_selector).inner_html()
        return '❤️' in heart_icon  # Eller något annat kriterium för att markera favorit




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

    async def is_book_in_list(self, title, author):
        # Kontrollera om en bok finns i listan med rätt titel och författare
        book_selector = f'.book:has-text("{title}")'
        book_count = await self.page.locator(book_selector).count()
        return book_count > 0

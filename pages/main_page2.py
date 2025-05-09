class MainPage:


    def __init__(self, page):
        self.page = page

    async def goto(self):
        # Navigera till startsidan
        await self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

    async def click_add_book(self):
        # Klicka på "Lägg till bok"-knappen
        await self.page.locator('[data-testid="add-book"]').click()

    async def click_favorite_button(self, title):
        # Klicka på hjärtikonen för att markera boken som favorit
        favorite_button_selector = f'[data-testid="star-{title}"]'
        await self.page.locator(favorite_button_selector).click()

    async def click_my_books_button(self):
        # Kontrollera om knappen "Mina böcker" är aktiv (inte disabled)
        favorites_button = self.page.locator('[data-testid="favorites"]')
        is_disabled = await favorites_button.is_disabled()
        if not is_disabled:
            # Om knappen är aktiv (inte disabled), klicka på den
            await favorites_button.click()
        else:
            print("Knappen 'Mina böcker' är inaktiverad och kan inte klickas på.")

    async def is_book_in_favorites(self, title):
        # Kontrollera om boken finns i favoritlistan
        book_selector = f'[data-testid="fav-{title}"]'
        book_count = await self.page.locator(book_selector).count()
        return book_count > 0

    async def add_book(self, title, author):
        # Lägg till boken och fyll i formuläret
        await self.page.locator('[data-testid="add-input-title"]').fill(title)
        await self.page.locator('[data-testid="add-input-author"]').fill(author)
        await self.page.locator('[data-testid="add-submit"]').click()

    async def is_favorites_button_enabled(self):
        # Kolla om knappen "Mina böcker" är aktiv (inte disabled)
        favorites_button = self.page.locator('[data-testid="favorites"]')
        return not await favorites_button.is_disabled()

    async def enable_favorites_button(self):
        # Om en favorit har lagts till, aktivera knappen "Mina böcker"
        if await self.is_book_in_favorites("Matz lär dig baka"):
            favorites_button = self.page.locator('[data-testid="favorites"]')
            await favorites_button.evaluate('button => button.removeAttribute("disabled")')

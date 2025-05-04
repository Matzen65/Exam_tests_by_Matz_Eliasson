from behave import given, when, then
from pages.main_page_1 import MainPage

# Given: Att användaren har öppnat sidan "lägg till bok"
@given('att användaren har öppnat sidan "lägg till bok"')
def step_impl(context):
    context.page = context.browser.new_page()
    context.main_page = MainPage(context.page)
    context.main_page.goto()  # Gå till hemsidan där man kan lägga till bok

# Then: Att användaren lägger till boken "Matz lär dig baka" av "Matz Eliasson"
@then('att användaren lägger till boken "{title}" av "{author}"')
async def step_impl(context, title, author):
    await context.main_page.add_book(title, author)

# And: Ska boken "Matz lär dig baka" av "Matz Eliasson" visas nederst i listan
@then('ska boken "{title}" av "{author}" visas nederst i listan')
async def step_impl(context, title, author):
    # Här kan du kontrollera om boken finns nederst i listan
    books = await context.main_page.get_books()

# Kontrollera att den sista boken i listan har rätt titel och författare
    last_book = books[-1]
    assert last_book['title'] == title, f"Förväntade titel: {title}, men fick {last_book['title']}"
    assert last_book['author'] == author, f"Förväntade författare: {author}, men fick {last_book['author']}"

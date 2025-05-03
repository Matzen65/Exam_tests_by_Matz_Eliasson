from behave import given, when, then
from pages.main_page import MainPage


@given('att användaren har lagt till boken "{title}" av "{author}"')
async def step_impl(context, title, author):
    context.page = await context.browser.new_page()
    context.main_page = MainPage(context.page)
    await context.main_page.goto()
    # Lägg till boken med hjälp av metoden för att fylla i titeln och författaren.
    await context.main_page.add_book(title, author)

@then('ska boken "{title}" av "{author}" visas i listan')
async def step_impl(context, title, author):
    # Kontrollera att boken finns i listan
    assert await context.main_page.is_book_in_list(title, author)

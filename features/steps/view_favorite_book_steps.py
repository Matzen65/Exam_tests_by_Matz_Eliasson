from behave import given, when, then
from time import sleep  # För att eventuellt pausa för att se resultatet (valfritt)

@given('att användaren är på hemsidan och har markerat boken "Matz lär dig baka" som favorit')
async def step_impl(context):
    # Öppna hemsidan
    await context.main_page.goto()
    # Lägg till boken "Matz lär dig baka" och markera den som favorit
    await context.main_page.add_book("Matz lär dig baka", "Matz Eliasson")
    await context.main_page.click_add_book()
    await context.main_page.click_favorite_button("Matz lär dig baka")  # Markera som favorit

@when('användaren klickar på knappen "Mina böcker"')
async def step_impl(context):
    # Klicka på knappen "Mina böcker"
    await context.main_page.click_my_books_button()

@then('ska boken "Matz lär dig baka" visas i listan med favoritböcker')
async def step_impl(context):
    # Kontrollera om boken "Matz lär dig baka" finns i favoritlistan
    is_favorite_book_visible = await context.main_page.is_book_in_favorites("Matz lär dig baka")
    assert is_favorite_book_visible, 'Favoritboken "Matz lär dig baka" syns inte i listan'

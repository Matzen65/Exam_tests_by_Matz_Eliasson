from behave import given, when, then
from time import sleep

@given('att användaren är på hemsidan efter att boken "{book_title}" lagts till')
async def step_given_user_is_on_homepage_after_adding_book(context, book_title):
    # Navigera till hemsidan och vänta på att boken ska ha lagts till
    await context.main_page.goto()
    assert await context.main_page.is_book_in_list(book_title, "Matz Eliasson")  # Kontrollera att boken finns i listan

@when('användaren öppnar boklistan')
async def step_when_user_opens_catalog(context):
    # Kontrollera att boklistan är synlig
    assert await context.main_page.is_book_in_list('Matz lär dig baka', 'Matz Eliasson')

@when('användaren klickar på hjärtikonen för boken "{book_title}"')
async def step_when_user_clicks_heart_icon(context, book_title):
    # Klicka på hjärtikonen för den valda boken
    await context.main_page.click_heart_icon(book_title)

@then('ska boken "{book_title}" vara markerad som favorit')
async def step_then_book_is_marked_as_favorite(context, book_title):
    # Kontrollera att boken har blivit markerad som favorit
    is_favorite = await context.main_page.is_book_favorited(book_title)
    assert is_favorite, f'Boken {book_title} är inte markerad som favorit'

from behave import when, then


@then("ska en lista med böcker visas")
async def step_impl(context):
    # Kontrollera att listan med böcker är synlig
    assert await context.main_page.has_books()

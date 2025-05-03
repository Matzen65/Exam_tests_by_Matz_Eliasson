from behave import when, then


@when('användaren klickar på knappen "Lägg till bok"')
async def step_impl(context):
    await context.main_page.click_add_book()

@then("visas ett formulär för att lägga till bok")
async def step_impl(context):
    assert await context.main_page.is_form_visible()


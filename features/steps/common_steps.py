"""
common_steps.py innehåller gemensamma stegdefinitioner som används av flera
scenarier. Den största nyttan är att undvika duplicering av kod.
I detta fall innehåller filen ett @given-steg som initialiserar testmiljön
"""

from behave import given
from pages.main_page import MainPage

@given("att användaren är på hemsidan")
async def step_impl(context):
    context.page = await context.browser.new_page()
    context.main_page = MainPage(context.page)
    await context.main_page.goto()

from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def after_all(context):
    #input("Tryck Enter för att stänga webbläsaren...")
    context.browser.close()
    context.playwright.stop()
from playwright.sync_api import Page


def test1(page: Page):
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator('.desktop-impact-items-F7T6E').screenshot(path="output/1.png")



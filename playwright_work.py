import time
from playwright.sync_api import sync_playwright


def sign_in(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://automationpractice.com/index.php")
    page.locator(".login").click()
    return page


def do_login(page, email, password):
    page.locator("#email").fill(email)
    page.locator("#passwd").fill(password)
    page.locator("#SubmitLogin").click()


def valid_input(email, password, text):
    with sync_playwright() as playwright:
        page = sign_in(playwright)
        do_login(page, email, password)
        time.sleep(2)
        return text in page.locator('#center_column > div.alert.alert-danger > ol > li').inner_text()


def buy_dress():
    with sync_playwright() as playwright:
        page = sign_in(playwright)
        do_login(page, email="asdasd@wxz.com", password="123456")
        index_of_min_price = 0

        #search for "summer"
        page.locator('#search_query_top').fill("summer")
        page.locator("#searchbox > button").click()
        time.sleep(3)

        right_blocks = page.query_selector_all(".right-block")
        prices = []
        for obj in right_blocks:
            price_product = obj.query_selector(".content_price")
            price = price_product.query_selector(".price").inner_text()
            prices.append(float(price[1:]))
            lowest_price = min(prices)
            index_of_min_price = prices.index(lowest_price)
        # finding the lowest price summer dress
        add_to_cart = right_blocks[index_of_min_price]
        page.wait_for_timeout(3000)
        add_to_cart.hover()
        # click "Add to cart" on the min price dress
        add_to_cart.query_selector("text='Add to cart'").click()
        time.sleep(5)
        page.locator("text='Proceed to checkout'").click()
        time.sleep(5)
        page.locator(".standard-checkout").click()
        time.sleep(2)
        page.locator("#center_column > form > p > button").click()
        time.sleep(2)
        page.locator("input#cgv").click()
        time.sleep(1)
        page.locator("#form > p > button").click()
        time.sleep(2)
        page.locator("#HOOK_PAYMENT > div:nth-child(2) > div > p > a").click()
        time.sleep(2)
        page.locator("#cart_navigation > button").click()
        time.sleep(2)
        page.close()
        return lowest_price









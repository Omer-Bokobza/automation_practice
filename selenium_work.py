import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = "C:/Users/omerb/Desktop/Sela/chromedriver.exe"


def sign_in():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.CLASS_NAME, "login").click()
    return driver


def do_login(driver, email, password):
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#passwd").send_keys(password)
    driver.find_element(By.CLASS_NAME, "icon-lock").click()


def valid_input(email, password, text):
    driver = sign_in()
    # let you continue in Python's unittest when an assertion fails
    try:
        do_login(driver, email, password)
        time.sleep(2)
        return text in driver.find_element(By.CSS_SELECTOR, "#center_column > div.alert.alert-danger > ol > li").text
    finally:
        driver.close()


def buy_dress():
    driver = sign_in()
    do_login(driver, email="asdasd@wxz.com", password="123456")
    index_of_min_price = 0

    # search for "summer"
    driver.find_element(By.ID, "search_query_top").send_keys("summer")
    driver.find_element(By.CSS_SELECTOR, "#searchbox > button").click()
    time.sleep(3)

    right_blocks = driver.find_elements(By.CLASS_NAME, "right-block")
    prices = []
    for obj in right_blocks:
        price_product = obj.find_element(By.CLASS_NAME, "content_price")
        price = price_product.find_element(By.CLASS_NAME, "price").text
        prices.append(float(price[1:]))
        lowest_price = min(prices)
        index_of_min_price = prices.index(lowest_price)

    # finding the lowest price summer dress
    add_to_cart = right_blocks[index_of_min_price]
    actions = ActionChains(driver)
    add_to_cart.find_element(By.CLASS_NAME, 'ajax_add_to_cart_button')
    actions.move_to_element(add_to_cart).perform()
    # click "Add to cart" on the min price dress
    add_to_cart.find_element(By.CSS_SELECTOR, 'a.ajax_add_to_cart_button').click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR,
                        "#layer_cart > div.clearfix > div.layer_cart_cart > div.button-container > a").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "standard-checkout").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#center_column > form > p > button").click()
    time.sleep(2)
    driver.find_element(By.ID, "cgv").click()
    driver.find_element(By.CSS_SELECTOR, "#form > p > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#HOOK_PAYMENT > div:nth-child(2) > div > p > a").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#cart_navigation > button").click()
    time.sleep(2)
    driver.close()
    return lowest_price

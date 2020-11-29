 
import pytest
from .pages.product_page import PageObject
from .pages.locators import ProductPageLocators
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage
import time


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1","2","3","4","5","6","7","8","9"])
def test_guest_can_add_product_to_basket(browser,promo_offer):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
	page = PageObject(browser, link)
	page.open()
	page.shoud_be_btn()
	name = browser.find_element(*ProductPageLocators.NAME_BOOK)
	price = browser.find_element(*ProductPageLocators.PRICE_BOOK)
	name = name.text
	price = price.text
	page.click_to_add()
	page.solve_quiz_and_get_code()
	time.sleep(10)
	page.add_is_ok(name, price)
	
@pytest.mark.need_review	
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageObject(browser, link)
	page.open()
	basket_page = page.go_to_basket()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_basket_is_empty() 
	basket_page.basket_text_empty()	
	
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = PageObject(browser, link)
	page.open()
	page.go_to_login_page()	
	
	

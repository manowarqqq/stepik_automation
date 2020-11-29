#! /usr/bin/python3

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')

class ProductPageLocators():
	ADD_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
	ALERT_NAME = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')
	PTICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
	NAME_BOOK = (By.CLASS_NAME, "col-sm-6.product_main")
	PRICE_BOOK = (By.CLASS_NAME, "price_color")
	SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in")
	
class BasketPageLocators():
	BASKET_TEXT = (By.ID, "content_inner")
	PRODUCTS_IN_BASKET = (By.CLASS_NAME, "table table-condensed")	

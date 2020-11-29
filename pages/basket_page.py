from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert self.browser.current_url, "not correct basket url"
    def basket_text_empty(self):
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
        assert "Ваша корзина пуста" or "Your basket is empty" in text_in_basket.text, "корзина не пустая"
	
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "should not be product in basket"

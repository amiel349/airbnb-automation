from pages.base_page import BasePage
from pages.popup.popup_locators import PopupPageLocators


class PopupPage(BasePage):
    """Popup page actions"""

    def __init__(self, page):
        super().__init__(page)
        self.locators = PopupPageLocators

    def close(self):
        """close pop up"""
        self.click(self.locators.POPUP_CLOSE)
        return

    def present(self):
        return self.is_visible(self.locators.POPUP_DIALOG)
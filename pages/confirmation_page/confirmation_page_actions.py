from pages.Enums import Country
from pages.base_page import BasePage
from pages.confirmation_page.confirmation_page_locators import ConfirmationPageLocators


class ConfirmationPage(BasePage):
    """Confirmation object class"""

    def __init__(self, page):
        super().__init__(page)
        self.locators = ConfirmationPageLocators

    def enter_phone_number(self, phone_number):
        """Enter a phone number in the reservation flow"""
        self.page.wait_for_selector(self.locators.PHONE_INPUT)
        self.page.fill(self.locators.PHONE_INPUT, phone_number)

    def enter_phone_prefix(self, country: Country):
        """Enter a phone number in the reservation flow"""
        self.page.wait_for_selector(self.locators.PHONE_PREFIX)
        self.page.select_option("#country", value=country.value)

    def get_reservation_details(self):
        """Get details from the reservation card"""

        price_element = self.page.locator(self.locators.TOTAL_PRICE)
        price_text = price_element.text_content().strip()

        dates_element = self.page.locator(self.locators.DATES)
        dates_text = dates_element.text_content().strip().replace("Dates","").replace("Edit", '')
        guests_element = self.page.locator(self.locators.GUESTS)
        guests_text = (guests_element.text_content().strip().
                       replace("\xa0", " ").
                       replace("Guests", "").
                       replace("Edit", ""))

        return {
            'price': price_text,
            'dates': dates_text,
            'guests': guests_text
        }

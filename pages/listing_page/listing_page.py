from pages.base_page import BasePage
from pages.listing_page.listing_page_locators import ListingPageLocators
from pages.listing_page.listing_page_actions import ListingPageActions


class ListingPage(BasePage):
    """Listing page object class"""

    def __init__(self, page):
        super().__init__(page)
        self.actions = ListingPageActions(self)
        self.locators = ListingPageLocators

    def get_listing_details(self):
        """Get details about the listing"""
        self.logger.info("Getting listing details")

        title = self.actions.get_listing_title()
        price = self.actions.get_listing_price()
        rating = self.actions.get_listing_rating()

        details = {
            'title': title,
            'price': price,
            'rating': rating
        }

        self.logger.info(f"Listing details: {details}")
        return details

    def get_reservation_card_details(self):
        """Get details from the reservation card"""
        self.logger.info("Getting reservation card details")

        reservation_details = self.actions.get_reservation_details()
        self.logger.info(f"Reservation details: {reservation_details}")

        return reservation_details

    def attempt_reservation(self):
        """Attempt to make a reservation"""
        self.logger.info("Attempting reservation")
        # Click reserve button
        self.actions.click_reserve_button()

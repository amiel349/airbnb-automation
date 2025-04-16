import re
from pages.listing_page.listing_page_locators import ListingPageLocators


class ListingPageActions:
    """Listing page actions"""

    def __init__(self, page_instance):
        self.page = page_instance

    def get_listing_title(self):
        """Get the title of the listing"""
        title_element = self.page.wait_for_selector(ListingPageLocators.LISTING_TITLE)
        return title_element.text_content().strip()

    def get_listing_price(self):
        """Get the price of the listing"""
        price_element = self.page.wait_for_selector(ListingPageLocators.LISTING_PRICE)
        price_text = price_element.text_content().strip()

        # Extract just the number
        match = re.search(r'[\d,]+', price_text)
        if match:
            return int(match.group(0).replace(',', ''))
        return 0

    def get_listing_rating(self):
        """Get the rating of the listing"""
        rating_element = self.page.wait_for_selector(ListingPageLocators.LISTING_RATING)
        rating_text = rating_element.text_content().strip()

        # Extract just the number
        match = re.search(r'([\d.]+)', rating_text)
        if match:
            return float(match.group(1))
        return 0

    def get_reservation_details(self):
        """Get details from the reservation card"""
        self.page.wait_for_selector(ListingPageLocators.RESERVATION_CARD)

        price_element = self.page.page.locator(ListingPageLocators.RESERVATION_PRICE)
        price_text = price_element.text_content().strip()

        check_in_element = self.page.page.locator(ListingPageLocators.RESERVATION_CHECK_IN)
        check_in_text = check_in_element.text_content().strip()

        check_out_element = self.page.page.locator(ListingPageLocators.RESERVATION_CHECK_OUT)
        check_out_text = check_out_element.text_content().strip()

        guests_element = self.page.page.locator(ListingPageLocators.RESERVATION_GUESTS)
        guests_text = guests_element.text_content().strip().replace("\xa0", " ")

        return {
            'price': price_text,
            'dates': f"{check_in_text} - {check_out_text}",
            'guests': guests_text
        }

    def click_reserve_button(self):
        """Click the reserve button"""
        self.page.click(ListingPageLocators.RESERVE_BUTTON)
        # Wait for the next page to load
        self.page.page.wait_for_timeout(2000)

    def click_continue_button(self):
        """Click the continue button in the reservation flow"""
        self.page.click(ListingPageLocators.CONTINUE_BUTTON)
        self.page.page.wait_for_timeout(2000)
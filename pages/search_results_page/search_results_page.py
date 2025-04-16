from pages.base_page import BasePage
from pages.search_results_page.search_results_page_locators import SearchResultsPageLocators
from pages.search_results_page.search_results_page_actions import SearchResultsPageActions


class SearchResultsPage(BasePage):
    """Search results page object class"""

    def __init__(self, page):
        super().__init__(page)
        self.actions = SearchResultsPageActions(self)
        self.locators = SearchResultsPageLocators

    def validate_search_parameters(self, location, adults, children):
        """Validate that search parameters match the filters"""
        self.logger.info("Validating search parameters")

        # Check location
        displayed_location = self.actions.get_search_location()
        location_valid = location.lower() in displayed_location.lower()
        self.logger.info(f"Location validation: Expected {location}, Found {displayed_location}, Valid: {location_valid}")

        # Check guests
        expected_guests = f"{adults + children} guest"
        if adults + children > 1:
            expected_guests += "s"

        displayed_guests = self.actions.get_search_guests()
        guests_valid = expected_guests in displayed_guests.replace("\xa0", " ")
        self.logger.info(f"Guests validation: Expected {expected_guests}, Found {displayed_guests}, Valid: {guests_valid}")

        return location_valid and guests_valid

    def get_highest_rated_listing(self):
        """Find and return the highest rated listing"""
        self.logger.info("Finding highest rated listing")
        highest_rated = self.actions.find_highest_rated_listing()
        details = self.actions.get_listing_details(highest_rated)
        self.logger.info(f"Highest rated listing: {details}")
        return highest_rated, details

    def get_cheapest_listing(self):
        """Find and return the cheapest listing"""
        self.logger.info("Finding cheapest listing")
        cheapest = self.actions.find_cheapest_listing()
        details = self.actions.get_listing_details(cheapest)
        self.logger.info(f"Cheapest listing: {details}")
        return cheapest, details

    def click_on_listing(self, listing):
        """Click on a listing to view details"""
        self.logger.info("Clicking on listing")
        self.actions.click_listing(listing)

        # Handle new tab
        pages = self.page.context.pages
        listing_page = pages[-1]  # Get the last page (newly opened tab)

        return listing_page
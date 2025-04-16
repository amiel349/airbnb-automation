import re
from pages.search_results_page.search_results_page_locators import SearchResultsPageLocators


class SearchResultsPageActions:
    """Search results page actions"""

    def __init__(self, page_instance):
        self.page = page_instance

    def get_search_location(self):
        """Get the search location from the results page"""
        location_element = self.page.wait_for_selector(SearchResultsPageLocators.SEARCH_LOCATION)
        return location_element.text_content().strip()

    def get_search_dates(self):
        """Get the search dates from the results page"""
        dates_element = self.page.wait_for_selector(SearchResultsPageLocators.SEARCH_DATES)
        return dates_element.text_content().strip()

    def get_search_guests(self):
        """Get the search guests from the results page"""
        guests_element = self.page.wait_for_selector(SearchResultsPageLocators.SEARCH_GUESTS)
        return guests_element.text_content().strip()

    def get_all_listings(self):
        """Get all search result listings"""
        self.page.wait_for_selector(SearchResultsPageLocators.SEARCH_RESULTS)
        listings = self.page.page.locator(SearchResultsPageLocators.SEARCH_RESULTS).all()
        return listings

    def get_listing_price(self, listing):
        """Get the price of a listing"""
        price_element = listing.locator(SearchResultsPageLocators.SEARCH_RESULT_PRICE)
        price_text = price_element.text_content().strip()

        # Extract just the number (remove currency symbol and other text)
        match = re.search(r'([\d,]+)\s*total', price_text)
        if match:
            # Remove commas and convert to integer
            return int(match.group(0).replace(' total', '').replace(",",""))
        return 0

    def get_listing_rating(self, listing):
        """Get the rating of a listing"""
        rating_element = listing.locator(SearchResultsPageLocators.SEARCH_RESULT_RATING)
        if rating_element.count() == 0:
            return 0

        rating_text = rating_element.text_content().strip()
        # Extract just the number (e.g., "4.95" from "4.95 (123)")
        match = re.search(r'([\d.]+)', rating_text)
        if match:
            return float(match.group(1))
        return 0

    def get_listing_title(self, listing):
        """Get the title of a listing"""
        title_element = listing.locator(SearchResultsPageLocators.SEARCH_RESULT_TITLE)
        return title_element.text_content().strip()

    def find_highest_rated_listing(self):
        """Find the listing with the highest rating"""
        listings = self.get_all_listings()
        highest_rating = 0
        highest_rated_listing = None

        for listing in listings:
            rating = self.get_listing_rating(listing)
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_listing = listing

        return highest_rated_listing

    def find_cheapest_listing(self):
        """Find the listing with the lowest price"""
        listings = self.get_all_listings()
        lowest_price = float('inf')
        cheapest_listing = None

        for listing in listings:
            price = self.get_listing_price(listing)
            if price > 0 and price < lowest_price:
                lowest_price = price
                cheapest_listing = listing

        return cheapest_listing

    def get_listing_details(self, listing):
        """Get details of a listing"""
        title = self.get_listing_title(listing)
        price = self.get_listing_price(listing)
        rating = self.get_listing_rating(listing)

        return {
            'title': title,
            'price': price,
            'rating': rating
        }

    def click_listing(self, listing):
        """Click on a listing to view details"""
        listing.click()
        # Wait for new tab to open
        self.page.page.wait_for_timeout(2000)
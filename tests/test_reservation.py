import time

import pytest

from pages.Enums import Country
from pages.confirmation_page.confirmation_page_actions import ConfirmationPage
from pages.popup.popup_page import PopupPage
from tests.base_test import BaseTest
from pages.home_page.home_page import HomePage
from pages.search_results_page.search_results_page import SearchResultsPage
from pages.listing_page.listing_page import ListingPage
from utils.utils import normalize_price, convert_date_range


class TestReservation(BaseTest):
    """Test case for attempting a reservation on Airbnb"""

    def test_reservation_flow(self):
        """Test case #2: Search for apartments and attempt reservation"""
        # Load test data
        test_data = self.load_test_data('reservation_data.json')
        location = test_data['location']
        adults = test_data['adults']
        children = test_data['children']
        phone_number = test_data['phone_number']
        phone_prefix = Country[test_data['phone_prefix']]

        # Initialize pages
        home_page = HomePage(self.page)

        # Navigate to Airbnb and perform search
        self.logger.info("Starting test_reservation_flow")
        home_page.load()
        home_page.search_apartments(location, adults, children)

        # Initialize results page
        search_results_page = SearchResultsPage(self.page)

        # Validate search parameters
        parameters_valid = search_results_page.validate_search_parameters(location, adults, children)
        self.verifier.assert_true(parameters_valid, "Search parameters validation")

        # Find and click on highest rated listing
        highest_rated, highest_rated_details = search_results_page.get_highest_rated_listing()
        self.verifier.assert_true(highest_rated is not None, "Highest rated listing found")

        # Click on the listing and get the new page
        listing_page_handle = search_results_page.click_on_listing(highest_rated)

        # Initialize the listing page with the new page handle
        listing_page = ListingPage(listing_page_handle)
        time.sleep(2)
        popup_page = PopupPage(listing_page_handle)
        if popup_page.present():
            popup_page.close()
        # Get reservation details
        reservation_details = listing_page.get_reservation_card_details()
        self.logger.info(f"Reservation details before attempting reservation: {reservation_details}")

        time.sleep(2)
        if popup_page.present():
            popup_page.close()
        # Attempt reservation
        listing_page.attempt_reservation()

        confirmation_page = ConfirmationPage(listing_page_handle)

        confirmation_page.enter_phone_prefix(phone_prefix)
        confirmation_page.enter_phone_number(phone_number)
        confirmation_details = confirmation_page.get_reservation_details()

        # Verify reservation details match initial details
        self.verifier.verify_equals_with_delta(
            normalize_price(confirmation_details['price']),
            normalize_price(reservation_details['price']),
            "Reservation price validation"
        )
        self.verifier.assert_equals(
            convert_date_range(confirmation_details['dates']),
            reservation_details['dates'],
            "Reservation dates validation"
        )
        self.verifier.assert_equals(
            confirmation_details['guests'],
            reservation_details['guests'],
            "Reservation guests validation"
        )
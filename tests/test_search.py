import pytest
from tests.base_test import BaseTest
from pages.home_page.home_page import HomePage
from pages.search_results_page.search_results_page import SearchResultsPage


class TestSearch(BaseTest):
    """Test case for searching apartments on Airbnb"""

    def test_search_and_analyze_results(self):
        """Test case #1: Search for apartments and analyze results"""
        # Load test data
        test_data = self.load_test_data('search_data.json')
        location = test_data['location']
        adults = test_data['adults']
        children = test_data['children']

        # Initialize pages
        home_page = HomePage(self.page)

        # Navigate to Airbnb and perform search
        self.logger.info("Starting test_search_and_analyze_results")
        home_page.load()
        home_page.search_apartments(location, adults, children)

        # Initialize results page
        search_results_page = SearchResultsPage(self.page)

        # Validate search parameters
        parameters_valid = search_results_page.validate_search_parameters(location, adults, children)
        self.verifier.assert_true(parameters_valid, "Search parameters validation")

        # Find highest rated listing
        highest_rated, highest_rated_details = search_results_page.get_highest_rated_listing()
        self.verifier.assert_true(highest_rated is not None, "Highest rated listing found")
        self.logger.info(f"Highest rated listing details: {highest_rated_details}")

        # Find cheapest listing
        cheapest, cheapest_details = search_results_page.get_cheapest_listing()
        self.verifier.assert_true(cheapest is not None, "Cheapest listing found")
        self.logger.info(f"Cheapest listing details: {cheapest_details}")
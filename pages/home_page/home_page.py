from pages.base_page import BasePage
from pages.home_page.home_page_locators import HomePageLocators
from pages.home_page.home_page_actions import HomePageActions


class HomePage(BasePage):
    """Home page object class"""

    def __init__(self, page):
        super().__init__(page)
        self.actions = HomePageActions(self)
        self.locators = HomePageLocators
        self.url = "https://www.airbnb.com/"

    def load(self):
        """Load the home page"""
        self.navigate(self.url)
        return self

    def search_apartments(self, destination, adults=2, children=0, check_in_date=None, check_out_date=None):
        """Search for apartments with the given parameters"""
        self.logger.info(f"Searching for apartments in {destination} for {adults} adults and {children} children")

        # Open search form
        self.actions.open_search_form()

        # Enter destination
        self.actions.enter_destination(destination)

        # Select dates
        self.actions.select_dates(check_in_date, check_out_date)

        # Select guests
        self.actions.select_guests(adults, children)

        # Submit search
        self.actions.submit_search()

        return self
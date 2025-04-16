import time
from datetime import datetime, timedelta
from pages.home_page.home_page_locators import HomePageLocators


class HomePageActions:
    """Home page actions"""

    def __init__(self, page_instance):
        self.page = page_instance

    def open_search_form(self):
        """Open the search form"""
        self.page.click(HomePageLocators.SEARCH_BUTTON)
        self.page.wait_for_selector(HomePageLocators.SEARCH_DESTINATION_INPUT)

    def enter_destination(self, destination):
        """Enter the destination in the search field"""
        self.page.fill(HomePageLocators.SEARCH_DESTINATION_INPUT, destination)
        # Wait for the autocomplete dropdown to appear
        self.page.page.wait_for_timeout(1000)

        # Press Enter to select the autocomplete suggestion
        self.page.page.keyboard.press("Enter")

    def select_dates(self, check_in_date=None, check_out_date=None):
        """Select check-in and check-out dates"""
        # If dates are not provided, generate arbitrary dates (one month from now)
        if not check_in_date:
            today = datetime.now()
            check_in_date = today + timedelta(days=30)
            check_out_date = check_in_date + timedelta(days=3)

        # Format dates as strings
        if isinstance(check_in_date, datetime):
            check_in_date = check_in_date.strftime("%Y-%m-%d")
        if isinstance(check_out_date, datetime):
            check_out_date = check_out_date.strftime("%Y-%m-%d")

        # Click on date field to open calendar
        self.page.click(HomePageLocators.SEARCH_DATE_FIELD)

        # Navigate to the correct month
        self.navigate_to_date_month(check_in_date)

        # Select check-in date
        self.select_date_from_calendar(check_in_date)

        # Select check-out date
        self.select_date_from_calendar(check_out_date)

    def navigate_to_date_month(self, date_str):
        """Navigate to the month containing the provided date"""
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        target_month_year = target_date.strftime("%B %Y")

        # Check if we need to navigate forward
        visible_month_element = self.page.page.locator("//div[@aria-label='Calendar']//h2").first
        visible_month = visible_month_element.text_content()

        while target_month_year not in visible_month:
            self.page.click(HomePageLocators.CALENDAR_NEXT_MONTH)
            self.page.page.wait_for_timeout(500)
            visible_month = self.page.page.locator("//div[@aria-label='Calendar']//h2").first.text_content()

    def select_date_from_calendar(self, date_str):
        """Select a specific date from the calendar"""
        day_element = self.page.page.locator(HomePageLocators.CALENDAR_DAYS.format(date_str))
        if day_element:
            day_element.click()


    def select_guests(self, adults=2, children=0):
        """Select the number of guests"""
        # Click on guests button to open selection
        self.page.click(HomePageLocators.SEARCH_GUESTS_BUTTON)

        # Set adults count
        current_adults = int(self.page.page.locator(HomePageLocators.ADULTS_COUNTER).text_content())
        for _ in range(adults - current_adults):
            self.page.click(HomePageLocators.ADULTS_INCREASE)

        # Set children count
        if children > 0:
            for _ in range(children):
                self.page.click(HomePageLocators.CHILDREN_INCREASE)

    def submit_search(self):
        """Submit the search form"""
        self.page.click(HomePageLocators.SEARCH_SUBMIT_BUTTON)
        time.sleep(2)
class HomePageLocators:
    """Home page locators"""
    # Search form elements
    SEARCH_BUTTON = "[data-testid='structured-search-input-field-query']"
    SEARCH_DESTINATION_INPUT = "input[data-testid='structured-search-input-field-query']"
    SEARCH_DATE_FIELD = "div[data-testid='structured-search-input-field-dates-panel']"
    SEARCH_CHECKIN_INPUT = "div[data-testid='structured-search-input-field-split-dates-0']"
    SEARCH_CHECKOUT_INPUT = "div[data-testid='structured-search-input-field-split-dates-1']"
    SEARCH_GUESTS_BUTTON = "[data-testid='structured-search-input-field-guests-button']"

    # Calendar elements
    CALENDAR_NEXT_MONTH = "button[aria-label='Move forward to switch to the next month.']"
    CALENDAR_DAYS = "button[data-state--date-string='{}']"

    # Guest selection elements
    ADULTS_COUNTER = "span[data-testid='stepper-adults-value']"
    ADULTS_INCREASE = "button[data-testid='stepper-adults-increase-button']"
    CHILDREN_COUNTER = "span[data-testid='stepper-children-value']"
    CHILDREN_INCREASE = "button[data-testid='stepper-children-increase-button']"

    # Submission elements
    SEARCH_SUBMIT_BUTTON = "button[data-testid='structured-search-input-search-button']"
class SearchResultsPageLocators:
    """Search results page locators"""
    # Results list
    SEARCH_RESULTS = "div[data-testid='card-container']"
    SEARCH_RESULT_PRICE = "div[data-testid='price-availability-row']"
    SEARCH_RESULT_RATING = "div[data-testid='price-availability-row']+div"
    SEARCH_RESULT_TITLE = "div[data-testid='listing-card-title']"

    # Search parameters validation
    SEARCH_LOCATION = "button[data-testid='little-search-location']"
    SEARCH_DATES = "button[data-testid='little-search-anytimes']"
    SEARCH_GUESTS = "button[data-testid='little-search-guests']"

    # Filter buttons
    FILTER_BUTTON = "button[data-testid='filter-button']"
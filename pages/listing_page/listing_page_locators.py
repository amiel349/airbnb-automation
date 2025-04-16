class ListingPageLocators:
    """Listing page locators"""
    # Listing details
    LISTING_TITLE = "h1[data-testid='listing-title']"
    LISTING_PRICE = "div[data-testid='listing-price']"
    LISTING_RATING = "div[data-testid='listing-rating']"

    # Reservation card
    RESERVATION_CARD = "div[data-section-id='BOOK_IT_SIDEBAR']"
    RESERVATION_PRICE = "//div[normalize-space(text())='Total']/../..//span[@aria-hidden]/span"
    RESERVATION_CHECK_IN = "div[data-testid='change-dates-checkIn']"
    RESERVATION_CHECK_OUT = "div[data-testid='change-dates-checkOut']"
    RESERVATION_GUESTS = "div[id='GuestPicker-book_it-trigger']"
    RESERVE_BUTTON = "//div[@data-section-id='BOOK_IT_SIDEBAR']//button[@data-testid='homes-pdp-cta-btn']"

    # Reservation flow
    PHONE_INPUT = "input[data-testid='phone-number-input']"
    CONTINUE_BUTTON = "button[data-testid='continue-button']"
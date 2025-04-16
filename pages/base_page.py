from playwright.sync_api import Page
from utils.logger import Logger


class BasePage:
    """Base page class that all page objects will inherit from"""

    def __init__(self, page: Page):
        self.page = page
        self.logger = Logger().get_logger()

    def navigate(self, url: str):
        """Navigate to the specified URL"""
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the title of the current page"""
        title = self.page.title()
        self.logger.info(f"Page title: {title}")
        return title

    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for a selector to be visible"""
        self.logger.info(f"Waiting for selector: {selector}")
        return self.page.wait_for_selector(selector, timeout=timeout)

    def wait_for_navigation(self):
        """Wait for navigation to complete"""
        self.logger.info("Waiting for navigation to complete")
        self.page.wait_for_load_state("networkidle")

    def get_element_text(self, selector: str) -> str:
        """Get text content of an element"""
        element = self.page.locator(selector)
        text = element.text_content()
        self.logger.info(f"Element text: {text}")
        return text

    def click(self, selector: str):
        """Click on an element"""
        self.logger.info(f"Clicking on element: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        """Fill a form field"""
        self.logger.info(f"Filling {selector} with value: {value}")
        self.page.fill(selector, value)

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible"""
        is_visible = self.page.locator(selector).is_visible()
        self.logger.info(f"Element {selector} is visible: {is_visible}")
        return is_visible
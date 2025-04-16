import os
import json
import pytest
from playwright.sync_api import Page
from utils.logger import Logger
from utils.verifier import Verifier


class BaseTest:
    """Base test class that all test classes will inherit from"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Set up test environment"""
        self.page = page
        self.logger = Logger().get_logger()
        self.verifier = Verifier()

        # Configure browser for consistent behavior
        self.page.set_viewport_size({"width": 1280, "height": 800})
        self.page.set_default_timeout(30000)

        # Yield control to the test
        yield

        # Teardown (can be extended as needed)
        self.logger.info("Test completed")

    def load_test_data(self, filename):
        """Load test data from JSON file"""
        data_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
        self.logger.info(f"Loading test data from {data_file_path}")

        with open(data_file_path, 'r') as file:
            data = json.load(file)

        return data
# Airbnb Test Automation with Pytest & Playwright

This project implements automated tests for the Airbnb website using Pytest and Playwright as part of the Axonius Automation Developer Interview Task.

## Project Structure

The project follows the Page Object Model (POM) design pattern and is organized as follows:

```
airbnb-automation/
│
├── pages/                              # Page objects
│   ├── base_page.py                    # Base page class
│   ├── home_page/                      # Home page components
│   ├── search_results_page/           # Search results page components
│   ├── listing_page/                   # Listing page components
│   ├── confirmation_page/           # Confirmation page object
│   └── popup_page/                  # Popup components
│
├── tests/                              # Test cases
│   ├── base_test.py                    # Base test class
│   ├── test_search.py                  # Test case #1
│   └── test_reservation.py            # Test case #2
│
├── utils/                              # Utility modules
│   ├── logger.py                       # Logging utilities
│   ├── verifier.py                     # Verification utilities
│   ├── enums/                          # Enum definitions
│   │   └── country_enum.py             # Example enum (e.g. Country)
│
├── data/                               # Test data
│   ├── search_data.json                # Data for test case #1
│   └── reservation_data.json           # Data for test case #2
│
├── conftest.py                         # Pytest configuration
├── requirements.txt                    # Project dependencies
└── README.md                           # Project documentation

```

## Features

- Page Object Model design pattern
- Base page class for common functionality
- Component-based page objects (locators, actions, page)
- Custom logging and verification utilities
- Data-driven testing using JSON files
- Comprehensive test cases following the required steps

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd airbnb-automation
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running the Tests

To run all tests:
```bash
pytest
```

To run a specific test:
```bash
pytest tests/test_search.py
```

To run tests with detailed output:
```bash
pytest -v
```

To run tests with Browser open:
```bash
pytest --headed
```

To generate an HTML report:
```bash
pytest --html=reports/report.html
```

## Configuration

You can modify the test data in the JSON files located in the `data` directory:

- `search_data.json`: Configuration for the search test
- `reservation_data.json`: Configuration for the reservation test

## Logging

Logs are stored in the `logs` directory. The default log level is INFO, but you can change it by setting the `LOG_LEVEL` environment variable.

## Notes

- The tests are set to run in headed mode by default (visible browser). You can change this in `conftest.py` by setting `headless: True`.
- The tests include a slight delay (`slow_mo`) to make the automation visible. Remove this for production use.
- The phone number in the reservation test is a placeholder. Update it in `reservation_data.json` if needed.
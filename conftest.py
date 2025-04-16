import os
import pytest
from playwright.sync_api import sync_playwright

os.makedirs("logs", exist_ok=True)

# Create test reports directory if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Create directories for traces and videos
os.makedirs("traces", exist_ok=True)
os.makedirs("videos", exist_ok=True)

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Return browser launch arguments"""
    return {
        "headless": False,  # Set to True for CI/CD pipeline
        "slow_mo": 100,  # Slow down execution for better visualization (remove in production)
    }


@pytest.fixture
def page(browser_type_launch_args):
    """Create and return a browser page"""
    with sync_playwright() as playwright:
        # Launch browser (Chrome/Chromium)
        browser = playwright.chromium.launch(**browser_type_launch_args)

        # Create a new browser context with tracing and video
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            record_video_dir="videos/",  # Enable video recording
        )

        # Start tracing
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        # Create a new page in the context
        page = context.new_page()

        # Set default timeout for all operations
        page.set_default_timeout(30000)

        yield page

        # Save trace to a file (named after the test)
        test_name = os.environ.get("PYTEST_CURRENT_TEST", "").split(":")[-1].split(" ")[0]
        context.tracing.stop(path=f"traces/{test_name or 'test'}.zip")

        # Close context and browser
        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to set test name for tracing"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        # Set test name environment variable for tracing
        os.environ["PYTEST_CURRENT_TEST"] = item.nodeid
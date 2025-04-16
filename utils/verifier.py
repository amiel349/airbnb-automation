from utils.logger import Logger


class Verifier:
    """Utility class for verifications and assertions"""

    def __init__(self):
        self.logger = Logger().get_logger()

    def verify_equals(self, actual, expected, message=""):
        """Verify that actual equals expected"""
        assertion_message = f"{message} - Expected: {expected}, Actual: {actual}"

        if actual == expected:
            self.logger.info(f"✅ Verification PASSED: {assertion_message}")
            return True
        else:
            self.logger.error(f"❌ Verification FAILED: {assertion_message}")
            return False

    def verify_equals_with_delta(self, actual:int, expected:int, message="", delta=1):
        """Verify that actual equals expected"""
        assertion_message = f"{message} - Expected: {expected}, Actual: {actual}"

        if abs(expected - actual) <= delta:
            self.logger.info(f"✅ Verification PASSED: {assertion_message}")
            return True
        else:
            self.logger.error(f"❌ Verification FAILED: {assertion_message}")
            return False

    def verify_contains(self, container, item, message=""):
        """Verify that container contains item"""
        assertion_message = f"{message} - Expected container to contain: {item}"

        if item in container:
            self.logger.info(f"✅ Verification PASSED: {assertion_message}")
            return True
        else:
            self.logger.error(f"❌ Verification FAILED: {assertion_message}")
            return False

    def verify_true(self, condition, message=""):
        """Verify that condition is True"""
        if condition:
            self.logger.info(f"✅ Verification PASSED: {message}")
            return True
        else:
            self.logger.error(f"❌ Verification FAILED: {message}")
            return False

    def verify_false(self, condition, message=""):
        """Verify that condition is False"""
        if not condition:
            self.logger.info(f"✅ Verification PASSED: {message}")
            return True
        else:
            self.logger.error(f"❌ Verification FAILED: {message}")
            return False

    def assert_equals(self, actual, expected, message=""):
        """Assert that actual equals expected"""
        assertion_message = f"{message} - Expected: {expected}, Actual: {actual}"

        if actual == expected:
            self.logger.info(f"✅ Assertion PASSED: {assertion_message}")
        else:
            self.logger.error(f"❌ Assertion FAILED: {assertion_message}")
            assert actual == expected, assertion_message

    def assert_contains(self, container, item, message=""):
        """Assert that container contains item"""
        assertion_message = f"{message} - Expected container to contain: {item}"

        if item in container:
            self.logger.info(f"✅ Assertion PASSED: {assertion_message}")
        else:
            self.logger.error(f"❌ Assertion FAILED: {assertion_message}")
            assert item in container, assertion_message

    def assert_true(self, condition, message=""):
        """Assert that condition is True"""
        if condition:
            self.logger.info(f"✅ Assertion PASSED: {message}")
        else:
            self.logger.error(f"❌ Assertion FAILED: {message}")
            assert condition, message

    def assert_false(self, condition, message=""):
        """Assert that condition is False"""
        if not condition:
            self.logger.info(f"✅ Assertion PASSED: {message}")
        else:
            self.logger.error(f"❌ Assertion FAILED: {message}")
            assert not condition, message
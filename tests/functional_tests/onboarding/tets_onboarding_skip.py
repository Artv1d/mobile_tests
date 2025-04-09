import unittest
import time
from drivers.appium_driver import create_driver
from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage

class OnboardingScreenTests(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()
        self.onboarding = OnboardingPage(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_skip_on_first_screen(self):
        """Тест кнопки 'Skip' на первом экране"""
        self.assertTrue(self.onboarding.is_skip_button_visible())
        self.onboarding.tap_skip()
        time.sleep(2)

        # Проверяем, что открылся главный экран
        self.assertTrue(self.onboarding.is_main_screen_visible())

    def test_skip_on_second_screen(self):
        """Тест кнопки 'Skip' на втором экране"""
        # Переход на второй экран
        self.onboarding.tap_continue()
        time.sleep(1)

        # Проверяем кнопку Skip
        self.assertTrue(self.onboarding.is_skip_button_visible())
        self.onboarding.tap_skip()
        time.sleep(2)

        # Проверяем, что открылся главный экран
        self.assertTrue(self.onboarding.is_main_screen_visible())

    def test_skip_on_third_screen(self):
        """Тест кнопки 'Skip' на третьем экране"""
        # Переход на третий экран
        for _ in range(2):
            self.onboarding.tap_continue()
            time.sleep(1)

        # Проверяем кнопку Skip
        self.assertTrue(self.onboarding.is_skip_button_visible())
        self.onboarding.tap_skip()
        time.sleep(2)

        # Проверяем, что открылся главный экран
        self.assertTrue(self.onboarding.is_main_screen_visible())

if __name__ == "__main__":
    unittest.main()
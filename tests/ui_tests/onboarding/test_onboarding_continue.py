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

    def test_continue_through_all_screens(self):
        """Тестирование кнопки 'Continue' на всех экранах онбординга"""
        for _ in range(3):  # Нажимаем Continue 3 раза (после 3-го должен быть 4-й экран)
            self.assertTrue(self.onboarding.is_continue_button_visible())
            self.onboarding.tap_continue()
            time.sleep(1)  # Пауза для перехода на новый экран

        # Проверяем, что мы на последнем экране (должна быть кнопка "Get Started")
        self.assertTrue(self.onboarding.is_get_started_visible())

if __name__ == "__main__":
    unittest.main()
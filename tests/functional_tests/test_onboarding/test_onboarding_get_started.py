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

    def test_get_started_button(self):
        """Тестирование кнопки 'Get Started' на последнем экране"""
        for _ in range(3):  # Пропускаем первые 3 экрана
            self.onboarding.tap_continue()
            time.sleep(1)

        self.assertTrue(self.onboarding.is_get_started_visible())
        self.onboarding.tap_get_started()
        time.sleep(2)  # Ждем перехода на главный экран

        # Проверяем, что открылся главный экран
        self.assertTrue(self.onboarding.is_main_screen_visible())
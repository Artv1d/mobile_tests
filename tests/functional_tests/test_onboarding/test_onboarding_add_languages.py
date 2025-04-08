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

    def test_add_or_edit_languages(self):
        """Тестирование кнопки 'Add or edit languages' и навигации"""

        self.assertTrue(self.onboarding.is_add_language_button_visible(), "Кнопка 'Add or edit languages' не отображается")
        self.onboarding.tap_add_language_button()

        # Проверяем, что открылся экран выбора языка
        self.assertTrue(self.onboarding.is_language_screen_visible(), "Экран добавления языка не открылся")

        # Нажимаем на кнопку "Add language"
        self.assertTrue(self.onboarding.is_add_language_in_list_visible(), "Кнопка 'Add language' не отображается")
        self.onboarding.tap_add_language_in_list()
        time.sleep(2)

        # Возвращаемся на экран выбора языка с помощью кнопки "Navigate up"
        self.assertTrue(self.onboarding.is_navigate_up_visible(), "Кнопка 'Navigate up' не отображается")
        self.onboarding.tap_navigate_up()

        # Возвращаемся на первый экран онбординга с помощью кнопки "Navigate up"
        self.assertTrue(self.onboarding.is_navigate_up_visible(), "Кнопка 'Navigate up' не отображается")
        self.onboarding.tap_navigate_up()

        # Проверяем, что вернулись на первый экран онбординга (проверка наличия кнопки Continue)
        self.assertTrue(self.onboarding.is_continue_button_visible())

if __name__ == "__main__":
    unittest.main()
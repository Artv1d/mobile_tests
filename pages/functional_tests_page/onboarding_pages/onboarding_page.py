from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnboardingPage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    # Protected Locators
    _CONTINUE_BTN_ID = "org.wikipedia.alpha:id/fragment_onboarding_forward_button"
    _GET_STARTED_BTN_ID = "org.wikipedia.alpha:id/fragment_onboarding_done_button"
    _SKIP_BIN_ID = "org.wikipedia.alpha:id/fragment_onboarding_skip_button"
    _ADD_LANGUAGE_BTN_ID = "org.wikipedia.alpha:id/addLanguageButton"
    _LANGUAGE_SCREEN_TITLE_ID = "org.wikipedia.alpha:id/toolbar"
    _MAIN_SCREEN_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout"
    _ADD_LANGUAGE_XPATH = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/wiki_language_title' and @text='Add language']"
    _NAVIGATE_UP_XPATH = "//android.widget.ImageButton[@content-desc='Navigate up']"

    def tap_continue(self):
        btn = self.driver.find_element(AppiumBy.ID, self._CONTINUE_BTN_ID)
        btn.click()

    def tap_skip(self):
        btn = self.driver.find_element(AppiumBy.ID, self._SKIP_BIN_ID)
        btn.click()

    def tap_get_started(self):
        self.driver.find_element(AppiumBy.ID, self._GET_STARTED_BTN_ID).click()

    def tap_add_language_button(self):
        btn = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, self._ADD_LANGUAGE_BTN_ID)))
        btn.click()

    def tap_add_language_in_list(self):
        btn = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self._ADD_LANGUAGE_XPATH)))
        btn.click()

    def tap_navigate_up(self):
        btn = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self._NAVIGATE_UP_XPATH)))
        btn.click()

    def is_main_screen_visible(self):
        return self.driver.find_element(AppiumBy.XPATH, self._MAIN_SCREEN_XPATH).is_displayed()

    def is_skip_button_visible(self):
        return self.driver.find_element(AppiumBy.ID, self._SKIP_BIN_ID).is_displayed()

    def is_get_started_visible(self):
        return self.driver.find_element(AppiumBy.ID, self._GET_STARTED_BTN_ID).is_displayed()

    def is_continue_button_visible(self):
        return self.driver.find_element(AppiumBy.ID, self._CONTINUE_BTN_ID).is_displayed()

    def is_add_language_button_visible(self):
        return self.driver.find_element(AppiumBy.ID, self._ADD_LANGUAGE_BTN_ID).is_displayed()

    def is_language_screen_visible(self):
        return self.driver.find_element(AppiumBy.ID, self._LANGUAGE_SCREEN_TITLE_ID).is_displayed()

    def is_add_language_in_list_visible(self):
        return self.driver.find_element(AppiumBy.XPATH, self._ADD_LANGUAGE_XPATH).is_displayed()

    def is_navigate_up_visible(self):
        return self.driver.find_element(AppiumBy.XPATH, self._NAVIGATE_UP_XPATH).is_displayed()
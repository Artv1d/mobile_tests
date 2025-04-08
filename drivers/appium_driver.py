from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.settings import Config

def create_driver():
    """Создает и возвращает драйвер Appium"""
    options = UiAutomator2Options()
    options.platform_name = Config.PLATFORM_NAME
    options.automation_name = Config.AUTOMATION_NAME
    options.device_name = Config.DEVICE_NAME
    options.app = Config.APP_PATH
    options.app_package = Config.APP_PACKAGE
    options.app_activity = Config.APP_ACTIVITY

    driver = webdriver.Remote(Config.APPIUM_SERVER_URL, options=options)
    return driver
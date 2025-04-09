class Config:
    """Конфигурация проекта"""

    # Адрес Appium-сервера
    APPIUM_SERVER_URL = "http://localhost:4723"

    # Путь к APK-файлу
    APP_PATH = "/Users/user/StudioProjects/apps-android-wikipedia/app/build/outputs/apk/alpha/debug/app-alpha-debug.apk"

    # Настройки Appium
    PLATFORM_NAME = "Android"
    AUTOMATION_NAME = "uiautomator2"
    DEVICE_NAME = "emulator-5554"
    LANGUAGE = "en"
    LOCALE = "US"

    # Пакет и активности
    APP_PACKAGE = "org.wikipedia.alpha"
    APP_ACTIVITY = "org.wikipedia.main.MainActivity"

    # Другие активности
    ACTIVITIES = {
        "main": "org.wikipedia.main.MainActivity",
        "search": "org.wikipedia.search.SearchActivity",
        "page": "org.wikipedia.page.PageActivity",
        "settings": "org.wikipedia.settings.SettingsActivity",
        "reading_list": "org.wikipedia.readinglist.ReadingListActivity",
        "about": "org.wikipedia.about.AboutActivity",
        "test": "leakcanary.internal.activity.LeakActivity",
    }
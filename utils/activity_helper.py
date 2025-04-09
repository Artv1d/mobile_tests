from config.settings import Config

class ActivityHelper:
    """Утилита для управления активностями"""

    @staticmethod
    def get_current_activity(driver):
        """Получить текущую активность"""
        print(driver.current_activity)
        return driver.current_activity

    @staticmethod
    def switch_to_activity(driver, activity_name):
        """Переключиться на указанную активность"""
        if activity_name in Config.ACTIVITIES:
            print(f"Запуск активности: {Config.ACTIVITIES[activity_name]}")
            driver.start_activity(Config.APP_PACKAGE, Config.ACTIVITIES[activity_name])
            print("Активность успешно запущена.")
        else:
            raise ValueError(f"Активность '{activity_name}' не найдена в Config.ACTIVITIES")

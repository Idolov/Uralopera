from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    """Страница логина"""

    E_MAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    PHONE_INPUT = (By.ID, "phone")
    LOGIN_BUTTON = (By.CSS_SELECTOR,
                    "#app > div.authmodal.is-not-authed > div > div.column.customer_wrapper > div > div > form > div > div:nth-child(4) > div:nth-child(1) > button > div > span")

    # Добавляем константы для элементов проверки
    SUCCESS_MESSAGE = (By.CLASS_NAME, "has-text-success")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#app > div.authmodal.is-not-authed > a")
    USER_ICON = (By.CSS_SELECTOR,
                 "#app > header > div > div > div.__column-menu.column.is-8.has-text-right > div > a:nth-child(2) > svg")
    REGISTER_TAB = (By.CSS_SELECTOR,
                    "#app > div.authmodal.is-not-authed > div > div.column.customer_wrapper > div > div > form > div > div.tabs.is-boxed.is-fullwidth > ul > li:nth-child(2) > a > span")
    USER_PROFILE = (By.CSS_SELECTOR,
                    "#app > div.authmodal.is-authed > div > div.content_wrapper.column.is-7 > div > div > div > h3")
    PROFILE_CLOSE = (By.CSS_SELECTOR,
                     "#app > div.authmodal.is-authed > div > div.column.customer_wrapper > div > div > a")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href*='logout']")  # Добавляем селектор для кнопки выхода

    def open_login_page(self):
        self.open("https://uralopera.ru/")

    def registrat(self, email, password, first_name, last_name, phone):
        print(f"Регистрируем пользователя: {email}")
        self.type(self.E_MAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.PHONE_INPUT, phone)
        self.click(self.LOGIN_BUTTON)
        time.sleep(5)

        # Получаем ТЕКСТ сообщения об успехе
        success_text = self.get_text(self.SUCCESS_MESSAGE)
        print(f"Текст сообщения об успехе: '{success_text}'")
        self.click(self.CLOSE_BUTTON)
        return success_text

    def regist(self):
        print("Открываем форму регистрации")
        self.click(self.USER_ICON)
        time.sleep(2)
        self.click(self.REGISTER_TAB)
        time.sleep(2)

    def login(self):
        print("Открываем форму логина")
        self.click(self.USER_ICON)
        time.sleep(2)

    def good_login(self, email, password):
        print(f"Пытаемся залогиниться: {email}")
        self.type(self.E_MAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(5)

        # Получаем ТЕКСТ профиля пользователя
        try:
            profile_text = self.get_text(self.USER_PROFILE)
            print(f"Текст профиля: '{profile_text}'")
        except Exception as e:
            print(f"Ошибка при получении текста профиля: {e}")
            # Делаем скриншот для отладки
            self.driver.save_screenshot("login_error.png")
            profile_text = ""

        self.click(self.PROFILE_CLOSE)
        return profile_text

    def logout(self):
        """Метод для разлогина"""
        print("Выполняем разлогин")
        try:
            # Кликаем на иконку пользователя (теперь она должна открывать меню для залогиненного пользователя)
            self.click(self.USER_ICON)
            time.sleep(2)

            # Пытаемся найти и кликнуть кнопку выхода
            # Возможно, нужно будет настроить селектор в зависимости от реальной структуры сайта
            logout_btn = (By.XPATH, "//a[contains(text(), 'Выйти') or contains(text(), 'Logout')]")
            self.click(logout_btn)
            time.sleep(2)
            print("✓ Успешный разлогин")
        except Exception as e:
            print(f"Не удалось разлогиниться стандартным способом: {e}")
            # Альтернативный способ - очистка cookies и перезагрузка
            self.driver.delete_all_cookies()
            self.open_login_page()
            print("✓ Разлогин через очистку cookies")
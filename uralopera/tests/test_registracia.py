import pytest
from conftest import *
from pages.registracia_page import LoginPage
import time


def test_successful_login(driver):
    login_page = LoginPage(driver)

    # Тестируем регистрации
    test_registration_data = [
        ("Cepaxp+test116@mail.ru", "123321", "Иван", "Петров", "+79095678901"),
        ("Cepaxp+test117@mail.ru", "124456", "Павел", "Гаврилов", "+79193456723"),
        ("Cepaxp+test118@mail.ru", "123123", "Анна", "Якина", "+79123459708"),
        ("Cepaxp+test119@mail.ru", "123321", "Сергей", "Закиров", "+79095678901")
    ]

    for email, password, first_name, last_name, phone in test_registration_data:
        print(f"\n=== Регистрация пользователя: {email} ===")
        login_page.open_login_page()
        time.sleep(3)
        login_page.regist()
        time.sleep(3)

        result_text = login_page.registrat(email, password, first_name, last_name, phone)
        assert result_text == 'На вашу электронную почту был отправлен код подтверждения.'
        print("✓ Регистрация успешна")
        time.sleep(3)

    # Тестируем логины
    print("\n=== Тестируем логины ===")

    # Первый логин
    login_page.open_login_page()
    time.sleep(3)
    login_page.login()
    time.sleep(2)

    result_login = login_page.good_login("Cepaxp@mail.ru", "123321")
    print(f"Результат логина: '{result_login}'")
    assert result_login != "", "Логин не удался - текст профиля пустой"
    print("✓ Первый логин успешен")

    # Разлогиниваемся перед вторым логином
    login_page.logout()
    time.sleep(3)

    # Второй логин
    login_page.open_login_page()
    time.sleep(3)
    login_page.login()
    time.sleep(2)

    result_login2 = login_page.good_login("Cepaxp2008@mail.ru", "123321")
    print(f"Результат второго логина: '{result_login2}'")
    assert result_login2 != "", "Второй логин не удался - текст профиля пустой"
    print("✓ Второй логин успешен")

    # Разлогиниваемся в конце теста
    login_page.logout()
    print("✓ Тест завершен успешно")

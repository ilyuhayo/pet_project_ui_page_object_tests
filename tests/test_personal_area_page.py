import pytest
from conftest import browser
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_area_page import PersonalAreaPage


class TestPersonalAreaPage:
    def test_click_on_personal_area_button(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site("https://stellarburgers.nomoreparties.site/")
        main_page.click_personal_area_button()
        assert main_page.get_current_url() == "https://stellarburgers.nomoreparties.site/login"

    def test_go_to_order_history_section(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site("https://stellarburgers.nomoreparties.site/")
        main_page.click_personal_area_button()
        login_page = LoginPage(browser)
        login_page.input_email_field()
        login_page.input_password_field()
        login_page.click_enter_button()
        main_page.click_personal_area_button()
        personal_area_page = PersonalAreaPage(browser)
        personal_area_page.click_order_history_section_button()
        assert personal_area_page.get_current_url() == "https://stellarburgers.nomoreparties.site/account/order-history"

    def test_exit_from_account(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site("https://stellarburgers.nomoreparties.site/")
        main_page.click_personal_area_button()
        login_page = LoginPage(browser)
        login_page.input_email_field()
        login_page.input_password_field()
        login_page.click_enter_button()
        main_page.click_personal_area_button()
        personal_area_page = PersonalAreaPage(browser)
        personal_area_page.click_exit_from_account_button()
        login_page.wait_for_login_form()
        assert login_page.get_current_url() == "https://stellarburgers.nomoreparties.site/login"


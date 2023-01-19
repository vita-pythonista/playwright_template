import time
import allure

from pages.main_page import MainPage


@allure.parent_suite('UI Тесты')
@allure.suite('Пробные тесты')
@allure.sub_suite('Проверка сайта python.org')
class TestPythonOrg:

    def test_1(self, page):

        main = MainPage(page)
        main.open()
        time.sleep(2)
        main.scroll_to_footer()
        time.sleep(3)
        main.scroll_to_doc_widget()
        main.click_url_into_doc_widget()
        time.sleep(3)
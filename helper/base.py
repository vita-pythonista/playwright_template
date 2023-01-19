import allure
import pytest
from playwright.sync_api import Locator, Page, expect
from pydantic.typing import List

TIMEOUT = 3 * 1000

class Base:

    def __init__(self, page):
        self.page = page

    @allure.step("Ожидание полной загрузки DOM-дерева")
    def wait_state_dom_tree(self) -> None:
        """Ожидание отсутствия активных сетевых соединений на странице"""
        self.page.wait_for_load_state('domcontentend')

    @allure.step("Получение веб-элемента после поиска на странице")
    def find_element(self, selector: str, timeout=TIMEOUT) -> Locator:
        """Найти элемент на странице с помощью локатора"""
        element = self.page.locator(selector)
        element.wait_for(state='attached', timeout=timeout) # прикреплен к DOM-дереву
        element.wait_for(timeout=timeout) # виден на странице
        try:
            with allure.step(f"Ожидаем появления элемента на странице с селектором {selector}"):
                expect(element).to_be_visible()
        except TimeoutError:
            self.wait_state_dom_tree()
        return element

    @allure.step("Получение списка веб-элементов после поиска на странице")
    def find_elements(self, selector) -> List:
        """Найти список элементов с помощью общего локатора"""
        elements = self.page.query_selector_all(selector)
        if not len(elements):
            with pytest.raises(Exception):
                pass
        return elements

    @allure.step("Нажатие на кликабельный веб-элемент")
    def click(self, selector, timeout=TIMEOUT) -> None:
        """Нажать на веб-элемент"""
        element = self.find_element(selector, timeout)
        element.click()

    def scroll_down_to_element(self, selector, timeout=TIMEOUT):
        """Прокрутить страницу вниз к элементу"""
        element = self.find_element(selector, timeout)
        element.scroll_into_view_if_needed()

    def scroll_up(self):
        """Прокрутить наверх страницы"""
        self.page.press('body', key='Home')
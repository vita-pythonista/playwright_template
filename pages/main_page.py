import allure

from helper.base import Base
from settings import settings


class Footer:

    footer_links = ".footer-links"

class MainContent:

    doc_widget = ".small-widget.documentation-widget"
    url_doc_widget = ".small-widget.documentation-widget a[href='https://docs.python.org']"

class MainPage(Base):

    def __init__(self, page):
        super().__init__(page)
        self.footer = Footer()
        self.main_content = MainContent()

    @allure.step('Открыть страницу python.org')
    def open(self):
        self.page.goto(settings.BASE_URL)

    def scroll_to_footer(self):
        self.scroll_down_to_element(self.footer.footer_links)

    def scroll_to_doc_widget(self):
        self.scroll_up()
        self.scroll_down_to_element(self.main_content.doc_widget)

    def click_url_into_doc_widget(self):
        self.click(self.main_content.url_doc_widget)
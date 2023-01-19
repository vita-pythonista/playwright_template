import allure
import pytest


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page) -> None:
    """Скриншот при падении теста"""
    yield
    if request.node.rep_call.failed:
        all_tabs = page.context.pages
        for i in range(len(all_tabs)):
            allure.attach(
                all_tabs[i].screenshot(),
                name=f"screenshot_{request.function.__name__}_tab_{i}",
                attachment_type=allure.attachment_type.PNG,
                )


@pytest.fixture(autouse=True)
def current_url_on_failure(request, page) -> None:
    """Прикладывает текущий url страницы при падении теста"""
    yield
    if request.node.rep_call.failed:
        allure.attach(page.url, name=request.function.__name__, attachment_type=allure.attachment_type.TEXT)
import pytest
from selene.support.shared import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture()
def browser_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')

    yield
    browser.quit()


@pytest.fixture()
def browser_mobile():
    browser.config.window_width = 1000
    browser.config.window_height = 2532
    browser.open('https://github.com')
    yield
    browser.quit()


def test_github_desktop(browser_mobile):
    browser.element("//button[@aria-label='Toggle navigation' and @data-view-component='true']").click()
    browser.element("//a[@href='/login']").click()


def test_github_mobile(browser_desktop):
    browser.element("//a[@href='/login']").click()

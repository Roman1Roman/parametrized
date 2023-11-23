"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=['desktop_1', 'mobile_1', 'desktop_2', 'mobile_2'])
def browser_scale(request):
    if request.param == 'desktop_1':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com')
    elif request.param == 'desktop_2':
        browser.config.window_width = 1280
        browser.config.window_height = 720
        browser.open('https://github.com')
    elif request.param == 'mobile_1':
        browser.config.window_width = 1000
        browser.config.window_height = 2532
        browser.open('https://github.com')
    elif request.param == 'mobile_2':
        browser.config.window_width = 1000
        browser.config.window_height = 2200
        browser.open('https://github.com')


@pytest.mark.parametrize('browser_scale', ["desktop_2"], indirect=True)
def test_open_github_parametrized_desktop(browser_scale):
    browser.element("//a[@href='/login']").click()


@pytest.mark.parametrize('browser_scale', ["mobile_1"], indirect=True)
def test_open_github_parametrized_mobile(browser_scale):
    browser.element("//button[@aria-label='Toggle navigation' and @data-view-component='true']").click()
    browser.element("//a[@href='/login']").click()

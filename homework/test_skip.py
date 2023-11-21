"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=['desktop_1', 'desktop_2', 'mobile_1', 'mobile_2'], scope='function')
def browser_config(request):
    if request.param == 'desktop_1':
        browser.config.window_height = 1080
        browser.config.window_width = 1920
        return request.param
    elif request.param == 'desktop_2':
        browser.config.window_height = 720
        browser.config.window_width = 1280
        browser.open('https://github.com')
        return request.param
    elif request.param == 'mobile_1':
        browser.config.window_height = 2532
        browser.config.window_width = 1000
        browser.open('https://github.com')
        return request.param
    elif request.param == 'mobile_2':
        browser.config.window_height = 2200
        browser.config.window_width = 1000
        browser.open('https://github.com')

    #browser.open('https://github.com')
    #return request.param
    yield
    browser.quit()


@pytest.mark.skipif('browser_config == "mobile_1" or browser_config == "mobile_2"',
                    reason="mobile scale not for desktop")
def test_github_desktop(browser_config):
    # if browser_config == 'mobile_1' or browser_config == 'mobile_2':
    #     pytest.skip(reason='mobile scale not for desktop')
    browser.element("//a[@href='/login']").click()


@pytest.mark.skipif('browser_config == "desktop_1" or browser_config == "desktop_2"',
                    reason="desktop scale not for mobile")
def test_github_mobile(browser_config):
    # if browser_config.param == 'desktop_1' or browser_config.param == 'desktop_2':
    #     pytest.skip(reason='desktop scale not for mobile')
    browser.element("//button[@aria-label='Toggle navigation' and @data-view-component='true']").click()
    browser.element("//a[@href='/login']").click()

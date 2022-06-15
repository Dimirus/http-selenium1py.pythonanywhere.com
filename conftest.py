import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#add parameter default language of page
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
        help="Choose language: es = Spanish, en = British English, fr = French, ru = Russian, uk = Ukrainian, de = Deutsch, it = Italiano")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
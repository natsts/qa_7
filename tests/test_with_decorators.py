import allure
from selene.support.shared import browser
from selene import have
from allure_commons.types import Severity
from allure_commons.types import AttachmentType

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "natsts")
@allure.feature("Issue in repository")
@allure.story("Issue 'Issue for allure' has in repository")
@allure.link("https://github.com", name="Testing")

def test_with_decorators(size_browser):
    open_general_page()
    search_repository('natsts/qa_7')
    search_issue()
    check_issue('Issue for allure')
    add_attach()

@allure.step('Ореn general page')
def open_general_page():
    browser.open('https://github.com')

@allure.step('Search repository')
def search_repository(repo):
    browser.element('.header-search-input').click().type(repo).press_enter()
    browser.element('[href="/natsts/qa_7"]').click()

@allure.step('Search issue')
def search_issue():
    browser.element('#issues-tab').click()

@allure.step('Check text of issue')
def check_issue(text):
    browser.element('#issue_1_link').should(have.text(text))

@allure.step('Make screenshot')
def add_attach():
    allure.attach(browser.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)

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

def test_with_allure_step(size_browser):
    browser.open('https://github.com')

    browser.element('.header-search-input').click().type('natsts/qa_7').press_enter()
    browser.element('[href="/natsts/qa_7"]').click()

    browser.element('#issues-tab').click()

    browser.element('#issue_1_link').should(have.text('Issue for allure'))

    allure.attach(browser.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)

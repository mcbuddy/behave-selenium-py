from behave import *
from selenium import *

@given(u'I at google search homepage')
def step_impl(context):
    context.browser.get("https://google.com/")

@when(u'I search for "behave" keyword')
def step_impl(context):
    context.browser.find_element_by_id('lst-ib').send_keys("behave.py")
    context.browser.find_element_by_name("btnK").click()

@then(u'I should see "behave" search result')
def step_impl(context):
    assert context.browser.find_element_by_id('resultStats').is_displayed()
    behave_result_path = '//*[@id="rso"]/div/div/div[1]/div/div/h3/a'
    assert context.browser.find_element_by_xpath(behave_result_path).text == "Tutorial — behave 1.2.5 documentation - PythonHosted.org"
    context.browser.find_element_by_xpath(behave_result_path).click()

@then(u'I should see "behave" official homepage')
def step_impl(context):
    assert context.browser.title == "Welcome to behave! — behave 1.2.5 documentation"
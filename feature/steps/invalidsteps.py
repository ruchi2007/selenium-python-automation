from behave import given, when, then
#import logging as log
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('i go to login page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)
    print("i go to login page")
    # log.info("i go to login page")
    # assert 1 == 1


@when('i enter invalid username')
def invalid_username(context):
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    context.driver.find_element_by_xpath(username).send_keys("abc")
    print('i enter invalid username')


@when('i enter invalid password')
def invalid_password(context):
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    context.driver.find_element_by_xpath(password).send_keys("admin12345")
    print('i enter invalid password')


@when('i click submit button')
def submit_button(context):
    submit_btn = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    context.driver.find_element_by_xpath(submit_btn).click()
    print('i click submit button')


@then('i should see error message')
def error_message(context):
    print("i should see error message")
    error_message = context.driver.find_element_by_xpath(
        "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
    assert "Invalid credentials" in error_message

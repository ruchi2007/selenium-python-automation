from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('i go to home page')
def home_page(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    print('i go to home page')


@when('i click logout_icon')
def click_logout_icon(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
    print('i click logout_icon')


@when('i click logout_button')
def click_logout_button(context):
    context.driver.find_element_by_xpath('//*[@id=\'app\']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
    print('i click logout_button')


@then('i should see login page')
def login_page(context):
    print('i should see login page')
    assert context.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

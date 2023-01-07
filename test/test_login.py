# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# import pytest
#
#
# @pytest.fixture()
# def test_setup():
#     global driver
#     url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
#     driver.get(url)
#     driver.implicitly_wait(1000)
#
#     yield
#     driver.close()
#     driver.quit()
#
#
# def test_login_successfully(test_setup):
#     username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
#     password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
#     login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
#     driver.find_element_by_xpath(username).send_keys("Admin")
#     driver.find_element_by_xpath(password).send_keys("admin123")
#     driver.find_element_by_xpath(login).click()
#     expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
#     actual_url = driver.current_url
#     driver.save_screenshot("image.png")
#     assert expected_url == actual_url
#     print(driver.current_url)
#     title = driver.title
#     assert title == "OrangeHRM"
#
#
# def test_verify_user_should_not_login_with_invalid_credential(test_setup):
#     username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
#     password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
#     login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
#     driver.find_element_by_xpath(username).send_keys("abc")
#     driver.find_element_by_xpath(password).send_keys("admin123")
#     driver.find_element_by_xpath(login).click()
#     error_message = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
#     assert "Invalid credentials" in error_message

# def test_closebrowser():
#     driver.close()
#     driver.quit()

from src.testproject.sdk.drivers import webdriver
from src.testproject.decorator import report


@report(project="FirstMobileProj", job="pytest example", test="Basic flow on TestProject demo app")
def test_firstem():
    desired_capabilities = {
        "appActivity": "io.testproject.demo.MainActivity",
        "appPackage": "io.testproject.demo",
        "udid": "emulator-5554",
        "browserName": "",
        "platformName": "Android",
    }

    driver = webdriver.Remote(desired_capabilities=desired_capabilities)
    driver.find_element_by_id('name').send_keys('John Smith')
    driver.find_element_by_id('password').send_keys('12345')
    driver.find_element_by_id('login').click()
    driver.close_app()
    driver.quit()

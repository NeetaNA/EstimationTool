from Locators.LoginLocators import LoginLocators
from Locators.AllEstimationsLocators import AllEstimationsLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.CommonFunctions import CommonFunctions


class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_xpath = LoginLocators.username_textbox_xpath
        self.password_textbox_xpath = LoginLocators.password_textbox_xpath
        self.login_button_xpath = LoginLocators.login_button_xpath
        self.create_new_estimation_xpath=AllEstimationsLocators.create_new_estimation_button_xpath
        self.login_failure_message_xpath=LoginLocators.login_fail_message_xpath

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        commonobj=CommonFunctions()
        url=commonobj.get_value_from_conf_file('configuration.properties','URL')
        try:
            EC.url_to_be('url')
        except TimeoutException:
            print("Home page is taking tool long to load completely")

    def verify_successful_login(self):
        try:
            self.driver.find_element_by_xpath(self.create_new_estimation_xpath)
            print "Login successful"
        except NoSuchElementException:
            print "Login failed"

    def verify_login_failure(self):
        # driver=self.driver
        # try:
        #     element=EC.presence_of_element_located(By.XPATH,self.login_failure_message_xpath)
        #     WebDriverWait(driver,20).until(element)
        try:
            self.driver.find_element_by_xpath(self.login_failure_message_xpath)
            print "Login failure message verified successfully"
        except NoSuchElementException:
            print "Login failure message not found"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.CommonFunctions import CommonFunctions
import unittest


class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        commonobj = CommonFunctions()
        url=str(commonobj.get_value_from_conf_file('configuration.properties','URL'))
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_valid_login(self):
        #Get valid login credentials from file
        commonobj=CommonFunctions()
        username=str(commonobj.get_value_from_conf_file('login.credentials','VALID_LOGIN_USER'))
        password=str(commonobj.get_value_from_conf_file('login.credentials','VALID_LOGIN_PASSWORD'))
        driver=self.driver
        loginobj=LoginPage(driver)
        loginobj.enter_username(username)
        loginobj.click_login()
        loginobj.enter_password(password)
        loginobj.click_login()
        loginobj.verify_successful_login()

    def test_invalid_login(self):
        #Get invalid login credentials from file
        commonobj=CommonFunctions()
        username=str(commonobj.get_value_from_conf_file('login.credentials','INVALID_LOGIN_USER'))
        password=str(commonobj.get_value_from_conf_file('login.credentials','INVALID_LOGIN_PASSWORD'))
        driver=self.driver
        loginobj=LoginPage(driver)
        loginobj.enter_username(username)
        loginobj.click_login()
        loginobj.enter_password(password)
        loginobj.click_login()
        loginobj.verify_login_failure()

    def tearDown(self):
        self.driver.close()


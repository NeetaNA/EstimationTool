class LoginLocators():

    username_textbox_xpath = "//input[@id='username']"
    password_textbox_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@type='submit' and span='Continue']"
    login_fail_message_xpath="//div[@type='error' and contains(text(),'Invalid username or password')]"


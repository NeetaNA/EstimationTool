from Locators.AllEstimationsLocators import AllEstimationsLocators


class AllEstimations():

    def __init__(self,driver):
        self.driver=driver
        self.create_new_estimation_button_xpath=AllEstimationsLocators.create_new_estimation_button_xpath



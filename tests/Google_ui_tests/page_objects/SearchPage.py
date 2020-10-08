from selenium import webdriver

from Helpers.CommonActions import waiting_appearing

BASE_URL = 'https://www.google.com/'
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.get(BASE_URL)


class SearchPage:

    SEARCH_INPUT = "//input[@type='text']"
    SEARCH_BUTTON = "//input[@value='Поиск в Google']"
    SEARCH_RESULT_FIRST_LINK = "//div[@class='g']//a"
    CURRENT_WEATHER = "//div[@class='cur-con-weather-card__panel']"

    def input_search_data(self, search_data):
        driver.find_element_by_xpath(self.SEARCH_INPUT).send_keys(search_data)

    def click_search(self):
        waiting_appearing(driver, self.SEARCH_BUTTON)
        driver.find_element_by_xpath(self.SEARCH_BUTTON).click()

    def open_first_link(self):
        waiting_appearing(driver, self.SEARCH_RESULT_FIRST_LINK)
        driver.find_element_by_xpath(self.SEARCH_RESULT_FIRST_LINK).click()

    def get_results(self):
        waiting_appearing(driver, self.CURRENT_WEATHER)
        return driver.find_element_by_xpath(self.CURRENT_WEATHER).text

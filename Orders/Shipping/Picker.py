# Import the necessary modules for development
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Login:
    username = "azmul"
    password = "Admin@123"


class ChromePicker(unittest.TestCase, Login):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_picker(self):
        driver_chrome = self.driver
        driver_chrome.get('https://staging-encore.brandedonline.com/Login')
        driver_chrome.find_element_by_name("username").send_keys(self.username)
        driver_chrome.find_element_by_name("password").send_keys(self.password)
        driver_chrome.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/form/button").click()
        time.sleep(6)
        #chrome_options = Options()
        #chrome_options.add_argument("--disable-notification")
        #driver_chrome = webdriver.Chrome(chrome_options=chrome_options)

        # Go to Order Shipping
        driver_chrome.get("https://staging-encore.brandedonline.com/vapps/oms/Shipping/dashboard")
        time.sleep(7)
        driver_chrome.find_element_by_css_selector("#content > div > div > div > div > div > div.row > div:nth-child(1) > a:nth-child(1)").click()
        time.sleep(5)
        driver_chrome.find_element_by_css_selector("#PicklistList_workEffortId_2_picklistDetail").click()
        time.sleep(5)
        driver_chrome.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/a[2]").click()
        time.sleep(10)
        #driver_chrome.save_screenshot('screenshot-Chrome.png')


class FirefoxPicker(unittest.TestCase, Login):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    def test_picker_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('https://staging-encore.brandedonline.com/Login')
        driver_firefox.find_element_by_name("username").send_keys(self.username)
        driver_firefox.find_element_by_name("password").send_keys(self.password)
        driver_firefox.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
        time.sleep(5)

        # Go to Order Shipping
        driver_firefox.get("https://staging-encore.brandedonline.com/vapps/oms/Shipping/dashboard")
        time.sleep(7)
        driver_firefox.find_element_by_xpath("//a[normalize-space()='Picklists']").click()
        time.sleep(7)
        driver_firefox.find_element_by_xpath("//a[normalize-space()='100357:']").click()
        time.sleep(6)
        driver_firefox.find_element_by_xpath("//a[normalize-space()='Picklist and Pack PDF']").click()
        # driver_chrome.save_screenshot('screenshot-Chrome.png')
        driver_firefox = webdriver.FirefoxProfile()
        download_dir = "C:/Users/Muhammad Azmul Haq/Downloads"
        driver_firefox.set_preference("browser..download.folderList",2)
        driver_firefox.set_preference("browser.download.dir", download_dir)
        driver_firefox.set_preference("browser.download.manager.showWhenStarting", False)
        driver_firefox.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

    def teardown(self):
        # self.driver.implicitly_wait(10)
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

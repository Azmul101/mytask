from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class browsers():
        def browsersName(self):
            browsercap = "chrome"
            if browsercap == "chrome":
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            elif browsercap == "firefox":
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            elif browsercap == "safari":
                self.driver = webdriver.Safari()
            else:
                print("Please pass the correct browser name :" + browsercap)
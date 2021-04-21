from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import logging, os


### HOOKS ###

### Before Tests ###

def before_feature(self, feature):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe",
                                   chrome_options=chrome_options)


### After Tests ###

def after_step(self, step):
    if step.status == "failed":
        try:
            os.makedirs("./screenshots/")
            logging.info("Folder screenshots created")
        except:
            logging.info("Folder screenshots exist")

        logging.error(f"STEP FAILED: {step}")
        self.driver.save_screenshot("./screenshots/error-step2.png")



def after_feature(self, feature):
    self.driver.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
import clipboard
import time


class DeepL_Translator:

    def __init__(self, driver=webdriver.Chrome()):
        self.driver = driver
        self.driver.get("https://www.deepl.com/translator")

        self.input_css = 'div.lmt__inner_textarea_container textarea'
        self.input_field = self.driver.find_element('css selector', self.input_css)

        self.cookiebanner()

        # self.button_xpath = '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/div[' \
        #                     '2]/span[2]/span/span/button'
        self.copy_css = 'div.lmt__target_toolbar__copy button'

    def translate(self, text):
        self.input_field.clear()
        self.input_field.send_keys(text)

        WebDriverWait(self.driver, 10).until(cond.element_to_be_clickable(('xpath',
            '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/span[1]/span/span/button')))
        time.sleep(1)

        copy = self.driver.find_element('css selector', self.copy_css)
        copy.click()

        output_text = clipboard.paste()
        return output_text

    def cookiebanner(self):
        cookie_xpath = '//*[@id="dl_cookieBanner"]/div/div/div/span/div[2]/button[1]'
        cookie_button = self.driver.find_element('xpath', cookie_xpath)
        cookie_button.click()

    def __del__(self):
        self.driver.quit()

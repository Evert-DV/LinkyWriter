from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
import clipboard
import time


class DeepL_Translator:
    """Uses a Selenium webdriver to acces the free online DeepL webpage and translate text."""

    def __init__(self, driver=webdriver.Chrome()):
        # Set up the webdriver
        self.driver = driver

        # Access the webpage
        self.driver.get("https://www.deepl.com/translator")

        # Find the input text area in the html code of the page
        self.input_css = 'div.lmt__inner_textarea_container textarea'
        self.input_field = self.driver.find_element('css selector', self.input_css)

        # Click away the cookie banner
        self.cookie_banner()

        # Define the 'copy translation' button location from the html code
        self.copy_xpath = '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/div[2]/span[' \
                          '2]/span/span/button'

    def translate(self, text):
        # Clear the text input field and send the text to translate
        self.input_field.clear()
        self.input_field.send_keys(text)

        # Wait until the copy button appears (i.e. the translation is finished)
        WebDriverWait(self.driver, 30).until(cond.element_to_be_clickable(('xpath',
                                                                           '//*[@id="panelTranslateText"]/div[1]/div['
                                                                           '2]/section[2]/div[3]/div[6]/div/div/span[1]'
                                                                           '/span/span/button')))
        time.sleep(1)

        # Click the copy button, translation is now on clipboard
        copy = self.driver.find_element('xpath', self.copy_xpath)
        copy.click()

        # Get the translated text
        output_text = clipboard.paste()
        return output_text

    def cookie_banner(self):
        # Locate the 'accept' button on the cookie banner and click it
        cookie_xpath = '//*[@id="dl_cookieBanner"]/div/div/div/span/div[2]/button[1]'
        cookie_button = self.driver.find_element('xpath', cookie_xpath)
        cookie_button.click()

    def __del__(self):
        # Destructor
        self.driver.quit()

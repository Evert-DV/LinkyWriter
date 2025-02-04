from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
import clipboard
import time
import base64


class DeepL_Translator:
    """
    Uses a Selenium webdriver to acces the free online DeepL webpage and translate text.
    """
    def __init__(self, driver=webdriver.Chrome()):
        # Set up the webdriver
        self.input_field = None
        self.driver = driver

        # Access the webpage
        self.driver.get("https://www.deepl.com/nl/login/")

        # Login
        self.login()

        # Click away the cookie banner
        self.cookie_banner()

        # Click the "use free services" button
        free_xpath = '//*[@id="headlessui-dialog-panel-2"]/div/div/button'
        free_button = self.driver.find_element('xpath', free_xpath)
        free_button.click()


        # Find the input text area in the html code of the page
        self.input_css = 'div.lmt__inner_textarea_container textarea'
        
        # Define the 'copy translation' and 'listen' button location from the html code
        self.copy_xpath = '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/div[2]/span[' \
                          '2]/span/span/button'
        self.listen_xpath = '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/span[1]' \
                            '/span/span/button'

    def translate(self, text):
        # find input field
        WebDriverWait(self.driver, 5).until(cond.presence_of_element_located(('css selector', self.input_css)))
        self.input_field = self.driver.find_element('css selector', self.input_css)
        
        # Clear the text input field and send the text to translate
        self.input_field.clear()
        self.input_field.send_keys(text)

        # Wait until the 'listen' button appears (i.e. the translation is finished)
        WebDriverWait(self.driver, 30).until(cond.element_to_be_clickable(('xpath', self.listen_xpath)))
        WebDriverWait(self.driver, 5).until(cond.presence_of_element_located(('xpath', self.copy_xpath)))
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
        WebDriverWait(self.driver, 10).until(cond.element_to_be_clickable(('xpath', cookie_xpath)))
        cookie_button = self.driver.find_element('xpath', cookie_xpath)
        cookie_button.click()

    def login(self):
        email_xpath = '//*[@id="gatsby-focus-wrapper"]/div/main/form/label[1]/div[1]/div/div[2]/input'
        password_xpath = '//*[@id="gatsby-focus-wrapper"]/div/main/form/label[2]/div[1]/div/div[2]/input'

        WebDriverWait(self.driver, 5).until(cond.presence_of_element_located(('xpath', email_xpath)))

        email_field = self.driver.find_element('xpath', email_xpath)
        password_field = self.driver.find_element('xpath', password_xpath)

        with open("credentials.txt", 'r') as c:
            contents = c.read()

        email_field.send_keys("evertdevroey@gmail.com")
        password_field.send_keys(base64.b64decode(contents[1:]).decode("utf-8"))
        password_field.send_keys("\n")


    def __del__(self):
        # Destructor
        self.driver.quit()

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Change the following constants based on your requirements
TARGET_ACCOUNT = "target_username"
YOUR_USERNAME = "your_username"
YOUR_PASSWORD = "your_password"

class InstagramBot:

    def __init__(self):
        # Open the browser with an option to detach
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    # Log in to Instagram account
    def login(self):
        login_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(login_url)
        time.sleep(4.2)

        # Dismiss the cookie warning if present
        cookie_warning_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, cookie_warning_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        # Find and fill in the username and password fields
        username_field = self.driver.find_element(by=By.NAME, value="username")
        password_field = self.driver.find_element(by=By.NAME, value="password")

        username_field.send_keys(YOUR_USERNAME)
        password_field.send_keys(YOUR_PASSWORD)

        time.sleep(2.1)
        password_field.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" to ignore the Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # Click "Not Now" on the notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    # Find followers of a specified Instagram account
    def find_followers(self):
        time.sleep(5)
        # Open the followers page of the target account
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers")

        time.sleep(8.2)
        # Update the modal xpath as it may change over time
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for _ in range(5):
            # Scroll through the followers' modal
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    # Follow users from the list
    def follow(self):
        # Check and update the CSS Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Handle the case where clicking on a button triggers a dialog (e.g., Unfollow/Cancel)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

# Create an instance of the InstagramBot class and perform actions
insta_bot = InstagramBot()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

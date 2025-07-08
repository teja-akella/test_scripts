import os
from ssl import Options
import yaml
import pytest

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="session")
def credentials(request):
    path = request.config.getoption("--credentials")
    if not path:
        path = os.path.join(os.path.dirname(__file__), "credentials.yaml")
        with open(path, "r") as f:
            return yaml.safe_load(f)

@pytest.fixture(scope="function")
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    # Teardown: close the browser after tests
    driver.quit()

def test_login(setup,credentials):
    driver = setup
    # with open('../tests/credentials.yaml', 'r') as file:
    #     credentials = yaml.safe_load(file)

        #step 1: Open the browser and navigate to the login page
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 30)
        
        #step 2: Enter the username and password
    email = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")

    email.send_keys(credentials['qa_username'])
    password.send_keys(credentials['qa_password'])

        #step 3: Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Login']/..")))

    login_button.click()

        #step 4: Wait for the page to load and verify the login was successful
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Welcome to 101GenAI!']")))
    assert "Welcome to 101GenAI!" in driver.page_source, "Login failed or page did not load correctly."
    print("Login successful!")
    time.sleep(2)



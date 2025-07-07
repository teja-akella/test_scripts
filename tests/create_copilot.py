#tests_for_create_copilot.py

import pytest
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from utils import login, setup
def test_create_copilot(setup):
    driver = setup
    wait = WebDriverWait(driver, 30)

    # Step 1: Login to the application
    login(setup)
    copilot_input = driver.find_element(By.XPATH, "//textarea")
    copilot_input.send_keys("You are an agent that talk about a patient who suffered from Bipolar disorder. You are a medical expert and you will answer the questions about the patient. And support emotional support to the patient by integrate the data from mood journals, wearable devices, and other sources to provide personalized insights and recommendations. You will also help the patient to manage their condition by providing information about treatment options, coping strategies, and self-care techniques. You will also help the patient to understand their condition better by providing information about the causes, symptoms, and treatment of Bipolar disorder.")
    copilot_input.send_keys(Keys.ENTER)
    time.sleep(10)

    # Step 2: Check and verify the Copilot creation
    continue_button =wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='text-white py-2 px-4 text-sm font-medium rounded-md bg-pink-dark']")))
    time.sleep(5)
    continue_button.click()
    

    #step 3: Naming the Copilot
    wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='What do you want to name your copilot?']" )))
    copilot_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//button[5]")))
    copilot_name_input.click()
    time.sleep(5)

    #step 4: Selecting the avatar
    wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Pick an avatar for your copilot?']")))
    avatar_button = driver.find_element(By.XPATH, "//img[@alt='Copilot Avatar test-image-id-4']")
    avatar_button.click()

    # step 5: Building the Copilot
    build_copilot_button = driver.find_element(By.XPATH, "//div[contains(@class,'border-grey-bg-med///button[contains(@class,'text-white py-2 px-4 text-sm font-medium rounded-md bg-pink-dark')]")
    build_copilot_button.click()


from dearpygui.core import *
from dearpygui.simple import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
PATH = "C:\Program Files (x86)\chromedriver.exe"
env_path = '.\\venv\.env'
load_dotenv(dotenv_path=env_path)
MY_ROUTER_IP = os.getenv('MY_ROUTER_IP')
_USERNAME = os.getenv('_USERNAME')
_PASSWORD = os.getenv('_PASSWORD')
driver = '' # set a value IDE shows undefined variable even if I set it at global
qos_on_radio = ''
qos_off_radio = ''



def init_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.headless = False
    global driver
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get(MY_ROUTER_IP)
    

def login_and_navigation():
    try:
        loginbutton = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'logIn'))
        )
    finally:
        loginbutton.click()
        print('Found Log In Button and clicked')

    username = driver.find_element_by_id('Frm_Username')
    password = driver.find_element_by_id('Frm_Password')
    submit = driver.find_element_by_id('LoginId')

    username.clear()
    username.send_keys(_USERNAME)
    password.clear()
    password.send_keys(_PASSWORD)
    submit.click()
    print('Logged In')

    try:
        internet_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'mmInternet'))
        )
    finally:
        internet_button.click()
        print('Found Internet Button and clicked')


    try:
        qos_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'smAdminQos'))
        )
 
    finally:
        qos_button.click()
        print('Found QoS Button and clicked')



def qos_state():
    # qos_state returns boolean if selected or not, tuple
    global qos_on_radio, qos_off_radio
    
    qos_on_radio = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'Enable1'))
    )
    qos_on_radio_state = qos_on_radio.is_selected()

  
    qos_off_radio = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'Enable0'))
    )
    qos_off_radio_state = qos_off_radio.is_selected()

    qos_state_tuple = (qos_on_radio_state, qos_off_radio_state)
    # (False, True): 'Off', (True, False): 'On
    return qos_state_tuple


def click_radio_on():
    qos_on_radio.click()
    apply_button = driver.find_element_by_id('Btn_apply_QoSBasicCfg').click()
    print('QoS On')


def click_radio_off():
    qos_off_radio.click()
    apply_button = driver.find_element_by_id('Btn_apply_QoSBasicCfg').click()
    print('QoS Off')


def gui():
    # add main window
    # add text for QoS state if on off
    # add radio button, try to make the button grey out or selected if already on (ie if True, True radio button is selected or cant be selected)
    # Submit button
    # Text "QoS is not set to {radiobutton state}
    pass

def main():
    start_dearpygui()


init_driver()
login_and_navigation()
before_qos_state = qos_state()
print(before_qos_state)
click_radio_off()
after_qos_state = qos_state()
print(after_qos_state)




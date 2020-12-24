from dearpygui.core import *
from dearpygui.simple import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
PATH = "C:\Program Files (x86)\chromedriver.exe"
env_path = '.\\venv\.env'
load_dotenv(dotenv_path=env_path)
MY_ROUTER_IP = os.getenv('MY_ROUTER_IP')
_USERNAME = os.getenv('_USERNAME')
_PASSWORD = os.getenv('_PASSWORD')
driver = '' # set a value IDE shows undefined variable even if I set it at global
import time
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.headless = False
    global driver
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get(MY_ROUTER_IP)
    

def login():
    loginbutton = driver.find_element_by_id('logIn')
    loginbutton.click()

    username = driver.find_element_by_id('Frm_Username')
    password = driver.find_element_by_id('Frm_Password')
    submit = driver.find_element_by_id('LoginId')

    username.clear()
    username.send_keys(_USERNAME)
    password.clear()
    password.send_keys(_PASSWORD)
    submit.click()


def qos_state():
    time.sleep(1)
    internet_button = driver.find_element_by_id('mmInternet')
    internet_button.click()

    time.sleep(1)
    qos_button = driver.find_element_by_id('smAdminQos')
    qos_button.click()

    # variable for QoS on or off state examples below
    # use isSelected() pr getAttribute()
    # String str = driver.findElement(By.id("26110162")).getAttribute("checked");
    # driver.findElement(By.id("26110162")).isSelected();


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
login()
qos_state()
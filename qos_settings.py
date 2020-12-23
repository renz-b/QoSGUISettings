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

def __init__():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.headless = False
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get(MY_ROUTER_IP)
    

def qos_state():
    # variable for QoS on or off state examples below
    # use isSelected() pr getAttribute()
    # String str = driver.findElement(By.id("26110162")).getAttribute("checked");
    # driver.findElement(By.id("26110162")).isSelected();
    pass

def gui():
    # add main window
    # add text for QoS state if on off
    # add radio button, try to make the button grey out or selected if already on (ie if True, True radio button is selected or cant be selected)
    # Submit button
    # Text "QoS is not set to {radiobutton state}
    pass

def main():
    start_dearpygui()


__init__()
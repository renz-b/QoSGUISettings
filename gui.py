from dearpygui.core import *
from dearpygui.simple import *
import qos_settings


def click_on(sender, data):
    qos_settings.click_radio_on()
    log_debug('qos on has been clicked...')


def click_off(sender,data):
    qos_settings.click_radio_off()
    log_debug('qos off has been clicked...')


# def check_current_settings(sender, data, settings_history=[]):
#     try:
#         delete_item('text1')
#         delete_item('text')
#     except:
#         print('idk')
#     if settings_history == []:
#         settings_history.append(current)
#         state = current
#     elif settings_history[-1] == 0:
#         state = 1
#     elif settings_history[-1] == 1:
#         state = 0
#     add_text('text1', parent='Main', default_value=f'Current: {state}')


set_main_window_pos(800,400)
set_main_window_size(320, 160)
set_theme('Light')
set_style_window_padding(15,15)


with window('Main'):
    print('Main window runnning...')
    add_text('Running')
    show_logger()
    qos_settings.init_driver()
    log_debug('Page loaded...')
    qos_settings.login_and_navigation()
    log_debug('Logging in..')
    log_debug('Navigating page...')
    # current = qos_settings.qos_state()
    # add_text('text', default_value=f'Current setting is: {current}')
    add_text('Qos settings: ')
    add_spacing(count=1)
    add_separator()
    add_spacing(count=1)
    add_button('On', callback=click_on)
    add_button('Off', callback=click_off)
    add_spacing(count=4)
    # add_button('Check', callback=check_current_settings)
    

start_dearpygui(primary_window='Main')


from dearpygui.core import *
from dearpygui.simple import *

state = 0

show_debug()
show_logger()


set_main_window_pos(800,400)
set_main_window_size(320, 160)
set_theme('Black')
set_style_window_padding(15,15)

def click(sender, data):
    pass

with window('Main'):
    print('Main window runnning...')
    add_text('Qos settings: ')
    add_radio_button('qos_radio', items=['Off', 'On'], horizontal=True, default_value=state, callback=lambda sender,data: log_debug('radio'))
    add_spacing(count=4)
    add_separator()
    add_spacing(count=2)
    add_button('Apply', callback= lambda sender,data: log_debug(f'{sender}, {data}')) # wrong


start_dearpygui(primary_window='Main')


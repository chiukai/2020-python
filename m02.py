# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        display.show('Hello, chiukai')
        
        
    if button_b.is_pressed():
        display.show(Image.RABBIT)
        
        
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.MUSIC_CROTCHET)
"""
Created by: Isaac Ip
Created on: Sep 2025
This module is a Micro:bit MicroPython program
This program turns an LED on and off
"""

from microbit import *

display.clear()
display.show(Image.HAPPY)

while True:
    # turns the LED on
    if button_a.is_pressed():
        display.clear()
        display.show(Image.YES)
        pin16.write_digital(1)

    # turns the LED off
    if button_b.is_pressed():
        display.clear()
        display.show(Image.NO)
        pin16.write_digital(0)

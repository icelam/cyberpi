"""
A simple program writtens with Python.
Listens to CyberPi click events and convert them to mouse events on computer.

Only works on "Run" mode.

Instructions:
CyberPi Joystick = Mouse move
CyberPi Button "B" = Mouse click
CyberPi Button "A" = Mouse Right click
CyberPi Button "B" + Joystick = Mouse scroll
"""

import time
import cyberpi
from pynput.mouse import Button, Controller

def print_instructions():
    """Print instructions"""
    cyberpi.console.println("Joystick - Move, △ - Click, □: Right click, △ + JoyStick - Scroll")

def start_controller():
    """Start listening to cyberpi events and control mouse correspondingly"""
    mouse = Controller()

    cyberpi.led.show("white white white white white")

    while True:
        is_scrolling = False
        is_moving = False
        is_left_clicked = False
        is_right_clicked = False

        if cyberpi.controller.is_press("b") and cyberpi.controller.is_press("up"):
            mouse.scroll(0, 1)
            is_scrolling = True
        elif cyberpi.controller.is_press("b") and cyberpi.controller.is_press("down"):
            mouse.scroll(0, -1)
            is_scrolling = True
        elif cyberpi.controller.is_press("b") and cyberpi.controller.is_press("left"):
            mouse.scroll(1, 0)
            is_scrolling = True
        elif cyberpi.controller.is_press("b") and cyberpi.controller.is_press("right"):
            mouse.scroll(-1, 0)
            is_scrolling = True
        elif cyberpi.controller.is_press("up"):
            mouse.move(0, -3)
            is_moving = True
        elif cyberpi.controller.is_press("down"):
            mouse.move(0, 3)
            is_moving = True
        elif cyberpi.controller.is_press("left"):
            mouse.move(-3, 0)
            is_moving = True
        elif cyberpi.controller.is_press("right"):
            mouse.move(3, 0)
            is_moving = True
        elif cyberpi.controller.is_press("b"):
            mouse.press(Button.left)
            mouse.release(Button.left)
            is_right_clicked = True
        elif cyberpi.controller.is_press("a"):
            mouse.press(Button.right)
            mouse.release(Button.right)
            is_right_clicked = True

        if is_scrolling or is_moving or is_left_clicked or is_right_clicked:
            print(
                "X: " + str(mouse.position[0]) + ", " \
                "Y: " + str(mouse.position[1]) + ", " \
                "Is moving: " + str(is_moving) + ", " \
                "Is scrolling: " + str(is_scrolling) + ", " \
                "Left click: " + str(is_left_clicked) + ", " \
                "Right click: " + str(is_right_clicked)
            )

        time.sleep(0.01)

if __name__ == '__main__':
    print_instructions()
    start_controller()

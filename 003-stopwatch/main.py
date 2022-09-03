"""
A simple stopwatch program written in microPython that allows pause and resume of timer.
"""

import event, time, cyberpi

WELCOME_MESSAGE = "Stopwatch\n\n△: Start\n○: Pause\n□: Reset"
LED_EFFECT_STEPS = 4

is_timer_started = False
previous_time = 0

"""
Welcome screen
"""
@event.start
def on_start():
    global seconds, minutes, hours

    cyberpi.display.show_label(WELCOME_MESSAGE, 16, "center")

"""
Reset stopwatch
"""
@event.is_press("a")
def is_button_a_press():
    global is_timer_started, previous_time

    if is_timer_started:
        cyberpi.stop_other()
        is_timer_started = False
        cyberpi.led.off(0)
        previous_time = 0
        cyberpi.display.show_label(WELCOME_MESSAGE, 16, "center")

"""
Pause stopwatch
"""
@event.is_press("middle")
def is_button_middle_press():
    global is_timer_started, previous_time

    if is_timer_started:
        cyberpi.stop_other()
        is_timer_started = False
        previous_time = cyberpi.timer.get()
        cyberpi.led.off(0)

"""
Start stopwatch
"""
@event.is_press("b")
def is_button_b_press():
    global is_timer_started, previous_time

    if not is_timer_started:
        is_timer_started = True
        cyberpi.timer.reset()

        cyberpi.led.set_bri(get_led_brightness(int(previous_time % 60)))
        cyberpi.led.show("red orange yellow green cyan")

        while True:
            minutes, seconds = divmod(previous_time + cyberpi.timer.get(), 60)
            hours, minutes = divmod(minutes, 60)

            formatted_time = (str(int(hours)) if hours >= 10 else "0" + str(int(hours))) + "h" +\
                             (str(int(minutes)) if minutes >= 10 else "0" + str(int(minutes))) + "m" + \
                             (str(int(seconds)) if seconds >= 10 else "0" + str(int(seconds))) + "s"

            cyberpi.display.show_label(formatted_time, 24, "center")

            time.sleep(0.3)
            cyberpi.led.set_bri(get_led_brightness(seconds))
            cyberpi.led.move(1)

def get_led_brightness(seconds):
    if seconds % LED_EFFECT_STEPS <= (LED_EFFECT_STEPS / 2):
        return (seconds % LED_EFFECT_STEPS + 1) * 10
    else:
       return ((LED_EFFECT_STEPS / 2) - ((seconds % LED_EFFECT_STEPS) - (LED_EFFECT_STEPS / 2)) + 1) * 10

"""
Simple MicroPython program that runs offline in your CyberPi to roll dice
"""
import event, time, cyberpi, random

@event.start
def on_start():
    dice_value = 0

    while True:
        # welcome screen
        cyberpi.display.show_label("Shake me to roll dice", 16, "center")

        # wait until we receive a shake event
        while not cyberpi.get_shakeval() > 10:
            pass

        # play sounds and display random integer as rolling effect
        cyberpi.broadcast("play_shake_sound")
        cyberpi.led.show("red orange yellow green cyan")

        for n in range(5):
            time.sleep(0.1)
            dice_value = random.randint(1, 6)
            cyberpi.display.show_label(dice_value, 32, "center")
            cyberpi.led.move(1)

        cyberpi.broadcast("play_finish_sound")
        cyberpi.led.on(255, 255, 255, "all")

        # stop at last display number for 5 seconds and return to welcome screen
        time.sleep(5)
        cyberpi.led.off("all")

@event.receive("play_shake_sound")
def play_sound_effect():
    cyberpi.audio.set_vol(30)
    cyberpi.audio.play_until("clockwork")

@event.receive("play_finish_sound")
def play_finish_effect():
    cyberpi.audio.set_vol(30)
    cyberpi.audio.play_until("prompt-tone")

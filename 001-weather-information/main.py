"""
Cyberpi program to fetch current weather and diplay it in a table
"""

import event, cyberpi, math, time

# City IDs, retrieved from mBlock drag and drop editor
CITY_ID = "1819730" # Hong Kong
AIR_QUALITY_ID = "2572" # Mongkok, Hong Kong

weather = None
temperature_max = None
temperature_min = None
humidity = None
sunrise_time = None
sunset_time = None
air_quality = None

current_page = None

@event.start
def on_start():
    while True:
        global CITY_ID, AIR_QUALITY_ID, weather, temperature_max, temperature_min, humidity, sunrise_time, sunset_time, air_quality

        # reset cyberpi
        cyberpi.display.set_brush(255, 255, 255)
        cyberpi.console.clear()
        cyberpi.led.off("all")

        # reset state
        weather = None
        temperature_max = None
        temperature_min = None
        humidity = None
        sunrise_time = None
        sunset_time = None
        air_quality = None
        current_page = None

        # welcome
        cyberpi.display.show_label("即時天氣\n\n（請按B鍵開始）", 16, "center")

        while not cyberpi.controller.is_press("b"):
            pass

        # check for wi-fi connection before proceeding
        if not cyberpi.wifi.is_connect():
            cyberpi.display.set_brush(255, 0, 0)
            cyberpi.display.show_label("無法連接網絡，請按B鍵重新啟重程式。", 16, "center")
            cyberpi.led.on(208, 2, 27, "all")

            while not cyberpi.controller.is_press("b"):
                pass

            cyberpi.restart()
            cyberpi.stop_all()

        cyberpi.console.clear()

        # fetch weather from cloud
        cyberpi.broadcast("fetch_weather")
        cyberpi.broadcast("fetch_temperature_min")
        cyberpi.broadcast("fetch_temperature_max")
        cyberpi.broadcast("fetch_humidity")
        cyberpi.broadcast("fetch_sunrise_time")
        cyberpi.broadcast("fetch_sunset_time")
        cyberpi.broadcast("fetch_air_quality")

        cyberpi.display.set_brush(255, 255, 255)
        cyberpi.led.show("red orange yellow green cyan")

        while (
            weather is None
            or temperature_max is None
            or temperature_min is None
            or humidity is None
            or sunrise_time is None
            or sunset_time is None
            or air_quality is None
        ):
            progress = sum(
                data is not None \
                for data in [weather, temperature_max, temperature_min, humidity, sunrise_time, sunset_time, air_quality]
            )
            items_to_fetch = 7
            percentage = str(math.floor((progress / items_to_fetch) * 100)) + "%"
            cyberpi.display.show_label("正在獲取天氣信息...\n\n" + percentage, 12, "center")
            cyberpi.led.move(1)
            time.sleep(0.5)

        # fetch finish
        cyberpi.led.on(255, 255, 255, "all")
        cyberpi.console.clear()

        # display table and read aloud
        cyberpi.display.show_label("香港天氣", 12, "top_mid")
        display_page1()
        cyberpi.broadcast("read_weather")

        # listen to press events
        while True:
            # exit program
            if cyberpi.controller.is_press("a"):
                cyberpi.stop_other()
                break
            elif cyberpi.controller.is_press("middle") or cyberpi.controller.is_press("b"):
                if current_page == 1:
                    display_page2()
                else:
                    display_page1()
            elif (cyberpi.controller.is_press("down") or cyberpi.controller.is_press("right")) and current_page != 2:
                display_page2()
            elif (cyberpi.controller.is_press("up") or cyberpi.controller.is_press("left")) and current_page != 1:
                display_page1()

@event.receive("fetch_weather")
def fetch_weather():
    global weather
    weather = cyberpi.cloud.weather("weather", CITY_ID)

@event.receive("fetch_temperature_min")
def fetch_temperature_min():
    global temperature_min
    temperature_min = cyberpi.cloud.weather("min_temp", CITY_ID)

@event.receive("fetch_temperature_max")
def fetch_temperature_max():
    global temperature_max
    temperature_max = cyberpi.cloud.weather("max_temp", CITY_ID)

@event.receive("fetch_humidity")
def fetch_humidity():
    global humidity
    humidity = cyberpi.cloud.weather("humidity", CITY_ID)

@event.receive("fetch_sunrise_time")
def fetch_sunrise_time():
    global sunrise_time
    sunrise_time = cyberpi.cloud.time("sunrise_time", CITY_ID)

@event.receive("fetch_sunset_time")
def fetch_sunset_time():
    global sunset_time
    sunset_time = cyberpi.cloud.time("sunset_time", CITY_ID)

@event.receive("fetch_air_quality")
def fetch_air_quality():
    global air_quality
    air_quality = cyberpi.cloud.air("aqi", AIR_QUALITY_ID)

@event.receive("read_weather")
def read_weather():
    global air_quality, sunrise_time, sunset_time, temperature_max, temperature_min, weather, humidity
    cyberpi.audio.set_vol(10)
    speak_text = "香港現在天氣：" + str(weather) + "，" + \
                 "氣溫：" + str(temperature_min) + "至"  + str(temperature_max) + "℃，" + \
                 "濕度：" + str(humidity) + "%，" + \
                 "空氣質素：" + str(air_quality) + "（ " + get_health_concern_level(air_quality) + "），" + \
                 "日出時間：" + str(sunrise_time) + "，" + \
                 "日落時間：" + str(sunset_time)
    cyberpi.cloud.tts("zh", speak_text)

def display_page1():
    global current_page, weather, humidity, air_quality, temperature_min, temperature_max

    current_page = 1

    cyberpi.table.add(1, 1, "天氣")
    cyberpi.table.add(1, 2, weather)
    cyberpi.table.add(2, 1, "溫度")
    cyberpi.table.add(2, 2, str(temperature_min) + "℃" + "-" + str(temperature_max) + "℃")
    cyberpi.table.add(3, 1, "濕度")
    cyberpi.table.add(3, 2, str(humidity) + "%")
    cyberpi.table.add(4, 1, "空氣質素")
    cyberpi.table.add(4, 2, str(air_quality) + "（ " + get_health_concern_level(air_quality) + "）")

def display_page2():
    global current_page, sunrise_time, sunset_time

    current_page = 2

    cyberpi.table.add(1, 1, "日出")
    cyberpi.table.add(1, 2, sunrise_time)
    cyberpi.table.add(2, 1, "日落")
    cyberpi.table.add(2, 2, sunset_time)
    cyberpi.table.add(3, 1, "")
    cyberpi.table.add(3, 2, "")
    cyberpi.table.add(4, 1, "")
    cyberpi.table.add(4, 2, "")

def get_health_concern_level(air_quality):
    if air_quality <= 50:
        return "良好"
    if air_quality >= 51 and air_quality <= 100:
        return "普通"
    if air_quality >= 101 and air_quality <= 150:
        return "對敏感族群不良"
    if air_quality >= 151 and air_quality <= 200:
        return "對所有族群不良"
    if air_quality >= 200 and air_quality <= 300:
        return "非常不良"
    if air_quality >= 301:
        return "有害"

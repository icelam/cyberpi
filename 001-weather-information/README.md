# Weather Information

This is a CyberPi program written with MicroPython to retrieve the current weather information using IoT API provided by CyberPi.

Currently, this is configured to get the weather information of Hong Kong, feel free to change it to other cities!

## Configurations

### `CITY_ID`

`CITY_ID` is used for getting weather information other than air quality index. The ID can be found using official API:

```bash
ccurl --location --request GET 'https://mweather.makeblock.com/weatherSearch?city=hong kong'
```

### `AIR_QUALITY_ID`

`AIR_QUALITY_ID` is used for getting air quality index. The ID can be found using official API:

```bash
curl --location --request POST 'https://msapi.makeblock.com/air/search' \
--header 'Content-Type: application/json' \
--header 'Cookie: acw_tc=2f6a1f8616621108492292113e4a532958f37cd681f9ecb9c199c06c371599' \
--data-raw '{"searchkey": "hong kong"}'
```

## Demo

https://user-images.githubusercontent.com/6780420/188112085-e11424c6-0bcb-4e59-8c74-a2cf1ac5fd5a.mp4

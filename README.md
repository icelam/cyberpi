<p align="center">
  <img src="./cyberpi.png" width="200" />
</p>

<h1 align="center">CyberPi Programs</h1>

<p align="center">
  This repository stores the MicroPython / Python source code for CyberPi programs I created. 
</p>

## Prequisite

To run the code in this repository, you need to:

1. Get a [CyberPi main control board](https://education.makeblock.com/help/cyberpi-series-cyberpi/).
2. [mBlock 5](https://mblock.makeblock.com/en-us/download/) on your computer. Please refer to [CyberPi Series User Manual](https://www.yuque.com/makeblock-help-center-en/cyberpi/coding-software) to download the required software.
3. Some programs in this repository requires network connection to work properly, please use mBlock 5 to configure CyberPi's Wi-Fi connection.

## Running applications on CyberPi

Open the code in mBlock 5 Python editor and press "Run" or "Upload" button base on the programming language used:

|   Programming Language    |              mBlock GUI              |             MicroPython              |          Python 3           |
| :-----------------------: | :----------------------------------: | :----------------------------------: | :-------------------------: |
| Software used for editing |                mBlock                |         mBlock Python Editor         | mBlock mBlock Python Editor |
|        "Run" mode         |                  ✓                   |                  ✗                   |              ✓              |
|       "Upload" mode       |                  ✓                   |                  ✓                   |              ✗              |
|   Third-party libraries   |          mBlock Extensions           |                  /                   |      Python libraries       |
|     Operating Systems     | Windows, OSX, Linux, Chromebook, Web | Windows, OSX, Linux, Chromebook, Web |  Windows, OSX, Linux, Web   |

-   "Upload" mode : For program which does not require third-party modules and is able to run on CyberPi in a standalone way. Suitable for final product or Offline IoT demonstration.
-   "Run" mode: For program which depends on third-party modules like `pynput`, `pygame`. Suitable for realtime communication with computers.
    -   A `cyberpi` package bug on version 0.0.7 will throw the error `AttributeError: module 'makeblock.modules.cyberpi.api_cyberpi_api' has no attribute 'get_shield'` when using "Run" to test program. Here is a [link](https://forum.makeblock.com/t/cyberpi-has-no-attribute-get-shield/20023/2) that teaches you how to downgrade `cyberpi`.

**Be-careful that the upload operation will override the original program stored at the selected program slot.**

For details of how this can be done, Please refer to [CyberPi Series User Manual](https://www.yuque.com/makeblock-help-center-en/cyberpi/coding-software).

## Useful reference

### English

1. [CyberPi Series User Manual](https://www.yuque.com/makeblock-help-center-en/cyberpi)
2. [APIs for CyberPi](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api)

### Chinese

1. [童芯派系列產品說明書](https://www.yuque.com/makeblock-help-center-zh/cyberpi)
2. [童芯派 Python API](https://www.yuque.com/makeblock-help-center-zh/mcode/cyberpi-api)

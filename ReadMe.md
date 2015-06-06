A python library for I2C 0.96" 128x64 OLED display using SSD1306 chip.
A common library suiting both Raspberry Pi and Virtual-GPIO.

Library version 0.5 supported python. Version 0.7 (June 2015) supports also python3.
 
This oled display is the monochrome 4-pin type (I2C), not the SPI ones (identify by more pins).
Typically about $5 on eBay from LOTS of suppliers. Count the PCB pins - don't necessarily trust the eBay headline!
There are some "two-colour" ones, but these are simply a different (fixed) colour for the top 16 pixel lines.

Interfacing is trivial, and they seem to work fine on 3.3V and 5V.
On arduino (V-GPIO) the arduino's high-value pullups seem to work OK without anything added.

The text, font, image and graphic work is handled by the Python Imaging Library,
and ttf or other font files from anywhere work fine, at any scaling. 1-bit BMP or PNG images can be displayed.

"PIL" is wonderfully versatile and competent for "writing/drawing" to a display like this.
However, original PIL is now becoming obsolete. Instead use the clone ""Pillow"", now available for Python (2) and Python3.

Installing Pillow:
You need to "sudo apt-get install python-dev python-setuptools".
Then Pillow can be installed for python: "sudo easy_install Pillow". Takes quite a while.
Need also to "sudo apt-get install python3-dev python3-setuptools"
Then Pillow can be installed for python3: "sudo easy_install3 Pillow".

Getting I2C and SMBus working on recent Raspbian:
Ensure "i2c-dev" is listed in the file /etc/modules.
Use (new versions) raspi-config utility to turn on I2C functionality. 
Reboot. Enter "ls /dev" at a terminal, and i2c-1 should be listed as a working device.
Now install smbus for python:  "sudo apt-get install python-smbus python3-smbus".
(Note the Raspbian image of 5/5/2015 does not list python3-smbus. Just do a "apt-get update" first.)

This library has been evolved from RM Hull's very fine library at
https://github.com/rm-hull/ssd1306
If you simply want to use it on Raspberry Pi, the Hull version may well suit you better.

And, oh yes, some eBay versions might look very similar, but they don't necessarily have same pin order.
I have two with swapped VCC and GND. Oops!

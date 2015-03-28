A python library for I2C 0.96" 128x64 OLED display using SSD1306 chip.
A common library suiting both Raspberry Pi and Virtual-GPIO.

This oled display is the monochrome 4-pin type (I2C), not the SPI ones (identify by more pins).
Typically about $5 on eBay from LOTS of suppliers. Count the PCB pins - don't necessarily trust the eBay headline!
There are some "two-colour" ones, but these are simply a different (fixed) colour for the top 16 pixel lines.

Interfacing is trivial, and they seem to work fine on 3.3V and 5V.
On arduino (V-GPIO) the arduino's high-value pullups seem to work OK without anything added.

The text, font, image and graphic work is handled by the PIL python module(s),
and ttf font files from anywhere work fine, at any scaling. 1-bit BMP or PNG images can be displayed.

This library has been evolved from R Hull's very fine library at
https://github.com/rm-hull/ssd1306
If you simply want to use it on Raspberry Pi, Hull's version may well suit you better.

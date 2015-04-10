A python library for I2C 0.96" 128x64 OLED display using SSD1306 chip.
A common library suiting both Raspberry Pi and Virtual-GPIO.

This oled display is the monochrome 4-pin type (I2C), not the SPI ones (identify by more pins).
Typically about $5 on eBay from LOTS of suppliers. Count the PCB pins - don't necessarily trust the eBay headline!
There are some "two-colour" ones, but these are simply a different (fixed) colour for the top 16 pixel lines.

Interfacing is trivial, and they seem to work fine on 3.3V and 5V.
On arduino (V-GPIO) the arduino's high-value pullups seem to work OK without anything added.

The text, font, image and graphic work is handled by the Python Imaging Library,
and ttf or other font files from anywhere work fine, at any scaling. 1-bit BMP or PNG images can be displayed.

"PIL" is wonderfully versatile and competent for "writing/drawing" to a display like this.
However, PIL is available for download to Raspberry Pi and Windows for python 2.7 only, and not for python3.
Conclusion: stay with python 2.7 for this project.

This library has been evolved from RM Hull's very fine library at
https://github.com/rm-hull/ssd1306
If you simply want to use it on Raspberry Pi, the Hull version may well suit you better.


And, oh yes, some eBay versions might look very similar, but they don't necessarily have same pin order.
I have two with swapped VCC and GND. Oops!

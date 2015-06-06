#!/usr/bin/env python

# Substantially derived from code by (c) 2015 Richard Hull The MIT License (MIT)
# https://github.com/rm-hull/ssd1306:
#       "Permission is hereby granted, free of charge, to any person obtaining a copy
#       "of this software and associated documentation files (the "Software"), to deal
#       "in the Software without restriction, including without limitation the rights
#       "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#       "copies of the Software, and to permit persons to whom the Software is
#       "furnished to do so, subject to the following conditions:
#       "The above copyright notice and this permission notice shall be included in
#       "all copies or substantial portions of the Software."
#
# B Lavery 2015:
# This derivative "library" module is not installed to the python system as Hull's version was:
# it simply resides alongside your own python script.
# In this version, the I2C bus object needs to be handed in as a parameter from your user code.
# This makes this one same library file work with either Raspberry Pi or Virtual GPIO system.
# Hull's (clever) auto-displaying "canvas" is replaced by a persistent draw object
# which can be incrementally changed. This canvas needs coded "display()" calls to push to the hardware.

from PIL import Image, ImageDraw


class ssd1306():

    def __init__(self, bus, address=0x3C):
        self.cmd_mode = 0x00
        self.data_mode = 0x40
        self.bus = bus
        self.addr = address
        self.width = 128
        self.height = 64
        self.pages = int(self.height / 8)
        self.image = Image.new('1', (self.width, self.height))
        self.canvas = ImageDraw.Draw(self.image) # this is a "draw" object for preparing display contents

        self._command(
            const.DISPLAYOFF,
            const.SETDISPLAYCLOCKDIV, 0x80,
            const.SETMULTIPLEX,       0x3F,
            const.SETDISPLAYOFFSET,   0x00,
            const.SETSTARTLINE,
            const.CHARGEPUMP,         0x14,
            const.MEMORYMODE,         0x00,
            const.SEGREMAP,
            const.COMSCANDEC,
            const.SETCOMPINS,         0x12,
            const.SETCONTRAST,        0xCF,
            const.SETPRECHARGE,       0xF1,
            const.SETVCOMDETECT,      0x40,
            const.DISPLAYALLON_RESUME,
            const.NORMALDISPLAY,
            const.DISPLAYON)

    def _command(self, *cmd):
        """
        Sends a command or sequence of commands through to the
        device - maximum allowed is 32 bytes in one go.
        LIMIT ON ARDUINO: CMD BYTE + 31 = 32, SO LIMIT TO 31     bl
        """
        assert(len(cmd) <= 31)
        self.bus.write_i2c_block_data(self.addr, self.cmd_mode, list(cmd))

    def _data(self, data):
        """
        Sends a data byte or sequence of data bytes through to the
        device - maximum allowed in one transaction is 32 bytes, so if
        data is larger than this it is sent in chunks.
        In our library, only data operation used is 128x64 long, ie whole canvas.
        """

        for i in range(0, len(data), 31):
            self.bus.write_i2c_block_data(self.addr, self.data_mode, list(data[i:i+31]))


    def display(self):
        """
        The image on the "canvas" is flushed through to the hardware display.
        Takes the 1-bit image and dumps it to the SSD1306 OLED display.
        """

        self._command(
            const.COLUMNADDR, 0x00, self.width-1,  # Column start/end address
            const.PAGEADDR,   0x00, self.pages-1)  # Page start/end address

        pix = list(self.image.getdata())
        step = self.width * 8
        buf = []
        for y in range(0, self.pages * step, step):
            i = y + self.width-1
            while i >= y:
                byte = 0
                for n in range(0, step, self.width):
                    byte |= (pix[i + n] & 0x01) << 8
                    byte >>= 1

                buf.append(byte)
                i -= 1

        self._data(buf) # push out the whole lot

    def cls(self):
        self.canvas.rectangle((0, 0, self.width-1, self.height-1), outline=0, fill=0)
        self.display()

    def onoff(self, onoff):
        if onoff == 0:
            self._command(const.DISPLAYOFF)
        else:
            self._command(const.DISPLAYON)


class const:
    CHARGEPUMP = 0x8D
    COLUMNADDR = 0x21
    COMSCANDEC = 0xC8
    COMSCANINC = 0xC0
    DISPLAYALLON = 0xA5
    DISPLAYALLON_RESUME = 0xA4
    DISPLAYOFF = 0xAE
    DISPLAYON = 0xAF
    EXTERNALVCC = 0x1
    INVERTDISPLAY = 0xA7
    MEMORYMODE = 0x20
    NORMALDISPLAY = 0xA6
    PAGEADDR = 0x22
    SEGREMAP = 0xA0
    SETCOMPINS = 0xDA
    SETCONTRAST = 0x81
    SETDISPLAYCLOCKDIV = 0xD5
    SETDISPLAYOFFSET = 0xD3
    SETHIGHCOLUMN = 0x10
    SETLOWCOLUMN = 0x00
    SETMULTIPLEX = 0xA8
    SETPRECHARGE = 0xD9
    SETSEGMENTREMAP = 0xA1
    SETSTARTLINE = 0x40
    SETVCOMDETECT = 0xDB
    SWITCHCAPVCC = 0x2

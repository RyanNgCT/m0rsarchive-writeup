#!/usr/bin/env python3
# =================================================================================
# Name: mocr.py (Morse OCR helper script)
# Version: v3 (alpha)
# Author: eauxfolles (10.07.2020), modified on 19.12.2023 by RyanNgCT
# Description: Script to read morse code from file and translate into readable text
# Usage: "python solve.py"
# Assumptions:  - Morse code expected to be reflected as "." and "-"
#               - "." expected to be 1 pixel, "-" expected to be 3 pixel long
#               - Image has consistent background color (as pixel at position 0,0)
#               - Background color is different than morse code
#               - Each line contains one word coded in morse
# =================================================================================

import sys
from PIL import Image

translate = {
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.-.-.-': '.',
    '--..--': ',',
    '---...': ':',
    '-.-.-.': ';',
    '..--..': '?',
    '-.-.--': '!',
    '-....-': '-',
    '..--.-': '_',
    '-.--.': '(',
    '-.--.-': ')',
    '.----.': '\'',
    '.-..-.': '\"',
    '-...-': '=',
    '.-.-.': '+',
    '-..-.': '/',
    '.--.-.': '@'
}

def decodeMorse(image_file):
    # use module "PIL" (Python Image Library) to open image-file and load image-data (size and background color) 
    try:
        morse_image = Image.open(image_file)
    except:
        print("error: could not open file")
        exit()
    width, height = morse_image.size
    pixel_data = morse_image.load()
    background_color = pixel_data[0,0]

    # define function to translate morse character into letter
    def morse_translate(morse_input):
        try:
            return translate[morse_input]
        except:
            print("\nerror: unable to translate morse code")
            exit()


    # store result of function call
    res = ''

    # loop through each pixel, line after line
    for line in range(0, height):
        morse_char = ""
        pixel_count = 0
        for pixel in range(0, width):
            if pixel_data[pixel, line] != background_color:
                pixel_count += 1
            else:
                if pixel_count == 1:
                    morse_char += "."
                    if pixel_data[pixel+1, line] == background_color: 
                        res += str(morse_translate(morse_char))
                        morse_char = ""
                elif pixel_count == 3:
                    morse_char += "-"
                    if pixel_data[pixel+1, line] == background_color: 
                        res += str(morse_translate(morse_char))
                        morse_char = ""
                elif pixel_count == 0:
                    pass
                else:
                    print("error: cannot read morse code")
                pixel_count = 0

    return res

    # close image-file
    morse_image.close()

if __name__ == "__main__":
    decodeMorse()

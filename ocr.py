#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import pytesseract
from PIL import Image
import os
import rumps
import pyperclip

@rumps.clicked('OCR')
def ocr(sender):
    os.system('screencapture -i %s' % '/Users/jerryhu/Desktop/capture.png')
    img = Image.open('/Users/jerryhu/Desktop/capture.png')
    text = pytesseract.image_to_string(img)
    pyperclip.copy(text)

    rumps.Window(message='OCR Capture', default_text=text, title='Text Copied').run()
    os.remove('/Users/jerryhu/Desktop/capture.png')

app = rumps.App('OCR', menu=[
    'OCR',
    None
])
app.run()
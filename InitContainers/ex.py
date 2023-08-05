import pyautogui as py
import time

msg="Happy BirthDay"

time.sleep(2)

for i in range(5):
    py.typewrite(msg)
    time.sleep(1)
    py.press('Enter')
    time.sleep(1)


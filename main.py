import pyautogui
import time
import random
import sys
import keyboard

horizontal = random.randint(1032,1361)
vertical = random.randint(254,581)
time.sleep(2)

def click():
    pyautogui.click(random.randint(1032,1361),random.randint(254,581))

i = 1
while i <= 10000000:
    pyautogui.mouseDown()
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        sys.exit()
    click()
    pyautogui.mouseDown()
#pyautogui.displayMousePosition()

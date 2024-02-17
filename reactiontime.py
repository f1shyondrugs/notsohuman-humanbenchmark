import pyautogui
import time

while True:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    if px[0] == 43:
        print("blue")
        time.sleep(3)
        pyautogui.click()

    elif px[0] == 206:
        print("red")


    elif px[0] == 75:
        print("green click")
        pyautogui.click()
    
    
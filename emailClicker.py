import win32api
import time
import pyautogui

i=0
coordinates = []
perma = []
print('click on cross')
while True:
        if win32api.GetKeyState(0x01) < 0:
            box_x, box_y = pyautogui.position()
            print('box_x, box_y obtained!')
            print(box_x, box_y)
            time.sleep(0.2)
            coordinates.append(box_x)
            coordinates.append(box_y)
            break
print('click permabox')
while True:
        if win32api.GetKeyState(0x01) < 0:
            box_x, box_y = pyautogui.position()
            print('box_x, box_y obtained!')
            print(box_x, box_y)
            time.sleep(0.2)
            perma.append(box_x)
            perma.append(box_y)
            break
while i<4000:
    i = i+1
    x = coordinates[0]
    y = coordinates[1]
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    x = perma[0]
    y = perma[1]
    pyautogui.moveTo(x, y)
    pyautogui.click()

    print(i)
    
    time.sleep(0.5)
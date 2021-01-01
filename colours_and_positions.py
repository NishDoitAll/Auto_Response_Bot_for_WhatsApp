import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position()
    print(posXY, pt.pixel(posXY[0],posXY[1]))
    sleep(1)
    if posXY[0] == 0:
        break

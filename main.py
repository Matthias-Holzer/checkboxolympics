import pyautogui
import pygetwindow as gw
from PIL import Image
import time
from pynput.mouse import Button, Controller

print(gw.getAllTitles())
mac = 'Firefox Checkbox Olympics'
# pyautogui.getWindowsWithTitle(mac)[0].maximize()
time.sleep(4)
pyautogui.screenshot('imgs/shot.png')
x, y, width, height = gw.getWindowGeometry(mac)
print(gw.getWindowGeometry(mac))
# croping the screenshot
img = Image.open('imgs/shot.png')
img = img.crop((x * 2, y * 2, (x + width) * 2, (y + height) * 2))
img.save('imgs/croped.png')

# start
ready = (465, 1210)
mouse = Controller()
mouse.position = ((x + ready[0]) / 2, (y + ready[1]) / 2)
time.sleep(0.5)
mouse.press(Button.left)
mouse.release(Button.left)
#pyautogui.leftClick((x + ready[0]) / 2, (y + ready[1]) / 2)
time.sleep(2.9)

# click
start = (858, 977)
for i in range(28):
    mouse.position = ((x + start[0] / 2, (y + start[1]) / 2))
    time.sleep(0.006)
    mouse.press(Button.left)
    mouse.release(Button.left)
    #pyautogui.leftClick((x + start[0] / 2, (y + start[1]) / 2))
    start = (start[0] + 42, start[1])

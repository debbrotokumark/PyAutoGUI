import pyautogui
import time as t


pyautogui.click(1218, 1049)
t.sleep(4)
# print(pyautogui.position())
pyautogui.click(179, 256)
t.sleep(2)
print(pyautogui.position())
pyautogui.click(772, 991)
t.sleep(2)

for i in range(10):
    pyautogui.typewrite(f"Debbroto Kumar Karmokar {i+1}")
    pyautogui.press('enter')
    t.sleep(1)

pyautogui.typewrite("Done")
pyautogui.press('enter')


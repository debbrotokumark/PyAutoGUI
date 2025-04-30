import time
import pyautogui

# pyautogui.PAUSE = .1  # Pause 0.5 seconds after each PyAutoGUI call

# screen_size = pyautogui.size()  # Screen size
# print(screen_size)
# width, height = pyautogui.size()
# print("Width:", width)
# print("Height:", height)

# print(pyautogui.position())  # mouse position
# pyautogui.moveTo(300, 38)  # set mouse in this position
# pyautogui.moveTo(472, 42, 4)  # move mouse old position to this position in 4s
# pyautogui.moveTo(500, 500)
# pyautogui.move(40, -30)  # right/down pasitivbe number #left/up negative number
# pyautogui.moveTo(1920,1080)
# pyautogui.click(989,956) # click this position
# pyautogui.click(989,956,button="right")  # click mouse right this position
# pyautogui.click(546,432,clicks=2) # click two time this position
# pyautogui.click(546,432,clicks=2,interval=2) # set time
# pyautogui.rightClick(546,432) # right click
# pyautogui.click(546,432,button="right") # right click
# pyautogui.click(546,432,button="left") # right click

# pyautogui.doubleClick(546,432)

# pyautogui.moveTo(546, 432)
# pyautogui.click()  # cick current position

# move its move from current position same px

# move to its move any position
# pyautogui.moveTo(1119, 417)
# pyautogui.press("enter")
# pyautogui.write("#debbroto")

# pyautogui.hotkey("ctrl", "a")  # Simulates Ctrl+a
# pyautogui.moveRel(50, 0, 1)


# pyautogui.scroll(500)  # Scrolls up
# pyautogui.scroll(-500)  # Scrolls down,

# time.sleep(3)  # Open MS Paint before this runs

# Draw a square
# pyautogui.moveTo(500, 300)
# pyautogui.dragTo(600, 300, duration=0.5)
# pyautogui.dragTo(600, 400, duration=0.5)
# pyautogui.dragTo(500, 400, duration=0.5)
# pyautogui.dragTo(500, 300, duration=0.5)

# xOffset: How far to drag on the X-axis (right = positive, left = negative)

# yOffset: How far to drag on the Y-axis (down = positive, up = negative)

# pyautogui.dragRel(100, 50, duration=3)
# pyautogui.mouseDown()
# pyautogui.dragRel(100, 0, duration=0.5)
# pyautogui.dragRel(0, 100, duration=0.5)
# pyautogui.dragRel(-100, 0, duration=0.5)XYab
# pyautogui.dragRel(0, -100, duration=0.5)
# pyautogui.mouseUp()

# pyautogui.typewrite(['a', 'b', 'left', 'left','enter','space','X', 'Y'])
# enter not working
# pyautogui.screenshot('screen.png')
# pyautogui.alert('Message')
# pyautogui.alert('This is an alert box!', title='Alert', button='OK')

# response = pyautogui.confirm('Do you want to continue?', title='Confirmation', buttons=['Yes', 'No'])

# print("You selected:", response)
# choice = pyautogui.confirm("Choose your role", buttons=[
#     "Admin", "User", "Guest"])

# name = pyautogui.prompt(
#     'Enter your name:', title='User Input', default='Guest')
# print("Name entered:", name)
# pyautogui.FAILSAFE = False

def subscribe():
    time.sleep(2)  # Give you time to open the screen
    sub = pyautogui.locateCenterOnScreen('subscribe.png', confidence=0.8)
    if sub:
        pyautogui.click(sub)
    else:
        print("Image not found!")


subscribe()  # detact image and click this image

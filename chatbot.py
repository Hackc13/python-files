import pyautogui
import time
time.sleep(10)

for i in range(20):
	pyautogui.typewrite('what msg u want to send')
	pyautogui.press('enter')
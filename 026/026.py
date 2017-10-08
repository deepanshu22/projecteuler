#This is a python3 script that is can autmate the clicking process
#It clicks for 250 times after every .6 seconds at any postion and displays a message while doing so.


import pyautogui
import time

x,y = pyautogui.position()
pyautogui.rightClick(x,y)
click=250
while(click):
	x,y = pyautogui.position()
	p=15
	pyautogui.click(x,y)
	print("we are clicking")
	time.sleep(.6)
	click=click-1	
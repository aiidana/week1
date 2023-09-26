import time, pyautogui

time.sleep(10)
f= open('text.txt', 'r')

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')
    
 
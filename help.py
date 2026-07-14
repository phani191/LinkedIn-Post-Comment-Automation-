import pyautogui


def helper():
    coordinates=pyautogui.locateCenterOnScreen('comment.png',confidence=0.8)
    pyautogui.moveTo(coordinates)
    pyautogui.click()
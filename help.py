import pyautogui


def helper():
    coordinates=pyautogui.locateCenterOnScreen('comment.png',confidence=0.8)
    pyautogui.moveTo(coordinates)
    pyautogui.click()

def helperSort():
    coordinates=pyautogui.locateCenterOnScreen('sort.png',confidence=0.8)
    pyautogui.moveTo(coordinates)
    pyautogui.click()

def findSort():
    coordinates=pyautogui.locateCenterOnScreen('sort.png',confidence=0.8)
    pyautogui.moveTo(coordinates)
    pyautogui.click()

def showres():
    coordinates=pyautogui.locateCenterOnScreen('showres.png',confidence=0.8)
    pyautogui.moveTo(coordinates)
    pyautogui.click()

def findlatest():
    coordinates=pyautogui.locateCenterOnScreen('latest.png',confidence=0.5)
    pyautogui.moveTo(coordinates)
    pyautogui.click()
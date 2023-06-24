import pyautogui


def lab001():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    print(screenWidth, screenHeight)

    # (buttonx, buttony) = pyautogui.locateCenterOnScreen('data/01.jpg')  # returns (x, y) of matching region
    # print(buttonx, buttony)

    pyautogui.locateCenterOnScreen('01.jpg')

    pass


if __name__ == '__main__':
    lab001()

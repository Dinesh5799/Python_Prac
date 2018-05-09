import pyautogui

alr = "Please Make Sure That Your Device Is Connected"
path = input('Enter The Path Which Contains Apk - ')
path += "luavmandroid.apk"
pyautogui.hotkey('win', 'r')
pyautogui.typewrite(['c','m','d','enter'])
for i in alr:
    pyautogui.typewrite(i)
#pyautogui.hotkey('ctrl', 'a')
for i in alr:
    pyautogui.typewrite(['backspace'])
#pyautogui.typewrite(['a','d','b','space','i','n','s','t','a','l','l','space'])
pyautogui.typewrite("adb install ")
for i in path:
    pyautogui.typewrite(i)
#luavmandroid.apk
pyautogui.typewrite(['enter'])





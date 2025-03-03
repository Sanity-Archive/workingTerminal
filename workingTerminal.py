import pyautogui

#tab 1
#has to be run twice, because one tab will be closed after python finishes
pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('t')   
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')
pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('t')   
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')


#tab2
pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('t')   
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')

#tab3 with split screen
pyautogui.keyDown('ctrl') 
pyautogui.keyDown('shift')
pyautogui.press('r')      
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')

pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('d')   
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')

#switch to tab1
pyautogui.keyDown('alt')  
pyautogui.press('1')   
pyautogui.keyUp('alt')
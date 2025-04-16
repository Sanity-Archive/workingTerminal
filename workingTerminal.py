import pyautogui

#tab 1
pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('t')
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')
#rename tab1
pyautogui.keyDown('alt')  
pyautogui.keyDown('shift')
pyautogui.press('s')   
pyautogui.keyUp('alt')
pyautogui.keyUp('shift')
pyautogui.write('tun0')
pyautogui.press('enter')

#tab 2
pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('t')
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')
#rename tab2
pyautogui.keyDown('alt')  
pyautogui.keyDown('shift')
pyautogui.press('s')   
pyautogui.keyUp('alt')
pyautogui.keyUp('shift')
pyautogui.write('enum')
pyautogui.press('enter')


#tab3
pyautogui.keyDown('ctrl')  
pyautogui.keyDown('shift')
pyautogui.press('t')   
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')
#rename tab3
pyautogui.keyDown('alt')  
pyautogui.keyDown('shift')
pyautogui.press('s')   
pyautogui.keyUp('alt')
pyautogui.keyUp('shift')
pyautogui.write('attack')
pyautogui.press('enter')
#split tab horizontally
pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.press('d')   
pyautogui.keyUp('ctrl')   
pyautogui.keyUp('shift')

#switch back to tab 1
pyautogui.keyDown('alt')
pyautogui.press('1')   
pyautogui.keyUp('alt')
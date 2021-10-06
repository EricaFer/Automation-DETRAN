import pyautogui
import pyperclip
import time
import winsound

pyautogui.PAUSE = 1

button = pyautogui.confirm(text='Automation is starting, please press OK to continue', title = 'Automation Warning', buttons=['OK', 'Cancel'])

def get_url():
    # Get the url
    pyautogui.press('f6')

    # Copys url
    pyautogui.hotkey('ctrl','c')

    # Return current url
    return pyperclip.paste()

if button == 'OK':

    pyautogui.hotkey('alt','tab')

    # Goes to first tab
    pyautogui.hotkey('ctrl','1')

    #Scrolls down
    pyautogui.press('home')
    pyautogui.press('pgdn')

    # Clicks "I'm not a robot"
    pyautogui.click(x=663, y=662)

    pyautogui.press('pgdn')

    # Click send
    pyautogui.click(x=713, y=220) 

    time.sleep(10)

    while url != 'https://detran.rj.gov.br/_agendamento.eletronico/renach/telab2.asp':

        url = get_url()
        time.sleep(10)

    # Scroll down
    pyautogui.press('pgdn')

    # Click send
    pyautogui.click(x=493, y=408)

    # Waits for page to load
    time.sleep(40)

    # Gets url
    url = get_url()

    if 'coderro' in url:
        
        pyautogui.confirm(text='Press OK to go back', title = 'No Slots Found', buttons=['OK'])

        # Go back twice
        pyautogui.click(x=317, y=508, clicks= 2)
        
    else:

        pyautogui.alert(text='We found a slot', title = 'Success', button = 'OK')

        # Warning
        winsound.Beep(440, 1000)

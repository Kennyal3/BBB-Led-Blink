#***!/usr/bin/python... shebang used to select other interpreter***
#first attempt to blink leds on beaglebone

import os

LED_PATH = '/home/BBB_Simulate/class/leds'

def main():
    print('running main')
    print('************')
    
#display directory
    os.chdir(LED_PATH)
    cwd = os.getcwd()
    print(cwd)
    print(os.listdir(LED_PATH))

#get user led choice
    led = get_usrled()
    print('in main user led =')
    print(led)
    
#set user led choice path
    usrled_path = set_usrled(led)
    print('in main: usrled path = ')
    print(usrled_path)
    
    #os.listdir(PATH)
    print('*********')
    print('main done')
    
#do something
    #set constant on/off
    state = str(input('Enter command: '))
    set_brightness(state)
    #turn on/off (mmc1 is on by default)
    #set delay on/off

    
#get usr led selection
def get_usrled():
    print('running get_usrled choice')
    print('******************')
    try:
        usrled = str(input('Enter User Led #: '))
        print('get_usrled done')
        print('***************')
        return usrled
    except:
        print('Error')
        return
    

#set user led choice
def set_usrled(usrled):
    print('running set_usrled')
    print('******************')

    try:
        usrled_path = str(LED_PATH + '/beaglebone_green_usr' + usrled)
        print('set_usrled done')
        print('***************')
        return usrled_path 
    except:
        print('Error')
        return

def set_brightness(state):
    #posistion 1 = on
    #position 0 = off
    if state == '1': 
        try:
            os.system("echo 'state' > brightness")
            print(get_usrled() + ' is on.')
        except:
            return
    elif state == '0':
        try:
            os.system("echo 'state' > brightness")
            print(get_usrled() + ' is off.')
        except:
            return
    else:
        return     
    
    
    
    
    
    
main()
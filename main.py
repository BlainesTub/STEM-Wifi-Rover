#imports the curses library

import curses

#imports the motor shield library

from pololu_drv8835_rpi import motors, MAX_SPEED

#these are the default values for the motor speeds
speed = 120

#Positive trim values make the bot make the bot turn right, negative values make the bot turn left
trim = 0

#CONTROL BUTTONS!!!! 
# press 1, 2, 3, or 4 to select speed, 
# Press Q to manually slow down
# Press E to manually speed up

#These are the different speed levels you can choose
speedlevel1 = 120
speedlevel2 = 240
speedlevel3 = 360
speedlevel4 = 480
#This is the increment value for manually adjusting speed
speedincrement = 5

#This is assuming that Motor 1 is your left motor, and motor 2 is your right motor
leftspeed = speed+trim
rightspeed = speed-trim

leftspeedreverse = leftspeed * -1
rightspeedreverse = rightspeed *-1

print ('System Initialized. Good Morning \n')
#Functions
def stop():
    motors.setSpeeds(0, 0)

def go_forward():
    motors.setSpeeds(leftspeed, rightspeed)

def go_backward():
    motors.setSpeeds(leftspeedreverse, rightspeedreverse)

def turn_left():
    motors.setSpeeds(leftspeedreverse, rightspeed)

def turn_right():
    motors.setSpeeds(rightspeed, leftspeedreverse)

def main():
    #set up curses window
    STDSCR = curses.initscr()
    #turn off keys echoing to screen
#####################################   # curses.noecho()
    #react to keys being pressed instantaneously instead of   waiting for enter to be pressed
    curses.cbreak()
    #replace default values returned with things like the  arrow keys to things like curses.KEY_LEFT
    STDSCR.keypad(True)

    STDSCR.addstr("To exit the program, press CTRL + C in order to quit the process. ")
    #To change keybindings for the movement change 
    #the keys shown here. You may need to refer to the 
    #python curses documentation which can be reached at    https://docs.python.org/3/library/curses.html for  non-ascii keys. 
    while True: 

        input_char = STDSCR.getch()
        if input_char == ord('w') or input_char == curses.KEY_UP:   
            go_forward()
        elif input_char == ord('s') or input_char == curses.KEY_DOWN:
            go_backward()
        elif input_char == ord('a') or input_char == curses.KEY_LEFT:
            turn_left()
        elif input_char == ord('d') or input_char == curses.KEY_RIGHT:
            turn_right()
        elif input_char == ord('f'):
            stop()
try:      
    main()
finally:    
    motors.setSpeeds(0, 0)#imports the curses library

import curses

#imports the motor shield library

from pololu_drv8835_rpi import motors, MAX_SPEED

#these are the default values for the motor speeds
speed = MAX_SPEED

reversespeed = speed * -1
#Functions
#The parameters for speed are in percent (eg. go_forward(0.7) would go forward at 70% speed; 
#default is 100%)

def stop():
    motors.setSpeeds(0, 0)

def go_forward():
    motors.setSpeeds(speed, speed)

def go_backward():
    motors.setSpeeds(reversespeed, reversespeed)

def turn_left():
    motors.setSpeeds(speed, reversespeed)

def turn_right():
    motors.setSpeeds(reversespeed, speed)

def main():
    #set up curses window
    STDSCR = curses.initscr()
    #turn off keys echoing to screen
    curses.noecho()
    #react to keys being pressed instantaneously instead of   waiting for enter to be pressed
    curses.cbreak()
    #replace default values returned with things like the  arrow keys to things like curses.KEY_LEFT
    STDSCR.keypad(True)

    STDSCR.addstr("To exit the program, press CTRL + C in order to quit the process. ")
    #To change keybindings for the movement change 
    #the keys shown here. You may need to refer to the 
    #python curses documentation which can be reached at    https://docs.python.org/3/library/curses.html for  non-ascii keys. 
    while True: 
        input_char = STDSCR.getch()
        if input_char == ord('w') or input_char == curses.KEY_UP:   
            go_forward()
        elif input_char == ord('a') or input_char == curses.KEY_LEFT:
            go_backward()
        elif input_char == ord('s') or input_char == curses.KEY_DOWN:
            turn_left()
        elif input_char == ord('d') or input_char == curses.KEY_RIGHT:
            turn_right()
        elif input_char == ord('f'):
            stop()
        #Speed levels
        elif input_char == ord('1')
            speed = speedlevel1
        elif input_char == ord('2')
            speed = speedlevel2
        elif input_char == ord('3')
            speed = speedlevel3
        elif input_char == ord('4')
            speed = speedlevel4
        elif input_char == ord('e')
            speed = speed+speedincrement
            print(speed + \n)
        elif input_char == ord('q')
            speed = speed-speedincrement
            print(speed + \n)
        
try:      
    main()
finally:    
    motors.setSpeeds(0, 0)

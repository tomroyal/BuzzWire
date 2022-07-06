import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# buzz wire circuit runs between D12 and ground

BuzzerWire = DigitalInOut(board.D12)
BuzzerWire.direction = Direction.INPUT
BuzzerWire.pull = Pull.UP

# red button for restart between D10 and ground

RedButton = DigitalInOut(board.D10)
RedButton.direction = Direction.INPUT
RedButton.pull = Pull.UP

# use on board neopixel to show in play state..

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

inGame = False

pixels[0] = (10, 0, 0)

def waitForBuzz(tvalue,initTvalue): 
    pressedYet = False;
    while pressedYet is False:
        # print(tvalue-initTvalue)
        time.sleep(0.1)
        tvalue = tvalue + 0.1
        pressed = BuzzerWire.value
        if pressed is False:
            pixels[0] = (10, 0, 0)
            pressedYet = True
            
    return tvalue

def waitForButton():
    pressedYet = False;
    while pressedYet is False:
        pressed = RedButton.value
        if pressed is False:
            pressedYet = True  

def showResult(tresult):
    print("Timer stopped at ",tresult)

def initGame(inGame):
    print("Game start!")
    pixels[0] = (0, 10, 0)
    inGame = True
    tvalue = time.monotonic();
    initTvalue = tvalue;
    tvalue = waitForBuzz(tvalue,initTvalue) 
    showResult(tvalue-initTvalue)
    inGame = False

while True:
    if inGame is False:
        waitForButton()
        initGame(inGame)


import time
import numpy as np
from rpi_ws281x import *

COORDINATES_2_LEDID = [[49, 48, 47, 46, 45, 44, 43, 42, 41, 40], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [29, 28, 27, 26, 25, 24, 23, 22, 21, 20], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
LEDID_2_COORDINATES = [[9, 4], [8, 4], [7, 4],[6, 4],[5, 4],[4, 4],[3, 4],[2, 4],[1, 4],[0, 4],[0, 3],[1, 3],[2, 3],[3, 3],[4, 3],[5, 3],[6, 3],[7, 3],[8, 3],[9, 3],[9, 2],[8, 2],[7, 2],[6, 2],[5, 2],[4, 2],[3, 2],[2, 2],[1, 2],[0, 2],[0, 1],[1, 1],[2, 1],[3, 1],[4, 1],[5, 1],[6, 1],[7, 1],[8, 1],[9, 1],[9, 0],[8, 0],[7, 0],[6, 0],[5, 0],[4, 0],[3, 0],[2, 0],[1, 0],[0, 0]]
MATRIX = np.zeros( (5, 100) )
MATRIX_Y_COUNT = 10
MATRIX_X_COUNT = 5

LED_COUNT      = MATRIX_Y_COUNT * MATRIX_X_COUNT
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10             # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255            # Set to 0 for darkest and 255 for brighstandard
LED_INVERT     = False          # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0              # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_BCKGRD = Color(0,0,255)   #color of the background
LED_COLOR = Color(0,255,0)          #color of the letters

CHAR_A = [7,11,13,28,31,26,30,34,49,45,32,33]
CHAR_B = [9,8,7,13,29,10,28,27,30,33,49,48,47]
CHAR_C = [8,7,10,29,30,48,47]
CHAR_D = [9,8,7,10,13,29,26,30,33,49,48,47]
CHAR_E = [9,8,7,6,10,29,28,27,30,49,48,47,46]
CHAR_F = [9,8,7,6,10,29,27,28,30,49]
CHAR_G = [8,7,6,10,29,27,26,30,33,48,47,46]
CHAR_H = [9,6,10,13,29,28,27,26,30,33,49,46]
CHAR_I = [9,8,7,11,28,31,49,48,47]
CHAR_J = [9,8,7,6,13,26,33,47,48,30]
CHAR_K = [9,6,10,12,29,28,30,32,49,46]
CHAR_L = [9,10,29,30,49,48,47,46]
CHAR_M = [9,5,10,11,13,14,29,27,25,30,34,49,45]
CHAR_N = [9,6,10,11,13,29,28,27,26,30,32,33,49,46]
CHAR_O = [8,7,10,13,29,26,30,33,48,47]
CHAR_P = [9,8,7,10,13,29,28,27,30,49]
CHAR_Q = [8,7,10,13,29,26,30,33,48,47,32,34,44]
CHAR_R = [9,8,7,10,13,29,28,27,30,33,49,46]
CHAR_S = [8,7,10,28,27,33,48,47]
CHAR_T = [9,8,7,6,5,12,27,32,47]
CHAR_U = [9,6,10,13,29,26,30,33,48,47]
CHAR_V = [9,5,10,14,28,26,31,33,47]
CHAR_W = [9,10,5,14,29,25,30,34,48,46,32,27]
CHAR_X = [9,5,11,13,27,31,33,49,45]
CHAR_Y = [9,5,11,13,27,32,47]
CHAR_Z = [9,8,7,6,12,13,28,27,30,31,49,48,47,46]
CHAR_MINUS = [29,28,27,26]
CHAR_POINT = [49]
CHAR_XCLMTN = [49,29,10,9]
CHAR_KOMMA = [49,31]
CHAR_0 = [8,10,12,29,27,30,32,48]
CHAR_1 = [10,8,11,28,31,48]
CHAR_2 = [9,8,12,28,30,49,48,47]
CHAR_3 = [10,8,7,13,27,33,47,48,30]
CHAR_4 = [9,7,10,12,29,28,27,32,47]
CHAR_5 = [9,8,7,10,29,28,32,49,48]
CHAR_6 = [8,7,10,29,28,27,30,32,49,48,47]
CHAR_7 = [9,8,7,12,28,31,49]
CHAR_8 = [8,10,12,28,30,32,48]
CHAR_9 = [9,8,7,10,12,29,28,27,32,49,48,47]
CHAR_STAR = [8,12,14,6,13,29,28,27,26,25,24,48,32,33,34,46,44]

space = -6
text = 'iot-tram rocks'
TEXT_ROUND = 0                              #Number of rounds the text goes (0 equals infinity)
TEXT_STEPS = 1                               #Steps in wich the text jumps
TEXT_SPEED = 0.1                            #Speed in wich the text moves (in Number of seconds, in wich one step happens)



#standard funktions
def reset(strip):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
            strip.show()

def showLED(strip, pin_num, color):
    strip.setPixelColor(pin_num, color)
    strip.show()

    


#funktions for writing                
def showDisplay():
    # Set Background
    for idx, col in np.ndenumerate(MATRIX):
        #print('MATRIX Index: ', idx)
        for status in np.ndenumerate(col):
            #print('Aktueller Wert für LED-Status: ', status[1])
            if status[1] == 0 and idx[1] < MATRIX_Y_COUNT and idx[1] > -1: # status 1=on; status 0=off
                #print('IDX[0]: ', idx[0])
                #print('IDX[1]: ', idx[1])
                showLED(strip, COORDINATES_2_LEDID[idx[0]][idx[1]], LED_BCKGRD)

    # Set Matrix Foreground
    for idx, col in np.ndenumerate(MATRIX):
        #print('MATRIX Index: ', idx)
        for status in np.ndenumerate(col):
            #print('Aktueller Wert für LED-Status: ', status[1])
            if status[1] == 1 and idx[1] < MATRIX_Y_COUNT and idx[1] > -1: # status 1=on; status 0=off
                #print('IDX[0]: ', idx[0])
                #print('IDX[1]: ', idx[1])
                showLED(strip, COORDINATES_2_LEDID[idx[0]][idx[1]], LED_COLOR)
    

def writeMatrix(letter):
        if letter == 'a' :
            for wert in CHAR_A:
                #print('Wert: ',  wert, ' entspricht der Koordinate: ', LEDID_2_COORDINATES[wert][1], ', ', LEDID_2_COORDINATES[wert][0])
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'b' :
            for wert in CHAR_B:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'c' :
            for wert in CHAR_C:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'd' :
            for wert in CHAR_D:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'e' :
            for wert in CHAR_E:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'f' :
            for wert in CHAR_F:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'g' :
            for wert in CHAR_G:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'h' :
            for wert in CHAR_H:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'i' :
            for wert in CHAR_I:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'j' :
            for wert in CHAR_J:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'k' :
            for wert in CHAR_K:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'l' :
            for wert in CHAR_L:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'm' :
            for wert in CHAR_M:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'n' :
            for wert in CHAR_N:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'o' :
            for wert in CHAR_O:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'p' :
            for wert in CHAR_P:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'q' :
            for wert in CHAR_Q:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'r' :
            for wert in CHAR_R:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 's' :
            for wert in CHAR_S:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 't' :
            for wert in CHAR_T:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'u' :
            for wert in CHAR_U:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'v' :
            for wert in CHAR_V:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'w' :
            for wert in CHAR_W:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'x' :
            for wert in CHAR_X:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'y' :
            for wert in CHAR_Y:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == 'z' :
            for wert in CHAR_Z:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '-' :
            for wert in CHAR_MINUS:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '.' :
            for wert in CHAR_POINT:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '!' :
            for wert in CHAR_XCLMTN:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '0' :
            for wert in CHAR_0:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '1' :
            for wert in CHAR_1:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '2' :
            for wert in CHAR_2:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '3' :
            for wert in CHAR_3:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '4' :
            for wert in CHAR_4:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '5' :
            for wert in CHAR_5:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '6' :
            for wert in CHAR_6:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '7' :
            for wert in CHAR_7:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '8' :
            for wert in CHAR_8:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '9' :
            for wert in CHAR_9:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        elif letter == '*' :
            for wert in CHAR_STAR:
                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        
        else :
                if letter == '!' :
                        for wert in CHAR_XCLMTN:
                                MATRIX[LEDID_2_COORDINATES[wert][1]] [LEDID_2_COORDINATES[wert][0]] = 1
        
def matrixShift(MATRIX,speed):
    return np.roll(MATRIX,speed,1)

def makeSpace(cha):
        if cha == 'a' or cha == 'm' or cha == 't' or cha == 'v' or cha == 'w' or cha == 'x' or cha == 'y': #this Letters are 5 Leds long
                return -7                                                                                      #space gets set to 6, so there are 2 Leds space
        elif cha == 'c' or cha == 'i':                                                                     #this Letters are 3 Leds long
                return -5                                                                                      #space gets set to 4, so there are 2 Leds space
        elif cha == ' ' or cha == '.' or cha == '!' or cha == ',':
                return -3
        elif cha == '*':
                return -9
        else :                                                                                             #the other Letters are 4 Leds long
                return -6                                                                                      #space gets set to 5, so there are 2 Leds space

        
def write(letter,color,background):
        for i in range(0,LED_COUNT):
                showLED(strip, i ,background)

        if letter == 'a' :
                for pixel in CHAR_A:    
                        showLED(strip, pixel,color)
        elif letter == 'b' :
                for pixel in CHAR_B:    
                        showLED(strip, pixel,color)
        elif letter == 'c' :
                for pixel in CHAR_C:    
                        showLED(strip, pixel,color)
        elif letter == 'd' :
                for pixel in CHAR_D:    
                        showLED(strip, pixel,color)
        elif letter == 'e' :
                for pixel in CHAR_E:    
                        showLED(strip, pixel,color)
        elif letter == 'f' :
                for pixel in CHAR_F:    
                        showLED(strip, pixel,color)
        elif letter == 'g' :
                for pixel in CHAR_G:    
                        showLED(strip, pixel,color)
        elif letter == 'h' :
                for pixel in CHAR_H:    
                        showLED(strip, pixel,color)
        elif letter == 'i' :
                for pixel in CHAR_I:    
                        showLED(strip, pixel,color)
        elif letter == 'j' :
                for pixel in CHAR_J:    

                        showLED(strip, pixel,color)
        elif letter == 'k' :
                for pixel in CHAR_K:    
                        showLED(strip, pixel,color)
        elif letter == 'l' :
                for pixel in CHAR_L:    
                        showLED(strip, pixel,color)
        elif letter == 'm' :
                for pixel in CHAR_M:    
                        showLED(strip, pixel,color)
        elif letter == 'n' :
                for pixel in CHAR_N:    
                        showLED(strip, pixel,color)
        elif letter == 'o' :
                for pixel in CHAR_O:    
                        showLED(strip, pixel,color)
        elif letter == 'p' :
                for pixel in CHAR_P:    
                        showLED(strip, pixel,color)
        elif letter == 'q' :
                for pixel in CHAR_Q:    
                        showLED(strip, pixel,color)
        elif letter == 'r' :
                for pixel in CHAR_R:    
                        showLED(strip, pixel,color)
        elif letter == 's' :
                for pixel in CHAR_S:    
                        showLED(strip, pixel,color)
        elif letter == 't' :
                for pixel in CHAR_T:    
                        showLED(strip, pixel,color)
        elif letter == 'u' :
                for pixel in CHAR_U:    
                        showLED(strip, pixel,color)
        elif letter == 'v' :
                for pixel in CHAR_V:    
                        showLED(strip, pixel,color)
        elif letter == 'w' :
                for pixel in CHAR_W:    
                        showLED(strip, pixel,color)
        elif letter == 'x' :
                for pixel in CHAR_X:    
                        showLED(strip, pixel,color)
        elif letter == 'y' :
                for pixel in CHAR_Y:    
                        showLED(strip, pixel,color)
        elif letter == 'z' :
                for pixel in CHAR_Z:    
                        showLED(strip, pixel,color)
        elif letter != ' ' :
                print('Error: The written element does not exist')





#funktions for some animations

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


if __name__ == '__main__':
    """
    x = 3
    y = 4
    led = 6
    print('Das ID der LED für (3,4) ist:', COORDINATES_2_LEDID[y][x]) # Ausgabe ist 6
    print('Die Koordinaten für LED 6 sind x, y:', LEDID_2_COORDINATES[led][0], COORDINATES_2_LEDID[led][1])
    """
    pin_num = 0
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    reset(strip)
    #print('Bitte Text eingeben')
    text = input()

    #colorWipe(strip,Color(0,0,0))
    #colorWipe(strip,LED_BCKGRD)
    
    length = 0
    for CHA in text:
        length = length + 1
    MATRIX = np.zeros( (5, length*7+10) )

    for CHA in text:    
            #write(CHA,LED_COLOR,LED_BCKGRD)
            writeMatrix(CHA)
            space = makeSpace(CHA)
            print (space)
            MATRIX = matrixShift(MATRIX,space)

    if TEXT_ROUND != 0:
            for i in range(0,length*7*TEXT_ROUND+10*TEXT_ROUND):
                    showDisplay()
                    MATRIX = matrixShift(MATRIX,TEXT_STEPS*-1)
                    time.sleep(TEXT_SPEED)
    else:
            while True:
                    showDisplay()
                    MATRIX = matrixShift(MATRIX,TEXT_STEPS*-1)
                    time.sleep(TEXT_SPEED)

    #colorWipe(strip,Color(0,0,0))
    #rainbowCycle(strip)
            
    #print(LEDID_2_COORDINATES[0][0])
    reset(strip)

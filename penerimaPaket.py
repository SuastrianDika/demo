# This program allows a user to enter a
# Code. Jika tombol C ditekan, maka input akan reset
# Jika user menekan tombol A, input akan diperiksa.

import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from time import sleep
from camera import *

#kode barcode
scode=""
dummy = "8999909001909"

#kode oled
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
padding = 2
shape_width = 20
top = padding
bottom = height-padding

x = padding

x += shape_width+padding

x += shape_width+padding

x += shape_width+padding

font = ImageFont.load_default()

#kode ir
sensor = 23
#solenoid = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
#GPIO.setup(solenoid,GPIO.OUT)

#GPIO.output(solenoid,True)

def bukaPintu():
    print ("IR Sensor Ready.....")
    print (" ")

    #solenoid membuka pintu
    print('solenoid membuka pintu')
    
    i = 15
    while i > 0:
        time.sleep(1)
        print(i)
        i-=1

    try: 
       while True:
          if GPIO.input(sensor):
             print ("Pintu masih Terbuka")
             time.sleep(2)
             draw.text((x, top),    "Pintu Terbuka",  font=font, fill=255)
             disp.image(image)
             disp.display()
             draw.rectangle((0,0,width,height), outline=0, fill=0)
             #while GPIO.input(sensor):
                #time.sleep(1)
          else: 
             print("Pintu Tertutup")
             time.sleep(2)
             draw.text((x, top),    "Pintu Tertutup",  font=font, fill=255)
             disp.image(image)
             disp.display()
             draw.rectangle((0,0,width,height), outline=0, fill=0)
             
             #solenoid menutup pintu
             print('solenoid menutup pintu')
             print('masukkan nomor resi lagi')
             break                   
                          
    except KeyboardInterrupt:
        GPIO.cleanup()
   

#mengecek apakah barcode sesuai
while 1:   
    scode= str(input())  #will wait to get the input from barcode reader
    
    if(scode == dummy):
        print('Barcode SESUAI')
        #tampilkan dioled
        draw.text((x, top),    'BARCODE SESUAI',  font=font, fill=255)
        disp.image(image)
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        
        #buka pintu oleh solenoid
        bukaPintu()
        
        tangkapGambar()#tangkap gambar
        
        

    else:
        #jika barcode tidak sesuai
        print('Barcode TIDAK SESUAI')

        #tampilkan dioled
        draw.text((x, top),    'BARCODE TIDAK SESUAI',  font=font, fill=255)
        disp.image(image)
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        ulang = True
        while ulang :
        
            #kode keypad
            L1 = 26
            L2 = 19
            L3 = 13
            L4 = 6

            C1 = 12
            C2 = 16
            C3 = 20
            C4 = 21

            # The GPIO pin of the column of the key that is currently
            # being held down or -1 if no key is pressed
            keypadPressed = -1

            secretCode = "8999909001909"
            input = ""

            # Setup GPIO
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)

            GPIO.setup(L1, GPIO.OUT)
            GPIO.setup(L2, GPIO.OUT)
            GPIO.setup(L3, GPIO.OUT)
            GPIO.setup(L4, GPIO.OUT)

            # Use the internal pull-down resistors
            GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

            # This callback registers the key that was pressed
            # if no other key is currently pressed
            def keypadCallback(channel):
                global keypadPressed
                if keypadPressed == -1:
                    keypadPressed = channel

            # Detect the rising edges on the column lines of the
            # keypad. This way, we can detect if the user presses
            # a button when we send a pulse.
            GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
            GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
            GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
            GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)

            # Sets all lines to a specific state. This is a helper
            # for detecting when the user releases a button
            def setAllLines(state):
                GPIO.output(L1, state)
                GPIO.output(L2, state)
                GPIO.output(L3, state)
                GPIO.output(L4, state)

            def checkSpecialKeys():
                global input
                pressed = False

                GPIO.output(L3, GPIO.HIGH)

                if (GPIO.input(C4) == 1):
                    print("Input reset!");
                    pressed = True

                GPIO.output(L3, GPIO.LOW)
                GPIO.output(L1, GPIO.HIGH)

                if (not pressed and GPIO.input(C4) == 1):
                    if input == secretCode:
                        #tampilkan dioled
                        draw.text((x, top),    'SESUAI',  font=font, fill=255)
                        disp.image(image)
                        disp.display()
                        draw.rectangle((0,0,width,height), outline=0, fill=0)

                        #buka pintu oleh solenoid
                        bukaPintu()
                        
                        tangkapGambar()#tangkap gambar
                        
                        
                        #matikan perulangan
                        ulang = False
                        
                    else:
                        #tampilkan dioled
                        draw.text((x, top),    'TIDAK SESUAI',  font=font, fill=255)
                        disp.image(image)
                        disp.display()
                        draw.rectangle((0,0,width,height), outline=0, fill=0)
                        
                        
                    pressed = True

                GPIO.output(L3, GPIO.LOW)

                if pressed:
                    input = ""

                return pressed

            # reads the columns and appends the value, that corresponds
            # to the button, to a variable
            def readLine(line, characters):
                global input
                # We have to send a pulse on each line to
                # detect button presses
                GPIO.output(line, GPIO.HIGH)
                if(GPIO.input(C1) == 1):
                    input = input + characters[0]
                if(GPIO.input(C2) == 1):
                    input = input + characters[1]
                if(GPIO.input(C3) == 1):
                    input = input + characters[2]
                if(GPIO.input(C4) == 1):
                    input = input + characters[3]
                GPIO.output(line, GPIO.LOW)

            try:
                while True:
                    # If a button was previously pressed,
                    # check, whether the user has released it yet
                    if keypadPressed != -1:
                        setAllLines(GPIO.HIGH)
                        if GPIO.input(keypadPressed) == 0:
                            keypadPressed = -1
                        else:
                            time.sleep(0.1)
                    # Otherwise, just read the input
                    else:
                        if not checkSpecialKeys():
                            readLine(L1, ["1","2","3","A"])
                            readLine(L2, ["4","5","6","B"])
                            readLine(L3, ["7","8","9","C"])
                            readLine(L4, ["*","0","#","D"])
                            time.sleep(0.1)
                        else:
                            time.sleep(0.1)
            except KeyboardInterrupt:
                print("\nApplication stopped!")


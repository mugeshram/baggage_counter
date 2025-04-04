import RPi.GPIO as GPIO
import time
import cv2
from picamera2 import Picamera2
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys
from deepface import DeepFace
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)  
# File path
GPIO.output(6,False)
GPIO.output(12,False)
csv_file = "customers.csv"

# Read the CSV file
df = pd.read_csv(csv_file)

# Setup I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Create a persistent image buffer (keep all drawings)
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Example usage
oled.fill(0)
oled.show()

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
image_folder = "customer_imgs"
temp_folder = "temp_imgs"
# Set the Row Pins
ROW_1 = 17
ROW_2 = 27
ROW_3 = 22
ROW_4 = 5

# Set the Column Pins
COL_1 = 23
COL_2 = 24
COL_3 = 25
COL_4 = 16

GPIO.setwarnings(False)
# BCM numbering
GPIO.setmode(GPIO.BCM)

# Set Row pins as output
GPIO.setup(ROW_1, GPIO.OUT)
GPIO.setup(ROW_2, GPIO.OUT)
GPIO.setup(ROW_3, GPIO.OUT)
GPIO.setup(ROW_4, GPIO.OUT)

# Set column pins as input and Pulled up high by default
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

cur_customer = 1
max_customer = 2
customers = [6,12]
free_locks = [1 if not (customer in df['customer_id'].values) else 0 for customer in customers  ]


def draw_text_at(x, y, text,is_refresh=False):
    # Draw text without clearing other areas
    global image , draw , font
    if is_refresh:
       image = Image.new("1", (oled.width, oled.height))
       draw = ImageDraw.Draw(image)
       font = ImageFont.load_default()
    draw.text((x, y), text, font=font, fill=255)
    oled.image(image)
    oled.show()


#draw_text_at(0, 0, "Hello")



# function to read each row and each column
 
def readRow(line, characters):
    GPIO.output(line, GPIO.LOW)
    input_text = ""
    if(GPIO.input(COL_1) == GPIO.LOW):
        input_text += characters[0]
    if(GPIO.input(COL_2) == GPIO.LOW):
        input_text += characters[1]
    if(GPIO.input(COL_3) == GPIO.LOW):
       input_text += characters[2]
    if(GPIO.input(COL_4) == GPIO.LOW):
        input_text += characters[3]
    GPIO.output(line, GPIO.HIGH)
    return input_text

# Endless loop by checking each row

def get_char():
    input_text = ""
    while True:
        input_text = readRow(ROW_1, ["1","2","3","A"])
        if len(input_text) !=0 :
            break
        input_text =readRow(ROW_2, ["4","5","6","B"])
        if len(input_text) !=0 :
            break
        input_text =readRow(ROW_3, ["7","8","9","C"])
        if len(input_text) !=0 :
            break
        input_text =readRow(ROW_4, ["*","0","#","D"])
        if len(input_text) !=0 :
            break
        

            
        time.sleep(0.2) # adjust this per your own setup
    return input_text    
 
def get_number():
    temp = ""
    numbers = "0123456789"
    
    while True:
        draw_text_at(0, 0, "phone number",True)
        draw_text_at(0, 25, f"{temp}")
        
        c = get_char()
        if c in numbers:
           temp += c
        
        if c == "C":
            return None
        if c=="D":
            return temp
        
def get_photo(folder):
        draw_text_at(0, 0, "smile please",True)
        draw_text_at(0, 25, "press D")
        while True:
            if get_char() == 'D':
                break
            if get_char() == 'C':
                return False
        img = picam2.capture_array()
        try:
            os.remove(f"{folder}/img_{cur_customer}.jpg")
        except:
            pass
        cv2.imwrite(f"{folder}/img_{cur_customer}.jpg",img)
        return True
    

        
def check_photo(customer_id):
     img1 = image_folder + f"/img_{customer_id}.jpg"
     img2 = temp_folder + f"/img_{customer_id}.jpg"
     result = DeepFace.verify(
             img1_path = img1,
            model_name="VGG-Face" ,
             enforce_detection=False,
             img2_path = img2,
        )
     print(result)
     print(customer_id)
     return  False
    
try:


    while True:

        free_slots = [customers[i] for i,lock in enumerate(free_locks) if lock == 1]
        if not free_slots:
            draw_text_at(25, 25, f"Counter Full",True)
        else:
            draw_text_at(25, 25, f"Bagage Counter",True)
    
        c = get_char()
        if c =='A':
            number  = get_number()
            if number:
                cur_customer = free_slots[0]
                result = get_photo(image_folder)
                
                if result:
                   
                   if  cur_customer in df['customer_id'].values:
                       index = df[df['customer_id'] == cur_customer].index[0]
                       df.at[index, 'number'] = number  # Modify this line as per your requirement
                       
                   else:
                        new_entry = pd.DataFrame({'customer_id': [cur_customer], 'number': [number]})
                        df = pd.concat([df, new_entry], ignore_index=True)
                   free_locks[customers.index(cur_customer)] = 0
                   df.to_csv(csv_file, index=False)   
                   draw_text_at(25, 0, f"Use Locker",True) 
                   draw_text_at(25, 25, f"No: {cur_customer}")
                   while True:
                       button_state = GPIO.input(26)
                       if button_state == False:
                          GPIO.output(cur_customer,False)
                          
                          break
                       else:
                          GPIO.output(cur_customer,True) 
                   
        elif c == 'B':
            number  = get_number()
            if number:
                if number in df['number'].values:
                   index = df[df['number'] == number].index[0]
                   cur_customer_get = int(df.at[index,'customer_id'])
                   result = get_photo(temp_folder)
                   draw_text_at(25, 25, f"cheking...",True) 
                   if check_photo(int(cur_customer_get)):
                       draw_text_at(25, 0, f"Open Locker",True) 
                       draw_text_at(25, 25, f"No: {cur_customer_get}")
                       while True:
                             button_state = GPIO.input(26)
                             if button_state == False:
                                GPIO.output(cur_customer_get,False)
                                df = df[df['customer_id'] != cur_customer_get]
                                free_locks[customers.index(cur_customer_get)] = 1
                                df.to_csv(csv_file, index=False)
                                try:
                                  os.remove( image_folder + f"/img_{cur_customer_get}.jpg")
                                except:
                                    pass
                                try:
                                  os.remove( temp_folder + f"/img_{cur_customer_get}.jpg")
                                except:
                                    pass
                                break
                             else:
                                GPIO.output(cur_customer_get,True)
                    
                   else:
                       draw_text_at(25, 0, f"Invalid User",True) 
                       time.sleep(4)
                   
                else :
                    draw_text_at(20, 0, f"No Bags Found",True)
                    time.sleep(4)
                    





except KeyboardInterrupt:
    print("\nKeypad Application Interrupted!")
    GPIO.cleanup()
    cv2.destroyAllWindows()


#!/usr/bin/env python3

import datetime
import os
import RPi.GPIO as GPIO
from picamzero import Camera
from gpiozero import MotionSensor
from time import sleep


# Set up LED pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def makeImageName():
    now = datetime.datetime.now()
    imageName = now.strftime("%Y%m%d%H%M%S")
    return imageName


def main():

    # Log
    print("BirdBot intializing...")

    # Declare variables
    Pir = MotionSensor(23)
    camera = Camera()
    imageDirect = "/home/rain/BirdBotV1/image_repo"

    # Make needed directories if they don't exist
    os.makedirs(imageDirect, exist_ok=True)

    # Log
    print("BirdBot ready for observations")
    
    try:
        # Begin observation loop

        while True:

            # Wait until motion is detected
            print("Waiting for activity...")
            Pir.wait_for_active()

            # Turn on signal LED
            GPIO.output(18, GPIO.HIGH)

            # Wait a moment for the movement to stop
            sleep(2)

            print("Activity detected")
            # Generate image name
            imageName = makeImageName()
            imageName = os.path.join(imageDirect, f"{imageName}.jpg")

            # take a photo
            camera.take_photo(imageName)
            print(f"Image captured, Saved:  {imageName}")


            # Turn off signal LED
            GPIO.output(18, GPIO.LOW)
            
            # Wait a little before allowing the next image to be taken
            sleep(10)

    except KeyboardInterrupt:
        print("exiting BirdBot")
        GPIO.cleanup()

if __name__ == "__main__":
    main()
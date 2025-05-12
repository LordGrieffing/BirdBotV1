
import datetime
import os
from picamera import PiCamera
from gpiozero import MotionSensor
from time import sleep




def makeImageName():
    now = datetime.datetime.now()
    imageName = now.strftime("%Y%m%d%H%M%S")
    return imageName


def main():

    # Log
    print("BirdBot intializing...")

    # Declare variables
    Pir = MotionSensor(23)
    camera = PiCamera()
    imageDirect = "image_repo"

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
            print("Activity detected")
            # Generate image name
            imageName = makeImageName()
            imageName = os.path.join(imageDirect, f"{imageName}.jpg")

            # take a photo
            camera.capture(imageName)
            print(f"Image captured, Saved:  {imageName}")

            # Wait a little before allowing the next image to be taken
            sleep(10)

    except KeyboardInterrupt:
        print("exiting BirdBot")
        camera.close()

if __name__ == "__main__":
    main()
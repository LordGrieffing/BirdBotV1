#!/usr/bin/env python3

import os
import shutil
import time
import RPi.GPIO as GPIO

IMAGE_DIR = "/home/rain/BirdBotV1/image_repo"
MOUNT_BASE = "/media/rain"

# Set up LED pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

def find_usb_drive():
    for entry in os.listdir(MOUNT_BASE):
        path = os.path.join(MOUNT_BASE, entry)
        if os.path.ismount(path):
            return path
    return None

def copy_files_to_usb(usb_path):

    # LED to signal that files are being transferred
    GPIO.output(18, GPIO.HIGH)

    target_dir = os.path.join(usb_path, "birdbot_images")
    os.makedirs(target_dir, exist_ok=True)
    print(f"Copying images to {target_dir}")
    for file in os.listdir(IMAGE_DIR):
        if file.endswith(".jpg"):
            src = os.path.join(IMAGE_DIR, file)
            dst = os.path.join(target_dir, file)
            if not os.path.exists(dst):  # avoid overwriting
                shutil.copy2(src, dst)
                print(f"Copied: {file}")

                # Delete file once it has been transferred
                os.remove(src)
    
    print("Done copying files.")

    # Shut down LED signal
    GPIO.output(24, GPIO.LOW)
    GPIO.cleanup()

def main():
    print("USB watcher started.")
    seen = False
    while True:
        usb_path = find_usb_drive()
        if usb_path and not seen:
            print(f"USB detected: {usb_path}")
            copy_files_to_usb(usb_path)
            seen = True
        elif not usb_path:
            seen = False  # Reset when USB is removed
        time.sleep(5)

if __name__ == "__main__":
    main()
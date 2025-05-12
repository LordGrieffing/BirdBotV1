#!/usr/bin/env python3

import os
import shutil
import time

IMAGE_DIR = "/home/pi/BirdBotV1/image_repo"
MOUNT_BASE = "/media/pi"

def find_usb_drive():
    for entry in os.listdir(MOUNT_BASE):
        path = os.path.join(MOUNT_BASE, entry)
        if os.path.ismount(path):
            return path
    return None

def copy_files_to_usb(usb_path):
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
                os.remove(dst)
    
    print("Done copying files.")

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
import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

# Coordinates of the area to monitor for obstacles
# These values should be adjusted for your screen resolution
DINO_POSITION = (140, 360)  # Approximate position of the dino
MONITOR_AREA = (DINO_POSITION[0] + 100, DINO_POSITION[1], DINO_POSITION[0] + 200, DINO_POSITION[1] + 30)

def press_space():
    """Simulate a jump by pressing the space bar."""
    pyautogui.press("space")

def detect_obstacle():
    """Capture a part of the screen and detect obstacles based on pixel intensity."""
    screen = ImageGrab.grab(MONITOR_AREA)
    gray_image = ImageOps.grayscale(screen)
    pixel_sum = np.array(gray_image).sum()
    return pixel_sum < 7000  # Threshold to detect obstacles

def main():
    print("Starting Dino Game Bot...")
    print("Switch to the game window. Bot will start in 3 seconds.")
    time.sleep(3)

    while True:
        if detect_obstacle():
            press_space()
        time.sleep(0.05)  # Delay to control bot speed

if __name__ == "__main__":
    main()

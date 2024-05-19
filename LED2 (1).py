import tkinter as tk
from gpiozero import PWMLED
from time import sleep

# Set up the LEDs on different GPIO pins
red_led = PWMLED(17)   # Red LED on GPIO pin 17
green_led = PWMLED(27) # Green LED on GPIO pin 27
blue_led = PWMLED(22)  # Blue LED on GPIO pin 22

def set_red_brightness(value):
    """Set Red LED brightness."""
    brightness = float(value) / 100.0
    red_led.value = brightness

def set_green_brightness(value):
    """Set Green LED brightness."""
    brightness = float(value) / 100.0
    green_led.value = brightness

def set_blue_brightness(value):
    """Set Blue LED brightness."""
    brightness = float(value) / 100.0
    blue_led.value = brightness

# Set up the main window
root = tk.Tk()
root.title("LED Brightness Control")

# Create sliders for each LED
red_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', label="Red LED Brightness",
                      command=set_red_brightness)
red_slider.pack()

green_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', label="Green LED Brightness",
                        command=set_green_brightness)
green_slider.pack()

blue_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', label="Blue LED Brightness",
                       command=set_blue_brightness)
blue_slider.pack()

# Start the GUI loop
root.mainloop()

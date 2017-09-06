import RPi.GPIO as GPIO
import pygame
from pygame.locals import *
from time import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.OUT)
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Documents/python-pir-mp3/cascata.mp3")
while True:
    x=GPIO.input(5)
    
    if x!=0: 
        GPIO.output(6, 1)
        if pygame.mixer.music.get_busy() != True :
            pygame.mixer.music.play()
    else: 
		GPIO.output(6, 0)
    sleep(0.1)

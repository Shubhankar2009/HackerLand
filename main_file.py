# Importing
import numpy as np
import pygame
import cv2
from cvzone.HandTrackingModule import HandDetector
from pygame import mixer

# Initializing
pygame.init()
mixer.init()


# Creating Window
window = pygame.display.set_mode((1240, 720))
pygame.display.set_caption("My fingertips are drum stick")

# Initialize Clock for FPS
fps = 60
clock = pygame.time.Clock()

# Our Webcam
video = cv2.VideoCapture(0)
video.set(3, 1280)  # width
video.set(4, 720)  # height

previous_time = 0
detector = HandDetector(detectionCon=0.8, maxHands=1)
# MediaPipe Finger Tips
finger_tips = [4, 8, 12, 16, 20]

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # OpenCV

    ret, img = video.read()
    hands, img = detector.findHands(img)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    RGB_img = np.rot90(RGB_img)
    img_to_blit = pygame.surfarray.make_surface(RGB_img).convert()
    img_to_blit = pygame.transform.flip(img_to_blit, True, False)

    if hands:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        number = fingers1.count(1)
        print(number)

        # Adding Music

        if number == 1:
            mixer.music.load("audio/1.mp3")
            mixer.music.play()

        if number == 2:
            mixer.music.load("audio/2.mp3")
            mixer.music.play()

        if number == 3:
            mixer.music.load("audio/3.mp3")
            mixer.music.play()

        if number == 4:
            mixer.music.load("audio/4.mp3")
            mixer.music.play()

        if number == 5:
            mixer.music.load("audio/5.mp3")
            mixer.music.play()

    window.blit(img_to_blit, (0, 0))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)

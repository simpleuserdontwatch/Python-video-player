import tkinter as tk
import tkinter.simpledialog as s

import numpy as np

root = tk.Tk()
root.withdraw()
framerate = int(s.askstring(title="enter frame rate", prompt="enter frame rate"))
video = s.askstring("enter video path", "enter video path")
b = s.askstring("", "enable pixelation? [y/n]") == "y"
if b:
    a = s.askstring("", "enter resolution (x y)").split()
    a = list(map(int, a))
    xp, yp = a
import time

import cv2

cap = cv2.VideoCapture(video)


def pixelate(img, w, h):
    height, width = img.shape[:2]
    temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)


while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 350))
    if b:
        frame = pixelate(frame, xp, yp)
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.getWindowProperty("video", cv2.WND_PROP_VISIBLE) < 1:
        break
    time.sleep(1 / framerate)
cv2.destroyAllWindows()

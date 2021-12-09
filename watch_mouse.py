#!/usr/bin/env python3

from pynput import mouse
import math

amnt = 0
prepos = [0.0, 0.0]
dot_pitch = 0.1554 #(mm)

def on_move(x, y):
    global amnt
    global prepos
    dist = math.sqrt((prepos[0] - x) ** 2 + (prepos[1] - y) ** 2)
    amnt = amnt + dist
    print("Distance: {:4.2f}cm, Amount: {:4.2f}cm".format(dist * dot_pitch * 0.1, amnt * dot_pitch * 0.1))
    prepos = [x, y]

with mouse.Listener(on_move=on_move) as listener:
    listener.join()
    listener.start()
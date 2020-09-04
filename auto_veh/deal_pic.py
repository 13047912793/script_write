
import time
import math
from pynput.mouse import Button, Controller

for i in range (3, 0, -1):
    print(i)
    time.sleep(1)

def HeartPoint(t):
    x = 500 + 19.5 * (16 * math.pow(math.sin(t), 3))
    y = 500 - 20 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
    return (x, y)


mouse = Controller()
(x0, y0) = HeartPoint(0)
mouse.position = (x0, y0)
for i in range(0, 100):
    t = (i / 5) / math.pi
    time.sleep(0.05)
    mouse.press(Button.left)
    mouse.position = HeartPoint(t)
    mouse.release(Button.left)

mouse.press(Button.left)
mouse.position = (x0, y0)
mouse.release(Button.left)


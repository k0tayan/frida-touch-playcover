import time

from lib.touch import FridaTouch, SimulateTouch, TouchType

touch = FridaTouch()
while True:
    touch.post_simulate_touch(SimulateTouch(0, 600, 1000, TouchType.PRESS))
    touch.post_simulate_touch(SimulateTouch(1, 1200, 1000, TouchType.PRESS))
    time.sleep(0.5)
    touch.post_simulate_touch(SimulateTouch(0, 600, 1000, TouchType.MOVE))
    touch.post_simulate_touch(SimulateTouch(1, 1200, 1000, TouchType.MOVE))
    time.sleep(0.5)
    touch.post_simulate_touch(SimulateTouch(0, 600, 1000, TouchType.RELEASE))
    touch.post_simulate_touch(SimulateTouch(1, 1200, 1000, TouchType.RELEASE))
    time.sleep(0.5)

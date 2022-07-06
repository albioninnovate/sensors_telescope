import PicoRobotics
import time

board = PicoRobotics.KitronikPicoRobotics()
#directions = ["f", "r"]
directions = ["f"]

while True:
    board.step(1, "f",100)
    #board.step(2, direction,8)

    board.stepAngle(1,"r", 180)
    time.sleep(0.5)  # pause between directions



import sys
import time
import gopigo
import robot_util



def handleCommand(command, keyPosition, price=0):

    # only uses pressing down of keys
    if keyPosition != "down":
        return

    print("handle command", command, keyPosition)


    if command == 'L':
        gopigo.left_rot()
        time.sleep(0.15)
        gopigo.stop()
    if command == 'R':
        gopigo.right_rot()
        time.sleep(0.15)
        gopigo.stop()
    if command == 'F':
        gopigo.forward()
        time.sleep(0.4)
        gopigo.stop()
    if command == 'B':
        gopigo.backward()
        time.sleep(0.3)
        gopigo.stop()

    robot_util.handleSoundCommand(command, keyPosition, price)



# working code foe working of usg sensor on itself without frontend
import time

from pymata4 import pymata4

count=0
trigpin=10
ecopin=13

board=pymata4.Pymata4()

def the_callback(data):
    global count
    print("distance: ", data[2])
    # print("data0: ", data[0])
    # print("data1: ", data[1])
    # if data[2] < 100:
    #     print("Distnce :")

board.set_pin_mode_sonar(trigpin,ecopin,the_callback)

while True:
    try:
        time.sleep(0.1)
        board.sonar_read(trigpin)
        time.sleep(5000)
    except Exception:
        board.shutdown()




# working code foe working of usg sensor on itself without frontend
import time

from pymata4 import pymata4

count=0
trigpin=10
ecopin=13

board=pymata4.Pymata4()

def the_callback(data):
    global count
    print("distance: ", data[2])

board.set_pin_mode_sonar(trigpin,ecopin,the_callback)

while True:
    try:
        time.sleep(0.1)
        board.sonar_read(trigpin)
        time.sleep(5000)
    except Exception:
        board.shutdown()


import time
import threading
from pymata4 import pymata4
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pymata4 import pymata4
from random import randrange
count2=0
def task():
    count=0

    trigpin=10
    ecopin=13

    board=pymata4.Pymata4()

    def the_callback(data):
        global count
        global count2
        count2=data[2]
        print("distance: ", data[2])
        # return data[2]


    board.set_pin_mode_sonar(trigpin,ecopin,the_callback)

    while True:
        try:
            time.sleep(0.1)
            board.sonar_read(trigpin)
            time.sleep(5000)
        except Exception:
            board.shutdown()


fig = plt.figure(figsize=(6, 3))
x = [0]
y = [0]

ln, = plt.plot(x, y, '-')
# plt.axis([0, 100, 0, 10])
plt.axis([0,300, 0, 200])
def update(frame):
    x.append(x[-1] + 1)
    # y.append(randrange(0, 10))
    y.append(count2)
    ln.set_data(x, y)
    return ln,
thread = threading.Thread(target=task)

# Start the thread
thread.start()
animation = FuncAnimation(fig, update, interval=500)
plt.show()

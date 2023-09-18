import time
import threading
from pymata4 import pymata4
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pymata4 import pymata4
from random import randrange
import queue
from collections import deque

alpha = 0.1

plt.style.use('Solarize_Light2')
class ExponentialSmoothing:
    def __init__(self, alpha):
        self.alpha = alpha
        self.queue = deque()
        self.smoothed_value = None

    def add_data_point(self, value):
        self.queue.append(value)

    def smooth(self):
        if not self.queue:
            return None

        if self.smoothed_value is None:
            self.smoothed_value = self.queue.popleft()
        else:
            current_value = self.queue.popleft()
            self.smoothed_value = self.alpha * current_value + (1 - self.alpha) * self.smoothed_value

        return self.smoothed_value


exp_smoother = ExponentialSmoothing(alpha)

count2 = 0
smoothed_value = 0
temp=0


# my_queue = queue.Queue()
# smoothed_data =queue.Queue()

# def exponential_smoothing(alpha, data_stream):

#     prev_smoothed = data_stream[0]  # Initial value for the first data point

#     for data_point in data_stream:
#         smoothed = alpha * data_point + (1 - alpha) * prev_smoothed
#         smoothed_data.append(smoothed)
#         prev_smoothed = smoothed

#     return smoothed_data


# # Apply exponential smoothing to the data
# smoothed_data = exponential_smoothing(alpha, my_queue)
def task():
    count = 0

    trigpin = 10
    ecopin = 13

    board = pymata4.Pymata4()

    def the_callback(data):
        global count
        global count2
        global temp
        count2 = data[2]
        # my_queue.put(count2)
        exp_smoother.add_data_point(count2)
        smoothed_value = exp_smoother.smooth()
        temp=smoothed_value
        print("distance: ", data[2], " ==", smoothed_value)
        # return data[2]

    board.set_pin_mode_sonar(trigpin, ecopin, the_callback)

    while True:
        try:
            time.sleep(0.1)
            board.sonar_read(trigpin)
            time.sleep(5000)
        except Exception:
            board.shutdown()


# fig = plt.figure(figsize=(6, 3))
# x = [0]
# y = [0]
#
# ln, = plt.plot(x, y, '-')
# plt.tight_layout()
# # plt.axis([0, 100, 0, 10])
# plt.axis([0, 300, 0, 200])
#
#
# def update(frame):
#     x.append(x[-1] + 1)
#     # y.append(randrange(0, 10))
#     # item1=my_queue.get()
#     y.append(temp)
#     ln.set_data(x, y)
#     plt.tight_layout()
#     return ln,

# fig, ax = plt.subplots()
fig = plt.figure(figsize=(6, 3))
plt.axis([0, 30, 0, 200])
xdata, ydata = [], []
xdata2, ydata2 = [], []
ln, = plt.plot([], [], '-b')
ln2, = plt.plot([], [], '--r')


# def init():
#     ax.set_xlim(0, 2 * np.pi)
#     ax.set_ylim(-1, 1)
#     return ln, ln2


def update(frame):
    xdata.append(frame)
    ydata.append(temp)
    ln.set_data(xdata, ydata)

    xdata2.append(frame)
    ydata2.append(count2)
    ln2.set_data(xdata2, ydata2)
    # plt.axis([(frame-20), 30, 0, 200])
    # plt.axis([30,(frame - 20), 0, 200])
    plt.axis([(0+frame-300), (30+frame), 0, 200])
    plt.tight_layout()
    return ln, ln2




thread = threading.Thread(target=task)

# Start the thread
thread.start()
animation = FuncAnimation(plt.gcf(), update, interval=500)
plt.tight_layout()
plt.show()

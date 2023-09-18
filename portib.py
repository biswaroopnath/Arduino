# import threading
# import time
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from pymata4 import pymata4
# from collections import deque
#
# window_size=3
# startptr = 0
# qu = deque()
# qu2=deque()
# def moving_avg(q,w):
#     sum2 = 0
#
#
#     if len(q) < w:
#         return q[len(q)-1]
#     # print(s)
#     # s=s+1
#     startptr+=1
#     # print(s)
#     for  i  in range(startptr,startptr+w):
#         sum2+=q[i]
#     return sum2/w
#
#
#
#
#
#
#
#
#
#
# alpha = 0.15
#
# plt.style.use('Solarize_Light2')
#
#
# # exp_smoother = ExponentialSmoothing(alpha)
#
# count2 = 0
# smoothed_value = 0
# temp=0
#
#
# def task():
#     count = 0
#
#     trigpin = 10
#     ecopin = 13
#
#     board = pymata4.Pymata4()
#
#     def the_callback(data):
#         global count
#         global count2
#         global temp
#         count2 = data[2]
#         qu.append(count2)
#         # my_queue.put(count2)
#         # exp_smoother.add_data_point(count2)
#         smoothed_value = moving_avg(qu,window_size)
#         temp=smoothed_value
#         print("distance: ", data[2], " ==", smoothed_value)
#         # return data[2]
#
#     board.set_pin_mode_sonar(trigpin, ecopin, the_callback)
#
#     while True:
#         try:
#             time.sleep(0.1)
#             board.sonar_read(trigpin)
#             time.sleep(5000)
#         except Exception:
#             board.shutdown()
#
#
#
# fig = plt.figure(figsize=(6, 3))
# plt.axis([0, 30, 0, 200])
# xdata, ydata = [], []
# xdata2, ydata2 = [], []
# ln, = plt.plot([], [], '-b')
# ln2, = plt.plot([], [], '--r')
#
#
#
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(temp)
#     ln.set_data(xdata, ydata)
#
#     xdata2.append(frame)
#     ydata2.append(count2)
#     ln2.set_data(xdata2, ydata2)
#
#     plt.axis([(0+frame-300), (30+frame), 0, 200])
#     plt.tight_layout()
#     return ln, ln2
#
#
#
#
# thread = threading.Thread(target=task)
#
#
# thread.start()
# animation = FuncAnimation(plt.gcf(), update, interval=500)
# plt.tight_layout()
# plt.show()
#
#
# # class ExponentialSmoothing:
# #     def __init__(self, alpha):
# #         self.alpha = alpha
# #         self.queue = deque()
# #         self.smoothed_value = None
# #
# #     def add_data_point(self, value):
# #         self.queue.append(value)
# #
# #     def smooth(self):
# #         if not self.queue:
# #             return None
# #         if self.smoothed_value is None:
# #             self.smoothed_value = self.queue.popleft()
# #         else:
# #             current_value = self.queue.popleft()
# #             self.smoothed_value = self.alpha * current_value + (1 - self.alpha) * self.smoothed_value
# #
# #         return self.smoothed_value


import threading
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pymata4 import pymata4
from collections import deque

window_size = 7
startptr = 0
qu = deque()
qu2 = deque()

def moving_avg(q, w):
    sum2 = 0
    if len(q) < w:
        return q[len(q) - 1]
    global startptr
    startptr += 1
    for i in range(startptr, startptr + w):
        idx = i % len(q)
        sum2 += q[idx]
    return sum2 / w

alpha = 0.15

plt.style.use('Solarize_Light2')

count2 = 0
smoothed_value = 0
temp = 0

def task():
    trigpin = 10
    ecopin = 13
    board = pymata4.Pymata4()

    def the_callback(data):
        global count2
        global temp
        count2 = data[2]
        qu.append(count2)
        smoothed_value = moving_avg(qu, window_size)
        temp = smoothed_value
        print("distance: ", data[2], " ==", smoothed_value)

    board.set_pin_mode_sonar(trigpin, ecopin, the_callback)

    while True:
        try:
            time.sleep(0.1)
            board.sonar_read(trigpin)
            time.sleep(5)  # Use 5 seconds instead of 5000 milliseconds
        except Exception:
            board.shutdown()

fig = plt.figure(figsize=(6, 3))
plt.axis([0, 30, 0, 200])
xdata, ydata = [], []
xdata2, ydata2 = [], []
ln, = plt.plot([], [], '-b')
ln2, = plt.plot([], [], '--r')

def update(frame):
    xdata.append(frame)
    ydata.append(temp)
    ln.set_data(xdata, ydata)

    xdata2.append(frame)
    ydata2.append(count2)
    ln2.set_data(xdata2, ydata2)

    plt.axis([(0 + frame - 300), (30 + frame), 0, 200])
    plt.tight_layout()
    return ln, ln2

thread = threading.Thread(target=task)
thread.start()
animation = FuncAnimation(plt.gcf(), update, interval=500)
plt.tight_layout()
plt.show()

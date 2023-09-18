import time
import requests
from pymata4 import pymata4



def the_callback(data):
    global count

    distance = data[2]
    print("distance:", distance)


# def hello(data):
#     global count
#
#     distance = data[0]
#     print("distance:", distance)


    # Send the distance data to the server
    url = 'https://emgbackend.onrender.com/api/entry'
    payload = {'distance': distance}
    headers = {'Content-Type': 'application/json'}


    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print("Data sent successfully")

    except requests.exceptions.RequestException as e:
        print("Failed to send data:", str(e))

while True:
    try:
        count = 0
        trigpin = 10
        ecopin = 13

        board = pymata4.Pymata4()
        # time.sleep(0.1)

        # board.sonar_read(trigpin)
        # h=hello(board.sonar_read(trigpin))
        board.set_pin_mode_sonar(trigpin, ecopin, the_callback)
        board.send_reset()
        # board.shutdown()
        # time.sleep(5)

    except Exception as e:

        print(e)
        board.shutdown()

# import time
# from flask import Flask, jsonify
#
# from pymata4 import pymata4
#
# app = Flask(__name__)
# board = pymata4.Pymata4()
# trigpin = 10
# ecopin = 13
#
# def the_callback(data):
#     distance = data[2]
#     print("Distance:", distance)
#     # You can perform any further processing or send the data via API here
#
# board.set_pin_mode_sonar(trigpin, ecopin, the_callback)
#
#
# @app.route('/send_data', methods=['POST'])
# def send_data():
#     try:
#         board.sonar_read(trigpin)
#         return jsonify({'message': 'Data sent successfully'})
#     except Exception as e:
#         return jsonify({'message': 'Error occurred', 'error': str(e)})
#
#
# if __name__ == '__main__':
#     app.run()
#


import time
from flask import Flask, jsonify, request

from pymata4 import pymata4

app = Flask(__name__)
board = pymata4.Pymata4()
trigpin = 10
ecopin = 13

def the_callback(data):
    distance = data[2]
    print("Distance:", distance)
    send_data(distance)  # Send the data via the API


board.set_pin_mode_sonar(trigpin, ecopin, the_callback)


@app.route('/send_data', methods=['POST'])
def send_data(distance):
    try:
        # Extract the data from the POST request
        distance = request.get_json()
        # Process the received data or perform any desired actions
        # ...

        return jsonify({'message': 'Data received and processed successfully'})
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)})


if __name__ == '__main__':
    app.run()

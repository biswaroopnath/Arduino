# import asyncio
# from pymata4 import pymata4
# from ably import AblyRealtime
# from pymongo import MongoClient
# import time
#
# trigpin = 10
# ecopin = 13
#
# board = pymata4.Pymata4()
#
# # Ably credentials
#
#
# # MongoDB connection details
# uri = 'mongodb://username:password@cluster0.c1mxulq.mongodb.net/test'
# client = MongoClient(uri)
# db = client['test']
# collection = db['emg_distance123']
#
#
# async def main():
#     ably = AblyRealtime('9xMJmA.N3AF_w:aGUrVGNOBW7qw7hqV9FNR9G1FLAllwLrjkoyb9Rj0Nw')
#     ably.connection.on('connected', lambda state: print('Ably connected:', state))
#     ably.connection.on('failed', lambda state: print('Ably connection failed:', state))
#
#     async def on_sensor_data(data):
#         distance = data[2]
#
#         # Publish to Ably channel
#         await ably.channels.get('distance_emg123').publish('message', distance)
#
#     async def on_message(msg):
#         # Insert received message into MongoDB
#         result = collection.insert_one(msg.data)
#
#     await ably.channels.get('distance_emg123').subscribe(on_message)
#
#     while True:
#         try:
#             board.set_pin_mode_sonar(trigpin, ecopin, on_sensor_data)
#             time.sleep(1)  # Delay to allow data to be read
#
#         except Exception as e:
#             print(e)
#             board.shutdown()
#
#
# if __name__ == '_main_':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()

import random
import time
import logging
import requests

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)


def send_random_numbers():
    while True:
        random_number = random.randint(1, 200)
        logger.info(f'Sending random number: {random_number}')

        payload = {'content': random_number}
        try:
            response = requests.post('https://dweet.io:443/dweet/for/random_numbers', data=payload)
            if response.status_code == 200:
                logger.info('Random number sent successfully')
            else:
                logger.warning('Failed to send random number')
        except requests.exceptions.RequestException as e:
            logger.error(f'Error occurred while sending random number: {e}')

        time.sleep(1)


if __name__ == '__main__':
    send_random_numbers()
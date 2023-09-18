from ably import AblyRealtime
from pymongo import MongoClient
from random import randint
from urllib.parse import quote_plus
import time
import asyncio

username = "parthib"
password = "Parthib@123"

username = quote_plus(username)
password = quote_plus(password)

# Connect to MongoDB
uri = f'mongodb+srv://{username}:{password}@cluster0.c1mxulq.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(uri)
db = client['test']
collection = db['emg_distance123']


def on_message(msg):
    result = collection.insert_one(msg.data)
    if result.acknowledged:
        print('Data successfully inserted!')
    else:
        print('Failed to insert data into MongoDB!')


async def publish_messages(channel):
    while True:
        await channel.publish(name='message', data={'value': randint(0, 100)})
        print('Published message:', {'value': randint(0, 100)})
        await asyncio.sleep(1)


async def main():
    ably = AblyRealtime('9xMJmA.N3AF_w:aGUrVGNOBW7qw7hqV9FNR9G1FLAllwLrjkoyb9Rj0Nw')
    ably.connection.on('connected', lambda state: print('Ably connected:', state))
    ably.connection.on('failed', lambda state: print('Ably connection failed:', state))

    channel = ably.channels.get('distance_emg123')
    await channel.subscribe(on_message, lambda info: print('Subscribed to channel:', info))
    await publish_messages(channel)


if __name__ == '_main_':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
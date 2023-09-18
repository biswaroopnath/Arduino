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


if __name__ == '_main_':
    send_random_numbers()
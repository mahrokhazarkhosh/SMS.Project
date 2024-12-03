#importing necessary libraries

import redis
import requests

#Setting up Redis connection

redis_client = redis.StricRedis(host='localhost', port=6379, db=0)

#Function to get phone numbers from user input

def get_phone_numbers():
    phone_numbers = input('Enter your phone number: ')
    return phone_numbers.split(',')

#Function to store phone numbers in Redis

def store_numbers_in_redis(numbers):
    for number in numbers:
        redis_client.sadd('phone_numbers', number)

#Function to send SMS using a placeholder SMS API

def send_sms(phone_number,message):
    api_url = 'http://api.fanyi.baidu.com'
    api_key = '<KEY>'
    payload = {
        'api_url': api_url,
        'api_key': api_key,
        'message': message,
    }
    response = requests.post(api_url, json=payload)
    return response.status_code()


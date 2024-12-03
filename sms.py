#importing necessary libraries

import redis
import requests

#Setting up Redis connection

redis_client = redis.StricRedis(host='localhost', port=6379, db=0)

#Function to get phone numbers from user input

def get_phone_numbers():
    phone_numbers = input('Enter your phone number: ')
    return phone_numbers.split(',')
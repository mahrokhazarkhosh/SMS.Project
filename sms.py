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
#Main function to execute the program
if __name__ == '__main__':
    phone_numbers = get_phone_numbers()
    store_numbers_in_redis(phone_numbers)

#Retrieve numbers from Redis and send sms

message = "This is a test message"
for phone_number in redis_client.smembers('phone_numbers'):
    status = send_sms(phone_number.decode(),message)
    if status == 200:
        print(f"Message sent to {phone_number.decode()}")
    else:
        print(f"Message failed to send to {phone_number.decode()}")
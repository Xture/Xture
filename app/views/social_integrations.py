import requests
from flask import request, redirect
from app import logger

try:
    from config import secrets
except:
    logger.error('No vk secrets')

VK_SIGNUP_URL = 'https://oauth.vk.com/access_token/'
VK_PROFILE_URL = 'https://api.vk.com/method/users.get'


def vk_signup(code):
    client_id = secrets.VK_CLIENT_ID
    redirect_uri = secrets.VK_REDIRECT_URI
    client_secret = secrets.VK_CLIENT_SECRET
    logger.debug({'client_id': client_id, 'redirect_uri': redirect_uri,
                  'client_secret': client_secret, 'code': code})
    data = requests.post(VK_SIGNUP_URL, params={'client_id': client_id, 'redirect_uri': redirect_uri,
                         'client_secret': client_secret, 'code': code}).json()
    logger.debug(data['user_id'])

    return data['access_token'], data['user_id']


def get_profile_data(access_token, uid):
    logger.debug(VK_PROFILE_URL)
    data = requests.get(VK_PROFILE_URL, params={'user_id': uid})
    logger.debug(data.json())
    return data.json()['response'][0]

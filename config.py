import os

mobileme_enabled = False
mobileme_username = ''
mobileme_password = ''

if os.environ['SERVER_SOFTWARE'] == 'Development/1.0':
    twitter_consumer_key = ''
    twitter_consumer_secret = ''
else:
    twitter_consumer_key = ''
    twitter_consumer_secret = ''
    
fts_enabled = False
fts_server = ''
fts_username = ''
fts_password = ''

# change this for deploy is you can registration from http://www.google.com/recaptcha
recaptcha_public_key = '6Ldn4c8SAAAAAODv7r0pTQn0BYOZDW3qFdN2_-YL'
recaptcha_private_key = '6Ldn4c8SAAAAAJoKvcZNVvIcNwBpxQNDMBG6r5X5'

daydream_secret = ''

site_key = ''
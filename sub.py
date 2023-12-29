import requests
from http.cookiejar import MozillaCookieJar

def subscribe_to_channel(channel_id):
    # Load the cookies from the cookies.txt file
    cookies = MozillaCookieJar()
    cookies.load('cookies.txt', ignore_expires=True, ignore_discard=True)

    # Create a session and apply the cookies
    session = requests.session()
    session.cookies = cookies

    # Send the POST request to subscribe to the channel
    url = f'https://www.youtube.com/subscription_ajax?action_create_subscription_to_channel={channel_id}'
    response = session.post(url)

    # Check if the subscription was successful
    if response.status_code == 200:
        print('Subscribed successfully!')
    else:
        print('Failed to subscribe.')

channel_id = 'UCn4rEMqKtwBQ6-oEwbd4PcA'
subscribe_to_channel(channel_id)

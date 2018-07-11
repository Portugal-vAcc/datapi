__author__ = 'Nick Harasym 1115151'

from requests_oauthlib import OAuth1
import requests


class VatsimSSO():

    def __init__(self,
                 base_url,
                 consumer_key,
                 consumer_secret,
                 callback_uri=None,
                 oauth_allow_suspended=0,
                 oauth_allow_inactive=0):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.call_backuri = callback_uri
        self.base_url = base_url
        self.verifier = None
        self.token = None
        self.oauth_allow_suspended = oauth_allow_suspended
        self.request_token = None
        self.oauth_allow_inactive = oauth_allow_inactive

    def login_token(self):
        extra_params = {'oauth_allow_suspended': self.oauth_allow_suspended,
                        'oauth_allow_inactive': self.oauth_allow_inactive}

        prepare = OAuth1(self.consumer_key,
                         client_secret=self.consumer_secret,
                         callback_uri=self.call_backuri,
                         signature_method='HMAC-SHA1',
                         signature_type='query')

        request = requests.post(self.base_url + '/login_token/',
                                auth=prepare,
                                params=extra_params).json()
        print(request)
        self.request_token = request['token']['oauth_token']

        return str(self.request_token)

    def login_return(self):

        if self.verifier is None:
            return 'Please provide verifier'

        if self.token is None:
            return 'Please provide token'

        prepare = OAuth1(self.consumer_key,
                         client_secret=self.consumer_secret,
                         signature_method='HMAC-SHA1',
                         verifier=self.verifier,
                         resource_owner_key=self.token,
                         signature_type='query')
        request = requests.post(self.base_url + '/login_return/',
                                auth=prepare).json()
        return request

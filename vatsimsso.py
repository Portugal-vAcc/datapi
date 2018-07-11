from requests_oauthlib import OAuth1
import requests

class VatsimSSO():

    def __init__(self,
                 url,
                 key,
                 secret):
        self.url = url
        self.key = key
        self.secret = secret

    def get_oauth_token(self,
                        redirect='oob',
                        allow_suspended=False,
                        allow_inactive=False):
        """ Handles the first step of getting an oauth token from VATSIM.

        Store the token_secret somewhere and redirect the user to the login page
        with the token.
        """
        params = {'oauth_allow_suspended': 1 if allow_suspended else 0,
                  'oauth_allow_inactive': 1 if allow_inactive else 0}

        auth = OAuth1(
            self.key,
            client_secret=self.secret,
            callback_uri=redirect,
            signature_method='HMAC-SHA1',
            signature_type='query')

        request = requests.post(
            self.url + '/api/login_token/',
            auth=auth,
            params=params
        ).json()

        return request['token']

    def get_user_details(self, token, token_secret, verifier):
        """Queries VATSIM for an authenticated user's details.

        """
        auth = OAuth1(
            self.key,
            client_secret=self.secret,
            signature_method='HMAC-SHA1',
            verifier=verifier,
            resource_owner_key=token,
            resource_owner_secret=token_secret,
            signature_type='query')

        user = requests.post(
            self.url + '/api/login_return/',
            auth=auth
        ).json()

        return user

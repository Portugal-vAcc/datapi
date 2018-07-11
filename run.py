#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Portugal-vAcc Data API
Copyright (C) 2018  Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of Portugal-vAcc Data API.

Portugal-vAcc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Portugal-vAcc Data API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Portugal-vAcc Data API. If not, see <http://www.gnu.org/licenses/>.
"""
from eve import Eve
from flask import redirect, request, url_for
import os
from vatsimsso import VatsimSSO
import redis
import json

app = Eve()
redis = redis.from_url(app.config['REDIS_URL'], decode_responses=True)
vatsim = VatsimSSO(app.config['VATSIM_SSO_SERVER'],
                  key=app.config['VATSIM_SSO_KEY'],
                  secret=app.config['VATSIM_SSO_SECRET'])

@app.route('/login')
def login():
    oauth_token = vatsim.get_oauth_token(
        redirect=url_for('callback', _external=True))

    redirect_uri = (
          app.config['VATSIM_SSO_SERVER']
        + '/auth/pre_login/?oauth_token=%s'
    ) % oauth_token['oauth_token']

    redis.set(oauth_token['oauth_token'], oauth_token['oauth_token_secret'])
    redis.expire(oauth_token['oauth_token'], 3600)

    return redirect(redirect_uri, code=302)

@app.route('/callback')
def callback():
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    oauth_token_secret = redis.get(oauth_token)
    redis.delete(oauth_token)

    response = vatsim.get_user_details(
        oauth_token,
        oauth_token_secret,
        oauth_verifier)

    if response['request']['result'] == 'success':
        return json.dumps(response['user']), 200

    return json.dumps(response['request']['message']), 401

port = int(os.environ.get('PORT', 5000))
debug = port == 5000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=debug)

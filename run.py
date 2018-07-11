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
from vatsimsso import VatsimSSO
# from redis import StrictRedis, ConnectionPool
import os

app = Eve()

@app.route('/login')
def login():
    # advise VATSIM
    vatsimsso = VatsimSSO(app.config['VATSIM_SSO_SERVER'],
                          consumer_key=app.config['VATSIM_SSO_KEY'],
                          consumer_secret=app.config['VATSIM_SSO_SECRET'],
                          callback_uri=url_for('callback'))

    oauth_token = vatsimsso.login_token()
    redirect_uri = (app.config['VATSIM_SSO_SERVER'] +
                    '/pre_login/?oauth_token=%s') % oauth_token

    # store the user request
    # redis = StrictRedis()
    # redis.connection_pool = ConnectionPool.from_url(app.config['REDIS_URL'])
    # redis.set(oauth_token, False)

    return redirect(redirect_uri, code=302)

@app.route('/callback')
def callback():
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    # redis = StrictRedis()
    # redis.connection_pool = ConnectionPool.from_url(app.config['REDIS_URL'])
    # status = redis.get(oauth_token)

    vatsimsso = VatsimSSO(app.config['VATSIM_SSO_SERVER'],
                          consumer_key=app.config['VATSIM_SSO_KEY'],
                          consumer_secret=app.config['VATSIM_SSO_SECRET'])
    vatsimsso.token = status
    vatsimsso.verifier = oauth_verifier
    user = vatsimsso.login_return()

    print(user)

port = int(os.environ.get('PORT', 5000))
debug = port == 5000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=debug)

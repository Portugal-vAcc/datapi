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
import os

# live: https://cert.vatsim.net/sso/api
# demo: http://sso.hardern.net/server/api
VATSIM_SSO_SERVER = os.environ.get('VATSIM_SSO_SERVER',
                                   'http://sso.hardern.net/server/api')

# Public demo credentials
# VATSIM_SSO_KEY = os.environ.get('VATSIM_SSO_KEY', 'SSO_DEMO')
# VATSIM_SSO_SECRET = os.environ.get('VATSIM_SSO_SECRET',
#                                    'js8Sm7nit-2a_~k_~My6_~')

# vACC credentials
# see
#   demo credentials: https://forums.vatsim.net/viewtopic.php?f=134&t=65319
VATSIM_SSO_KEY = os.environ.get('VATSIM_SSO_KEY', r'SSO_DEMO_VACC')
VATSIM_SSO_SECRET = os.environ.get('VATSIM_SSO_SECRET', r'04i_~ruVUE.1-do1--sc')

MONGO_URI = os.environ.get('MONGO_URI',
                           'mongodb://localhost:27017/vaccdatapi')
REDIS_URL = os.environ.get('REDIS_URL',
                           'redis://localhost:6379')

DOMAIN = {}

X_DOMAINS = '*'
X_HEADERS = [
    'content-type',
    'if-match',
    'if-none-match',
]

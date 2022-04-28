import json

import jwt

class Token:

    def __init__(self, data):
        '''
        Gets the data from a request
        :param data: retrieved data
        '''
        self.data = data

    @property
    def token(self):
        return self.data['Authorization'].split()[1]

    @property
    def decoded_token(self):
        return jwt.decode(self.token, 'supersecret', algorithm='HS256')

    @property
    def identity(self):
        return self.decoded_token['identity']

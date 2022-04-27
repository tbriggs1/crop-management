import json

import jwt


class Token:

    def __init__(self, data):
        '''
        Gets the data from a request
        :param data: retrieved data
        '''
        self.data = data
        self.token = ""
        self.decoded_value = ""

    def set_token(self):
        self.token = self.data['Authorization']

    def decode_token(self):
        print(self.token)
        decoded = jwt.decode(self.token, algorithms="HS256")
        print(decoded)

    def get_decoded_token(self):
        pass
import requests
import collections
from robot.api import logger

buffer_base_path = '/bufferfile'


class BufferLibrary(object):

    def __init__(self):
        self._status = ''
        self.consumedElement = ''

    def create_new_buffer(self, base_url, name, path, max_size):
        body = {'name': name, 'father': path, 'max_size': max_size}
        response = requests.post(base_url + buffer_base_path, json=body)
        self._status = response.status_code

    def delete_existing_buffer(self, base_url, path):
        response = requests.delete(base_url + buffer_base_path + '?path=' + path)
        self._status = response.status_code

    def consume_existing_buffer(self, base_url, path):
        response = requests.get(base_url + '/bufferfile?path=' + path)
        if response.status_code == 200:
            self.consumedElement = response.json().get('content')
        self._status = response.status_code

    def put_existing_buffer(self, base_url, path, info):
        body = {'path': path, 'info': info}
        response = requests.put(base_url + buffer_base_path, json=body)
        self._status = response.status_code

    def compare_with_buffer_content(self, content):
        if content == self.consumedElement:
            self._status = 'Match'
        else:
            self._status = 'No Match'

    def move_buffer_to_new_folder(self, base_url, move_from, move_to):
        response = requests.patch(base_url + buffer_base_path + '?move_to=' + move_to + '&move_from=' + move_from)

        self._status = response.status_code

    def buffer_status_should_be(self, expected_status):
        if str(expected_status) != str(self._status):
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

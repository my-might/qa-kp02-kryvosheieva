import requests
import collections
from robot.api import logger

directory_base_path = '/directory'


class DirectoryLibrary(object):

    def __init__(self):
        self._status = ''
        self._directory_content = []

    def create_new_directory(self, base_url, name, path, max_elements):
        body = {'name': name, 'father': path, 'max_elems': max_elements}
        response = requests.post(base_url + directory_base_path, json=body)
        self._status = response.status_code

    def delete_existing_directory(self, base_url, path):
        response = requests.delete(base_url + directory_base_path + '?path=' + path)
        self._status = response.status_code

    def list_existing_directory(self, base_url, path):
        response = requests.get(base_url + '/directory?path=' + path)
        if response.status_code == 200:
            self._directory_content = response.json().get('children')
        self._status = response.status_code

    def compare_with_directory_content(self, content):
        if collections.Counter(content) == collections.Counter(str(self._directory_content)):
            self._status = 'Match'
        else:
            self._status = 'No Match'

    def move_directory_to_new_folder(self, base_url, move_from, move_to):
        response = requests.patch(base_url + directory_base_path + '?move_to=' + move_to + '&move_from=' + move_from)
        self._status = response.status_code

    def status_should_be(self, expected_status):
        if str(expected_status) != str(self._status):
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def reset_db(self, base_url):
        response = requests.put(base_url + '/reset')

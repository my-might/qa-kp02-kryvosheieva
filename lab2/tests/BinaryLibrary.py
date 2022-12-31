import requests

binary_file_base_path = '/binaryfile'


class BinaryLibrary(object):

    def __init__(self) -> None:
        super().__init__()
        self._status = ''
        self._file_content = ''

    def create_new_binary_file(self, base_url, name, path, content):
        response = requests.post(base_url + binary_file_base_path, json={'name': name, 'father': path, 'info': content})
        self._status = response.status_code

    def find_binary_file(self, base_url, path):
        response = requests.get(base_url + binary_file_base_path + '?path=' + path)
        if response.status_code == 200:
            self._file_content = response.json().get('content')
        self._status = response.status_code

    def delete_binary_file(self, base_url, path):
        response = requests.delete(base_url + binary_file_base_path + '?path=' + path)
        self._status = response.status_code

    def move_existing_binary_file(self, base_url, move_from, move_to):
        response = requests.patch(base_url + binary_file_base_path + '?move_from=' + move_from + '&move_to=' + move_to)
        self._status = response.status_code

    def expect_binary_file_content(self, expect_binary_file_content):
        if self._file_content != expect_binary_file_content:
            raise AssertionError("Expected binary file content is '%s' but was '%s'."
                                 % (expect_binary_file_content, self._file_content))

    def binary_status_should_be(self, expected_status):
        if str(expected_status) != str(self._status):
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))


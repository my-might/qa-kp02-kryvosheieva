import requests

logtext_base_path = '/logtextfile'


class LogTextLibrary(object):

    def __init__(self):
        self._status = ''
        self._logtext_content = ''

    def create_new_logtext_file(self, base_url, name, path):
        body = {'name': name, 'father': path}
        response = requests.post(base_url + logtext_base_path, json=body)
        self._status = response.status_code

    def delete_existing_logtext_file(self, base_url, path):
        response = requests.delete(base_url + logtext_base_path + '?path=' + path)
        self._status = response.status_code

    def append_line_to_logtext_file(self, base_url, path, content):
        body = {'path': path, 'info': content}
        response = requests.put(base_url + logtext_base_path, json=body)
        self._status = response.status_code

    def find_existing_logtext_file(self, base_url, path):
        response = requests.get(base_url + logtext_base_path + '?path=' + path)
        self._status = response.status_code
        if response.status_code == 200:
            self._logtext_content = response.json().get('content')

    def move_existing_logtext_file(self, base_url, move_from, move_to):
        response = requests.patch(base_url + logtext_base_path + '?move_to=' + move_to + '&move_from=' + move_from)
        self._status = response.status_code

    def logtext_content_should_be(self, expected_content):
        if self._logtext_content != expected_content:
            raise AssertionError("Expected content to be '%s' but was '%s'."
                                 % (expected_content, self._logtext_content))

    def logtext_status_should_be(self, expected_status):
        if str(expected_status) != str(self._status):
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

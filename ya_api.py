from pprint import pprint
import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, yadisk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": yadisk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, yadisk_file_path: str, filename: str):
        href_json = self._get_upload_link(yadisk_file_path=yadisk_file_path)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input(r'Введите полный путь на компьютере к файлу: ')
    path_only_name = os.path.basename(path_to_file)
    token = input('Введите свой токен: ')
    uploader = YaUploader(token=token)

    uploader._get_upload_link(path_only_name)

    result = uploader.upload(path_only_name, path_to_file)
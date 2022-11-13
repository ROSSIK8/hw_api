import requests
from settings import TOKEN
class Yandex:
    base_host = 'https://cloud-api.yandex.net/'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        requests_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(requests_url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка призошла успешно!')
        else:
            print('Ошибка')


if __name__ == '__main__':
    disk = Yandex(TOKEN)
    disk.upload_to_disk('C:\\Users\\ayuro\\OneDrive\\Изображения\\Saved Pictures\\luzaru.png', '/luzaru.png')
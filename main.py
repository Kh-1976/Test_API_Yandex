import requests

token_ya = 'yandex_token'


class YaUploader:

  def __init__(self, token_ya):
    self.token = token_ya

  def get_headers(self):
    return {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'OAuth {}'.format(self.token)
    }

  def new_folder(self):
    new_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': 'New_Folder'}
    response = requests.put(new_folder_url, headers=self.get_headers(), params=params)
    resp_get = requests.get(new_folder_url, headers=self.get_headers(), params=params)
    
    if response.status_code == 201:
      return resp_get.status_code
      #print('Папка New_Folder создана')
    else:
      return resp_get.status_code

if __name__ == '__main__':
  ya = YaUploader(token_ya)
  print(ya.new_folder())

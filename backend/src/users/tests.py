from django.test import TestCase
import os
import requests
import json

ENDPOINT = 'http://localhost:8000/api/users/register/'
image_path = os.path.basename(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'media', 'default', 'no-image.png'))
headers = {
    'Content-Type': 'application/json',
}
print(image_path);

# def do_img(method='POST', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#
#     if img_path is not None:
#         with open(img_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     return r
#
# do_img(method='put', data={'firstname': 'Kim','lastname': 'Toston'}, is_json=False, img_path=image_path)

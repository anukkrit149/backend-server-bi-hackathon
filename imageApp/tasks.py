"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

import requests


def ml_model(image_id, image_url):
    requests.post(url='http://65.1.33.297/image',
                  data={'image_id': image_id, 'image_url': image_url})
    return
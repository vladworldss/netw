# coding: utf-8
from urllib.parse import urlencode
from urllib.request import urlopen
import json

from settings import google_key


def google_geo(addr, key):
    params = {'address': addr,
              'key': key,
              'output': 'json',
              'oe': 'utf8'
              }
    base_addr = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url = '{}{}'.format(base_addr, urlencode(params))
    rawreply = urlopen(url).read()
    reply = json.loads(rawreply)
    return reply['results'].pop()


if __name__ == '__main__':
    addr = '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    res = google_geo(addr, google_key)
    print('address_components={}'.format(res['address_components']))

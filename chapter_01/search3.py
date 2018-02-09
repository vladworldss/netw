# coding: utf-8
import json
from http.client import HTTPConnection, HTTPSConnection
from urllib.parse import urlencode


from settings import google_key


def google_geo_http_req(addr, key):
    params = {'address': addr,
              'key': key,
              'output': 'json',
              'oe': 'utf8'
              }

    path = '/maps/api/geocode/json?'+urlencode(params)

    connect = HTTPSConnection('maps.googleapis.com')
    connect.request('GET', path)
    rawreply = connect.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    return reply


if __name__ == '__main__':
    addr = '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    res = google_geo_http_req(addr, google_key)
    print('address_components={}'.format(res['address_components']))

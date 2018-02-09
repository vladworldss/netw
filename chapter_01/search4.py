import socket

from settings import google_key


def google_sock_con(addr, key):
    s = socket.socket()
    s.connect(('maps.googleapis.com', 80))

    s.sendall(
        b'GET /maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH'
        b'&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'
        b'Host: maps.google.com:80\r\n'
        b'User-Agent: search4.py\r\n'
        b'Connection: close\r\n'
        b'\r\n'
    )
    rawreply = s.recv(4096)
    rawreply = rawreply.decode('utf-8')
    return rawreply


if __name__ == '__main__':
    addr = '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    res = google_sock_con(addr, google_key)
    print('address_components={}'.format(res['address_components']))
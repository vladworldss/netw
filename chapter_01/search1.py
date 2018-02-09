# coding: utf-8
from googlemaps import Client
from datetime import datetime

from settings import google_key


def google_maps_request(addr, key):
    gmaps = Client(key=key)

    # Geocoding an address
    geocode_result = gmaps.geocode(addr)
    print('geocode_result={}'.format(geocode_result))

    #  Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    print('reverse_geocode_result={}'.format(reverse_geocode_result))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(
        origin="Sydney Town Hall",
		destination="Parramatta, NSW",
		mode="transit",
		departure_time=now
	)
    print('directions_result={}'.format(directions_result))


if __name__ == '__main__':
    addr = '1600 Amphitheatre Parkway, Mountain View, CA'
    google_maps_request(addr, google_key)


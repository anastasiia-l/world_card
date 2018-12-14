import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDrk9pUPzya8KpMS5rUh4EVDpCIHsLmLBg')


def get_geometry(address):
    location_info = gmaps.geocode(address)
    return (location_info[0]['geometry']['location']['lat'],
            location_info[0]['geometry']['location']['lng'])


def get_address(location):
    location_info = gmaps.reverse_geocode(location)
    return location_info[0]['formatted_address']


a = get_geometry('Бучмы 20 Харьков')
b = get_address(a)
print(b)

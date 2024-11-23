import googlemaps

class GoogleMapsAPI:
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)

    def get_tourist_spots(self, city="Lahore"):
        """Fetch tourist spots in the given city."""
        query = f"tourist spots in {city}"
        places_result = self.gmaps.places(query=query)
        
        spots = []
        for place in places_result['results']:
            spot = {
                'name': place['name'],
                'location': place['geometry']['location'],
                'address': place.get('formatted_address', 'No address provided'),
                'rating': place.get('rating', 'No rating available')
            }
            spots.append(spot)
        
        return spots

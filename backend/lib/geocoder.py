"""Methods for geocoding with Geocodio or Open Street Map."""
import os

from geocodio import GeocodioClient
from geocodio.exceptions import GeocodioAuthError, GeocodioDataError  # noqa: F401

import osmnx as ox


class GeocodioCoder():
    """Geocodio geocoder class."""

    def __init__(self, api_key=os.environ.get('GEOCODIO_KEY', None)):
        """Initialize Geocodio geocoder class."""
        self.client = GeocodioClient(api_key)

    def geocode(self, address):
        """Geocode a single point with geocodio."""
        result = self.client.geocode(address)
        return {
            'address': address,
            'latitude': result.coords[0],
            'longitude': result.coords[1]
        }

    def geocode_batch(self, addresses):
        """
        Geocode a list of addressed with geocodio.

        Returns a list of tuples with addresses, and coordinates in the format:
        [(address, (long, lat)), ...]
        """
        results = self.client.geocode(addresses)
        return [{
            'address': address,
            'latitude': results.get(address).coords[0],
            'longitude': results.get(address).coords[1]
        } for address in addresses]


class OxCoder():
    """Open Street Maps geocoder class."""

    def __init__(self, api_url=None, api_key=None):
        """Initialize the geocoder class."""
        self.api_url = api_url
        self.api_key = api_key

    def geocode(self, address):
        """Geocode a single address with OSM."""
        try:
            result = ox.geocode(address)
            return {
                'address': address,
                'latitude': result[0],
                'longitude': result[1]
            }
        except:
            return None


def get_geocoder(name):
    """Return an instantiated geocoder of the required class."""
    return GEOCODER_NAME_TO_FUNCTION_MAPPING[name.lower()]()


GEOCODER_NAME_TO_FUNCTION_MAPPING = {
    'geocodio': GeocodioCoder,
    'oxcoder': OxCoder
}

from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """
        parent_id = area_id
        names = []
        while parent_id is not None:
            node = API.get_area(parent_id)
            names.append(node.name)
            parent_id = node.parent_id
        return ', '.join(names[::-1])

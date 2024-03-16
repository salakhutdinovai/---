from api import API, TreeNode
from geocoders.geocoder import Geocoder
from typing import Union


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: Union[int, None] = None, data: Union[list[TreeNode], None] = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _search(self, target_area_id, nodes, path=None):
        for node in nodes:
            if node.id == target_area_id:
                return [node.name]
            path = self._search(target_area_id, node.areas, path)
            if path and len(path):
                path.append(node.name)
                return path
        return path

    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Сделать перебор дерева для каждого area_id
            - В ходе перебора возвращать массив элементов, состоящих из TreeNode необходимой ветки
            - Из массива TreeNode составить полный адрес
        """
        area_id = str(area_id)
        path = self._search(area_id, self.__data)
        return ', '.join(path[::-1])

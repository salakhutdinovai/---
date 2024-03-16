from api import TreeNode, API
from geocoders.geocoder import Geocoder
from typing import Union
from collections import defaultdict


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: Union[int, None] = None, data: Union[list[TreeNode], None] = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

        self.path_dict = defaultdict(list)
        self.data_initialization()

    def data_initialization(self):
        """
            TODO:
            Сделать функцию перебора дерева:
            - Для каждого узла сохранять в словарь адресов
        """
        for node in self.__data:
            self.path_dict[node.id].append(node.name)
            self._search(node)

    def _search(self, parent_node):
        for node in parent_node.areas:
            self.path_dict[node.id].extend(self.path_dict[parent_node.id])
            self.path_dict[node.id].append(node.name)
            self._search(node)

    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Возвращать данные из словаря с адресами
        """
        return ', '.join(self.path_dict[str(area_id)])

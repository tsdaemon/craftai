import reflex as rx

from craftai.entities.base import Listable


class Connector(rx.Base, Listable):
    name: str
    connector_type: str
    connector_data: dict[str, str]

    def check_search_string(self, value: str) -> bool:
        return value.lower() in self.name.lower() or value.lower() in self.connector_type.lower()

    @classmethod
    def sort_attributes(cls) -> list[str]:
        return ["name", "connector_type"]

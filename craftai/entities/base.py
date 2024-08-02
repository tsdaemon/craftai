import abc

import reflex as rx


class Listable(rx.Base, abc.ABC):
    """Base class for entities which can be used in a list."""

    @abc.abstractmethod
    def check_search_string(self, value: str) -> bool:
        pass

    @abc.abstractmethod
    @classmethod
    def sort_attributes(cls) -> list[str]:
        pass

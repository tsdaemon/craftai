import abc
from typing import Any


class BaseConnectorType(abc.ABC):
    def __init__(self, config: dict[str, Any]):
        self.raw_config = config

    @abc.abstractmethod
    def get_tools(self) -> None:
        pass

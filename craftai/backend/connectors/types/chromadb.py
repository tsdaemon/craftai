from typing import Any

from craftai.backend.connectors.types.base import BaseConnectorType
from craftai.entities.config.chromadb import ChromaDbConfig


class ChromaDbConnectorType(BaseConnectorType):
    def __init__(self, config: dict[str, Any]):
        super().__init__(config)
        self.config = ChromaDbConfig.from_dict(config)

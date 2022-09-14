from dataclasses import dataclass
from typing import Dict, Union


@dataclass
class Meta:
    event_version: int
    interfaces: Dict[str, Dict[str, Union[str, int]]]

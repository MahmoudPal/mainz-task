import uuid
from typing import Dict, Any


class BaseEvent:
    def __init__(self, lead: Dict[str, Any]):
        self.lead = lead
        self.event_id = str(uuid.uuid4())

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError

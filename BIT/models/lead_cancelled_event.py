from models.base_event import BaseEvent
from typing import Dict, Any
from constants import EVENT_LEAD_CANCELLED, COL_ID, COL_EVENT_TYPE, COL_EVENT_EMPLOYEE, COL_EVENT_DATE, COL_EVENT_LEAD_ID, COL_UPDATED_DATE, COL_CANCELLATION_DATE, COL_CANCELLED_EMPLOYEE, UNKNOWN_EMPLOYEE


class LeadCancelledEvent(BaseEvent):
    def to_dict(self) -> Dict[str, Any]:
        return {
            COL_ID: self.event_id,
            COL_EVENT_TYPE: EVENT_LEAD_CANCELLED,
            COL_EVENT_EMPLOYEE: self.lead.get(COL_CANCELLED_EMPLOYEE, UNKNOWN_EMPLOYEE),
            COL_EVENT_DATE: self.lead[COL_CANCELLATION_DATE],
            COL_EVENT_LEAD_ID: self.lead[COL_ID],
            COL_UPDATED_DATE: self.lead[COL_UPDATED_DATE]
        }

from models.base_event import BaseEvent
from typing import Dict, Any
from constants import EVENT_LEAD_REQUESTED_CANCELLATION, COL_ID, COL_EVENT_TYPE, COL_EVENT_EMPLOYEE, COL_EVENT_DATE, COL_EVENT_LEAD_ID, COL_UPDATED_DATE, COL_CANCELLATION_REQUEST_DATE, UNKNOWN_EMPLOYEE


class LeadRequestedCancellationEvent(BaseEvent):
    def to_dict(self) -> Dict[str, Any]:
        return {
            COL_ID: self.event_id,
            COL_EVENT_TYPE: EVENT_LEAD_REQUESTED_CANCELLATION,
            COL_EVENT_EMPLOYEE: UNKNOWN_EMPLOYEE,  # Always "Unknown" for this event
            COL_EVENT_DATE: self.lead[COL_CANCELLATION_REQUEST_DATE],
            COL_EVENT_LEAD_ID: self.lead[COL_ID],
            COL_UPDATED_DATE: self.lead[COL_UPDATED_DATE]
        }

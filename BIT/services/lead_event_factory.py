from typing import List, Dict
from models.lead_sold_event import LeadSoldEvent
from models.lead_requested_cancellation_event import LeadRequestedCancellationEvent
from models.lead_cancelled_event import LeadCancelledEvent
from models.lead_cancellation_rejected_event import LeadCancellationRejectedEvent
from constants import COL_CANCELLATION_REQUEST_DATE, COL_CANCELLATION_DATE, COL_CANCELLATION_REJECTION_DATE


class LeadEventFactory:
    @staticmethod
    def create_events(lead: Dict) -> List:
        events = [LeadSoldEvent(lead)]
        if lead.get(COL_CANCELLATION_REQUEST_DATE):
            events.append(LeadRequestedCancellationEvent(lead))
        if lead.get(COL_CANCELLATION_DATE):
            events.append(LeadCancelledEvent(lead))
        if lead.get(COL_CANCELLATION_REJECTION_DATE):
            events.append(LeadCancellationRejectedEvent(lead))
        return events

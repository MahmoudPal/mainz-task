from repository.data_repository import DataRepository
from services.lead_event_factory import LeadEventFactory


class LeadTransformer:
    def __init__(self, repository: DataRepository):
        self.repository = repository

    def transform(self):
        leads = self.repository.fetch_leads()
        all_events = [
            event.to_dict()
            for lead in leads for event in
            LeadEventFactory.create_events(lead)]

        self.repository.save_events(all_events)
        print(f"Inserted {len(all_events)} events into Snowflake.")

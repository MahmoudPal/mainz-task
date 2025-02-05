from typing import List, Dict, Any


class DataRepository:
    def fetch_leads(self) -> List[Dict[str, Any]]:
        """
        Public method to fetch leads.
        Wraps the internal _fetch_leads method with error handling.
        """
        try:
            return self._fetch_leads()
        except Exception as e:
            print("Error fetching leads: %s", e)
            raise

    def save_events(self, events: List[Dict[str, Any]]):
        """
        Public method to save events.
        Wraps the internal _save_events method with error handling.
        """
        try:
            self._save_events(events)
        except Exception as e:
            print("Error saving events: %s", e)
            raise

    def _fetch_leads(self) -> List[Dict[str, Any]]:
        """
        Internal method to be implemented by subclasses.
        Should contain the logic for fetching lead records.
        """
        raise NotImplementedError("Subclasses must implement _fetch_leads()")

    def _save_events(self, events: List[Dict[str, Any]]):
        """
        Internal method to be implemented by subclasses.
        Should contain the logic for saving event records.
        """
        raise NotImplementedError("Subclasses must implement _save_events()")

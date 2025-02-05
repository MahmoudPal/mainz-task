import snowflake.connector
from typing import List, Dict, Any
from repository.data_repository import DataRepository
from config import SNOWFLAKE_CONFIG
from constants import TABLE_COMPANY_LEADS, TABLE_LEAD_EVENTS, COL_EVENT_ID, COL_EVENT_TYPE, COL_EVENT_EMPLOYEE, COL_EVENT_DATE, COL_EVENT_LEAD_ID, COL_EVENT_UPDATED_DATE_UTC


class SnowflakeConn(DataRepository):
    def __init__(self):
        self.conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)

    def fetch_leads(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_COMPANY_LEADS}")
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def save_events(self, events: List[Dict[str, Any]]):
        cursor = self.conn.cursor()
        for event in events:
            cursor.execute(
                f"""
                INSERT INTO {TABLE_LEAD_EVENTS} ({COL_EVENT_ID}, {COL_EVENT_TYPE}, {COL_EVENT_EMPLOYEE}, {COL_EVENT_DATE}, {COL_EVENT_LEAD_ID}, {COL_EVENT_UPDATED_DATE_UTC})
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (event[COL_EVENT_ID],
                 event[COL_EVENT_TYPE],
                 event[COL_EVENT_EMPLOYEE],
                 event[COL_EVENT_DATE],
                 event[COL_EVENT_LEAD_ID],
                 event[COL_EVENT_UPDATED_DATE_UTC]))
        self.conn.commit()

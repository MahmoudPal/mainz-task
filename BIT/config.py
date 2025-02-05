import os
from dotenv import load_dotenv, find_dotenv

found_dotenv = find_dotenv('.env')

if not found_dotenv:
    raise FileNotFoundError(f"Your .env file is missing")


# Load environment variables from .env file
load_dotenv()

SNOWFLAKE_CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
}

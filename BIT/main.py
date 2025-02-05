from repository.snowflake_connector import SnowflakeConn
from services.lead_transformer import LeadTransformer

if __name__ == "__main__":
    snowflake_repo = SnowflakeConn()
    transformer = LeadTransformer(snowflake_repo)
    transformer.transform()

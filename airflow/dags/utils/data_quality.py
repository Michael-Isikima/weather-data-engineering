import great_expectations as ge
from utils.logger import get_logger

logger = get_logger("data_quality")


def validate_weather(df):
    logger.info("Starting data quality checks")

    ge_df = ge.from_pandas(df)

    ge_df.expect_column_values_to_not_be_null("timestamp")
    ge_df.expect_column_values_to_not_be_null("city")

    ge_df.expect_column_values_to_be_between("temperature", -60, 60)
    ge_df.expect_column_values_to_be_between("humidity", 0, 100)
    ge_df.expect_column_values_to_be_between("windspeed", 0, 300)
    ge_df.expect_column_values_to_be_between("precipitation", 0, 500)

    result = ge_df.validate()

    if not result["success"]:
        logger.error("Data quality checks failed")
        raise ValueError("Data quality validation failed")

    logger.info("Data quality checks passed successfully")

    return df

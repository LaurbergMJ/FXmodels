import eurostat
from config.app_config import fred_api_key
from fredapi import Fred


def get_fred_data(Series_id: str, startdate, enddate) -> list:
    fred = Fred(api_key=fred_api_key)
    data = fred.get_series(Series_id, observation_start=startdate, observation_end=enddate)
    return data
import eurostat
from config.app_config import fred_api_key
from fredapi import Fred


def get_fred_data(Series_id: str, startdate, enddate, freq) -> list:
    fred = Fred(api_key=fred_api_key)
    data = fred.get_series(Series_id, observation_start=startdate, observation_end=enddate, frequency=freq)
    return data

#def get_eurostat(Series_id: str, filter_pars: str) -> list:
#    euro_stat = eurostat.get_data_df(Series_id, filter_pars=filter_pars)
#    return euro_stat

def get_eurostat(Series_id: str) -> list:
    euro_stat = eurostat.get_data_df(Series_id)
    return euro_stat
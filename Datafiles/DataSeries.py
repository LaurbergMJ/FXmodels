#This file contains data structures for the different data series that will be retrived from the different kinds 
#public data vendors that are being used throughout the project
#Examples of such data vendors incluedes FRED, EUROSTAT, Bank of England, Swiss... etc.
#See the documentation files on "data sources" for a thorough introduction to the data sources involved in this project! 

#region Data from FRED
US_swap_rates = {
    "USSW1": "ICERATES1100USD1Y",
    "USSW2": "ICERATES1100USD2Y",
    "USSW5": "ICERATES1100USD5Y",
    "USSW10": "ICERATES1100USD10Y",
    "USSW20": "ICERATES1100USD20Y",
    "USSW30": "ICERATES1100USD30Y"}

rates_Spread = {
    "TED": "TEDRATE",
    "Bei_10y": "T10YIE",
    "Bei_5y": "T5YIE",
    "5Y5Y_infl_fwd": "T5YIFR",
    "Bei_20y":"T20YIEM",
    "Bei_30y": "T30YIEM",
    }

fx_pairs = {
    "EURUSD": "DEXUSEU",
    "Broad_Nom_USD": "DTWEXBGS",
    "USDJPY": "DEXJPUS",
    "GBPUSD": "DEXUSUK",
    "USDCAD": "DEXCAUS",
    "USDMXN": "DEXMXUS",
    "USDKRW": "DEXKOUS",
    "USDIDR": "DEXINUS",
    "BRLUSD": "DEXBZUS",
    "AUDUSD": "DEXUSAL",
    "USDTHB": "DEXTHUS",
    "CHFUSD": "DEXSZUS",
    "ZARUSD": "DEXSFUS",
    "USDSEK": "DEXSDUS",
    "USDNOK": "DEXNOUS",
    "USDDKK": "DEXDNUS"
    } 

macrodata_US = {
    "M2": "M2",
    "CPI": "CPIAUCSL",
    "PPI": "PPIACO",
    "IndProd": "INDPRO",
    "Imp": "IR",
    "Exp": "IQ",
    "Vix": "VIXCLS"
}

fred_data = {
    "M2": "M2",
    "CPI": "CPIAUCSL",
    "PPI": "PPIACO",
    "IndProd": "INDPRO",
    "Imp": "IR",
    "Exp": "IQ",
    "Vix": "VIXCLS",
    "TED": "TEDRATE",
    "Bei_10y": "T10YIE",
    "Bei_5y": "T5YIE",
    "5Y5Y_infl_fwd": "T5YIFR",
    "Bei_20y":"T20YIEM",
    "Bei_30y": "T30YIEM",
    "USSW1": "ICERATES1100USD1Y",
    "USSW2": "ICERATES1100USD2Y",
    "USSW5": "ICERATES1100USD5Y",
    "USSW10": "ICERATES1100USD10Y",
    "USSW20": "ICERATES1100USD20Y",
    "USSW30": "ICERATES1100USD30Y"
}

#endregion

#region Data from Eurostat

eurostat_data = {
    "HICP": "prc_hicp_midx",
    "PPI": "sts_inppd_m",
    "IndProd": "sts_inpr_m",
    "ext_trd": "ext_st_ea19sitc",
    "Yld_Crv": "IRT_EURYLD_M"
}
#endregion 

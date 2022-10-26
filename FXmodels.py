import numpy as np
import pandas as pd
from Utilities import helper_functions as fct
from Datafiles import DataSeries as dat 

startdate = "1/1/2010"
startdate_EU = '2010-01'
enddate = "8/1/2022"

frequency = "m"

list_of_FRED_data = ['IndProd', 'CPI', 'PPI', 'Vix', '5Y5Y_infl_fwd', 'Bei_10y', 'Imp', 'Exp']

fred_data = pd.DataFrame()


def get_fred_data(lst):
    #Loading all necessary data from FRED into a dataframe
    for x in lst:
        if not 'dates' in fred_data.columns:
            fred_data['dates'] = (fct.get_fred_data(dat.fred_data[x], startdate=startdate, enddate=enddate, freq=frequency).index)
        else:
            fred_data[x] = (fct.get_fred_data(dat.fred_data[x], startdate=startdate, enddate=enddate, freq=frequency).values)

    return fred_data 

cc = get_fred_data(list_of_FRED_data)

print(cc)

#print(fred_data)

#----------Trying to load data from Eurostat-----------------

#----------HICP-----------------
#data_hicp = fct.get_eurostat(dat.eurostat_data['HICP'])
#data_hicp.rename({'geo\TIME_PERIOD': 'geo'}, inplace=1, axis=1)
#idx = np.where((data_hicp['coicop'] == "CP00") & (data_hicp['unit'] == "I15") & (data_hicp['geo'] == "EA19"))
#data_hicp = data_hicp.loc[idx]
#data_hicp = data_hicp.loc[:,startdate_EU:]
#data_hicp = data_hicp.T
##print(len(data_hicp.index))

##----------Query for Imports and Exports series-----------------
#data_ext_trd = fct.get_eurostat(dat.eurostat_data['ext_trd'])

#idx_imp = np.where((data_ext_trd['indic_et'] == "IVU") & (data_ext_trd['stk_flow'] == "IMP") & (data_ext_trd['partner'] == "EA19") & (data_ext_trd['sitc06'] == "TOTAL"))
#data_imp_unit_val = data_ext_trd.loc[idx_imp]

#idx_exp = np.where((data_ext_trd['indic_et'] == "IVU") & (data_ext_trd['stk_flow'] == "EXP") & (data_ext_trd['partner'] == "EA19") & (data_ext_trd['sitc06'] == "TOTAL"))
#data_exp_unit_val = data_ext_trd.loc[idx_exp]

#data_imp_unit_val = data_imp_unit_val.loc[:,startdate_EU:]
#data_exp_unit_val = data_exp_unit_val.loc[:,startdate_EU:]
#data_imp_unit_val = data_imp_unit_val.T
#data_exp_unit_val = data_exp_unit_val.T
#data_imp_unit_val = data_imp_unit_val.reset_index(drop=True)
#data_exp_unit_val = data_exp_unit_val.reset_index(drop=True)
##print(f'len IMP: {len(data_imp_unit_val.values)} len EXP: {len(data_exp_unit_val.values)}')

##----------PPI Index-----------------
#data_prod_prc = fct.get_eurostat(dat.eurostat_data['PPI'])
#data_prod_prc.rename({'geo\TIME_PERIOD': 'geo'}, inplace=1, axis=1)
#idx_prod_prc = np.where((data_prod_prc['geo'] == "EA19") & (data_prod_prc['unit'] == "I15") & (data_prod_prc['s_adj'] == "NSA") & (data_prod_prc['nace_r2'] == "B-E36"))
#data_prod_prc = data_prod_prc.loc[idx_prod_prc]
#data_prod_prc = data_prod_prc.loc[:,startdate_EU:]
#data_prod_prc = data_prod_prc.T
#data_prod_prc = data_prod_prc.reset_index(drop=True)


##----------Industrial Production Index-----------------
#data_indu_prod = fct.get_eurostat(dat.eurostat_data['IndProd'])
#data_indu_prod.rename({'geo\TIME_PERIOD': 'geo'}, inplace=1, axis=1)
#idx_indu_prod = np.where((data_indu_prod['geo'] == "EA19") & (data_indu_prod['unit'] == "I15") & (data_indu_prod['s_adj'] == "SCA") & (data_indu_prod['nace_r2'] == "B-D"))
#data_indu_prod = data_indu_prod.loc[idx_indu_prod]
#data_indu_prod = data_indu_prod.loc[:,startdate_EU:]
#data_indu_prod = data_indu_prod.T
#data_indu_prod = data_indu_prod.reset_index(drop=True)

##print(data_indu_prod)

##----------Merging Eurostat data into combined DF-----------------
#combined_EU_data = pd.DataFrame()
#combined_EU_data['dates'] = data_hicp.index
#combined_EU_data.reset_index()
#combined_EU_data['EU_HICP'] = data_hicp.values
#combo = [combined_EU_data, data_imp_unit_val, data_exp_unit_val, data_prod_prc, data_indu_prod]

#combined_EU_data = pd.concat(combo, axis=1, ignore_index=True)
#combined_EU_data.columns = ['dates', 'HICP', 'IMP', 'EXP', 'PPI', 'IndProd']
#print(combined_EU_data)


##combined_data = fred_data.copy(deep=True)


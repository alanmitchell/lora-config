"""Utility routines related to sensors, needed by the configuration script.
"""

import pandas as pd

def read_sensor_file(fn):
    """Reads a text file containing sensor key and model information, and returns
    a list of dictionaries containing the key information.  This routine attempts
    to automatically determine the type of input file, e.g. Elsys CSV file from the
    manufacturer.
    """
    with open(fn) as fin:
        first_line = fin.readline()
        if 'SKU;' in first_line and 'FW;' in first_line:
            return read_elsys_file(fn)

    raise ValueError('Unknown Sensor file type.')

def read_elsys_file(fn):
    """Reads an Elsys CSV file and returns a list of dictionaries containing key 
    info for each sensor.
    """
    recs = []
    for _, row in pd.read_csv(fn, delimiter=';', dtype='str').iterrows():
        recs.append(dict(
            model = row.SKU,
            dev_eui = row.EUI,
            app_eui = row.AppEUI,
            app_key = row.AppKey
        ))
    
    return recs
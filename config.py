"""Configuration settings for the LoRaWAN sensor config application.
"""

# Frequency band designator for Things Netwwork V3.
frequency_plan_id = 'US_902_928_FSB_2'

# Constants that specify the LoRaWAN and PHY version
ver_1_0_2b = ('MAC_V1_0_2', 'PHY_V1_0_2_REV_B')

# List of Sensor Models supported and their characteristics.  Use lowercase for model.

sensor_models = {
    'elt2': {
        'lora_ver': ver_1_0_2b,
        'params': [                           # This list covers the built-in reading types
            ('temperature', 'deg F'), 
            ('humidity', '%RH'), 
            ('pressure', 'millibars'), 
            ('accel_x', 'Gs'), 
            ('accel_y', 'Gs'), 
            ('accel_z', 'Gs'), 
            ('vdd', 'Volts'),
        ],
        'ext_types': [                        # These are the possibilities for the external sensor
            ('Temperature', ('extTemperature', 'deg F')),
            ('Switch', ('digital', '1=On 0=Off')),
            ('Pulse', ('pulseAbs', 'count')),
            ('Voltage', ('analog', 'Volts'))
        ],
    },
    'eltlite': {
        'lora_ver': ver_1_0_2b,
        'params': [('vdd', 'Volts')],
        'ext_types': [
            ('Temperature', ('extTemperature', 'deg F')),
            ('Switch', ('digital', '1=On 0=Off')),
            ('Pulse', ('pulseAbs', 'count')),
            ('Voltage', ('analog', 'Volts'))
        ],
    },
    'ers': {
        'lora_ver': ver_1_0_2b,
        'params': [
            ('temperature', 'deg F'), 
            ('humidity', '%RH'),
            ('light', 'lux'),
            ('motion', 'count'),
            ('vdd', 'Volts'),
        ],
        'ext_types': [],
    },
    'ersco2': {
        'lora_ver': ver_1_0_2b,
        'params': [
            ('temperature', 'deg F'), 
            ('humidity', '%RH'),
            ('light', 'lux'),
            ('motion', 'count'),
            ('co2', 'ppm'),
            ('vdd', 'Volts'),
        ],
        'ext_types': [],
    },
    'erslite': {
        'lora_ver': ver_1_0_2b,
        'params': [
            ('temperature', 'deg F'), 
            ('humidity', '%RH'),
            ('vdd', 'Volts'),
        ],
        'ext_types': [],
    },
}

# This maps parameter suffixes to labels displayed in the BMON Sensor Title
param_to_label = {
    'accel_x': 'X Acceleration', 
    'accel_y': 'Y Acceleration',
    'accel_z': 'Z Acceleration', 
    'analog': 'Voltage', 
    'co2': 'CO2', 
    'digital': 'State', 
    'extTemperature': 'Temperature', 
    'humidity': 'Humidity', 
    'light': 'Light', 
    'motion': 'Motion', 
    'pressure': 'Pressure', 
    'pulseAbs': 'Pulse Count', 
    'temperature': 'Temperature', 
    'vdd': 'Battery Voltage',
    'snr': 'Signal SNR',
}

def param_label(param):
    """Returns a label for a sensor parameter.  'param' is the abbrev
    for that parameter.  If the parameter is not listed in the above mapping
    dictionary, the Title case version of the parameter abbreviation is returned.
    """
    return param_to_label.get(param, param.title())
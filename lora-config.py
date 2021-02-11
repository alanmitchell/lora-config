#!/usr/bin/env python3
"""Main script to start LoRaWAN sensor configuration program.
"""

import sys
from pathlib import Path
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

import config
import sensor_utils

# create the Window that collects the sensor CSV file to open,
# and the list of buildings.
layout = [
    [sg.Text("Sensor Information File:", font='Any 14')],
    [
        sg.In(size=(80, 1), enable_events=True, key="sensor-file"),
        sg.FileBrowse('Select Sensor File', file_types=(('CSV files', '*.csv'), ('All Files', '*.*'))),
    ],
    [sg.Text('')],
    [sg.Text('Building List', font='Any 14')],
    [sg.Text('One Row per building, each row has a Building Abbreviation and Building Name, separated by a colon.')],
    [sg.Multiline('Bldg1: Building Name', (50, 4), key='bldgs')],
    [sg.Text('')],
    [sg.Button('Continue', key='continue'), sg.Button('Cancel', key='cancel')],
]

win_init = sg.Window('Sensor Config Inputs', layout)

sensor_file = ''
bldgs = []
while True:
    event, values = win_init.read()
    if event == "continue":
        sensor_file = values['sensor-file']
        if not Path(sensor_file).is_file():
            sg.popup('The Sensor File entered does not exist.')
            continue
        try:
            bldgs = [lin.split(':') for lin in values['bldgs'].splitlines() if len(lin.strip())]
            bldgs = [(abbrev.strip(), title.strip()) for abbrev, title in bldgs]
        except:
            sg.popup_error('Bad format in Building List.  Exactly one colon per line is required.')
            continue
        break

    elif event == 'cancel' or event == sg.WIN_CLOSED:
        sys.exit(0)

win_init.close()

# Read the sensor file and make the Window that collects additional information for each
# sensor.
try:
    sensors = sensor_utils.read_sensor_file(sensor_file)
except Exception as e:
    sg.popup_error(f'Error reading Sensor File: {e}')
    sys.exit(0)

bldg_abbrevs = [abbrev for abbrev, _ in bldgs]
bldg_def = bldg_abbrevs[0]
rows = [
    [sg.Text('Select Building, External Sensor type, Enter Base Sensor Description, and Check Readings to include in BMON')],
]

for ix, s in enumerate(sensors):
    info = config.sensor_models[s['model'].lower()]
    desc = f"{s['model']}: {s['dev_eui'][-4:]}"
    ext_types = ['None'] + [typ for typ, _ in info['ext_types']]
    ext_def = 'None' if len(ext_types)==1 else ext_types[1]
    a_row = [
        sg.Text(desc),
        sg.Combo(bldg_abbrevs, bldg_def, key=f'{ix}-bldg', readonly=True),
        sg.Combo(ext_types, ext_def, key=f'{ix}-ext', readonly=True),
        sg.Input('', (20,1), key=f'{ix}-name'),
    ]
    a_row += [sg.Checkbox(param[0], True if param[0] != 'vdd' else False, key=f'{ix}-{param[0]}') for param in info['params']]
    a_row += [sg.Checkbox('snr', False, key=f'{ix}-snr')]
    rows.append(a_row)

rows.append([sg.Text('')])
rows.append([
    sg.Button('Make Things V3 JSON File', key='make-v3'), 
    sg.Button('Make Things V2 Text File', key='make-v2'),
    sg.Button('Make BMON Spreadsheet', key='make-bmon'),
    sg.Text('       '),
    sg.Button('Exit', key='exit'),
    ])

# Create the Window
window = sg.Window('Edit Sensors', [[sg.Column(rows, scrollable=True, size=(1200, 800))]])

def add_sensor_info(vals):
    """Adds info from User Input to list of sensors. 'vals' is the dictionary of values that
    come from the User Interface.  It is produced in the window.read() method of the event loop below.
    The 'sensors' list, created above outside of this method is modified by this method.
    """
    for ix, s in enumerate(sensors):
        # Get the configuration info for this sensor type
        info = config.sensor_models[s['model'].lower()]
        s['bldg_abbrev'] = vals[f'{ix}-bldg']
        s['bldg'] = dict(bldgs)[s['bldg_abbrev']]
        s['name'] = vals[f'{ix}-name']
        s['lora_ver'] = info['lora_ver']

        # make a list of the selected reading parameters
        params = []

        # Start with the external sensor
        ext = vals[f'{ix}-ext']
        if ext != 'None':
            ext_param = dict(info['ext_types'])[ext]
            params.append(ext_param)

        # Loop the internal sensors to see if they are requested by the GUI
        for nm, unit in info['params']:
            if vals[f'{ix}-{nm}']:
                params.append( (nm, unit) )

        # Check for SNR request
        if vals[f'{ix}-snr']:
            params.append( ('snr', 'dB') )
        
        # Add the final list to the sensor record
        s['params'] = params
        
    return

# Create an event loop
while True:
    event, values = window.read()

    try:
        # End program if user closes window or
        # presses the OK button
        if event == "exit" or event == sg.WIN_CLOSED:
            break

        elif event == 'make-v3':
            add_sensor_info(values)
            file_contents = sensor_utils.make_things_v3_file(sensors)
            fn = sg.popup_get_file(
                'File to Save into.',
                default_extension='json',
                save_as=True,
                file_types=(('JSON Files', '*.json'),),
                no_window=True,
                )
            open(fn, 'w').write(file_contents)
            sg.popup_ok('Successful Creation of File!')

        elif event == 'make-v2':
            add_sensor_info(values)
            file_contents = sensor_utils.make_things_v2_file(sensors)
            fn = sg.popup_get_file(
                'File to Save into.',
                default_extension='txt',
                save_as=True,
                file_types=(('Text Files', '*.txt'),),
                no_window=True,
                )
            open(fn, 'w').write(file_contents)
            sg.popup_ok('Successful Creation of File!')
        
        elif event == 'make-bmon':
            add_sensor_info(values)
            fn = sg.popup_get_file(
                'File to Save into.',
                default_extension='xlsx',
                save_as=True,
                file_types=(('Excel Files', '*.xlsx'),),
                no_window=True,
                )
            sensor_utils.write_bmon_spreadsheet(sensors, fn)
            sg.popup_ok('Successful Creation of File!')

    except Exception as e:
        sg.popup_error(str(e))

window.close()

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
            sg.popup('Bad format in Building List.  Exactly one colon per line is required.')
            continue
        break
    if event == 'cancel' or event == sg.WIN_CLOSED:
        sys.exit(0)

win_init.close()

# Read the sensor file
try:
    sensors = sensor_utils.read_sensor_file(sensor_file)
except Exception as e:
    sg.popup(f'Error: {e}')
    sys.exit(0)


bldg_abbrevs = [abbrev for abbrev, _ in bldgs]
bldg_def = bldg_abbrevs[0]
rows = []
for ix, s in enumerate(sensors):
    info = config.sensor_models[s['model'].lower()]
    desc = f"{s['model']}: {s['dev_eui'][-4:]}"
    ext_types = ['None'] + [typ for typ, _ in info['ext_types']]
    ext_def = 'None' if len(ext_types)==1 else ext_types[1]
    a_row = [
        sg.Text(desc),
        sg.Combo(bldg_abbrevs, bldg_def, key=f'{ix}-bldg'),
        sg.Combo(ext_types, ext_def, key=f'{ix}-ext'),
        sg.Input('', (20,1), key=f'{ix}-name'),
    ]
    a_row += [sg.Checkbox(sens[0], True if sens[0] != 'vdd' else False, key=f'{ix}-{sens[0]}') for sens in info['sensors']]
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
#window = sg.Window('Edit Sensors', [[sg.Column(rows, scrollable=True)]])
window = sg.Window('Edit Sensors', rows)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "exit" or event == sg.WIN_CLOSED:
        print(values)
        break

window.close()

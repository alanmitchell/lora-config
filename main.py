#!/usr/bin/env python3
"""Main script to start LoRaWAN sensor configuration program.
"""

import sys
from pathlib import Path
import PySimpleGUI as sg

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

print(sensor_file)
print(bldgs)

win_init.close()

print(sensor_utils.read_sensor_file(sensor_file))

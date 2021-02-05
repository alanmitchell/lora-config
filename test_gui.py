# hello_psg.py

import PySimpleGUI as sg

rows = [  [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana'], 'Tetlin'), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog'], 'Temp'), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ELT-Lite: 123A'), sg.Combo(['Tetlin', 'Tanacross', 'Gulkana']), sg.Combo(['Temp', 'Pulse', 'Switch', 'Analog']), sg.Input('', (20,1)), sg.Checkbox('Temp', True), sg.Checkbox('Hum', True), sg.Checkbox('Ext', True), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ERS: 456F'), sg.Checkbox('Temp'), sg.Checkbox('Hum'), sg.Checkbox('Ext'), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Text('ERS-CO2: AB12'), sg.Checkbox('CO2'), sg.Checkbox('Temp'), sg.Checkbox('Hum'), sg.Checkbox('Light'), sg.Checkbox('Motion'), sg.Checkbox('Bat'), sg.Checkbox('Sig')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]



# Create the Window
window = sg.Window('Window Title', [[sg.Column(rows, scrollable=True)]])

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Ok" or event == sg.WIN_CLOSED:
        break

window.close()

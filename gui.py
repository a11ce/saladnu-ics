import PySimpleGUI as sg
import saladnu_ics as sics
import traceback 

def guiApp():
    sg.theme('DarkPurple6')
    layout = [[
        sg.Text('Select csv from salad.nu:'),
        sg.Input(key='-INCSV-'),
        sg.FileBrowse(target='-INCSV-')
    ], [sg.Button('Convert to ICS')]]

    window = sg.Window('Salad.nu to ICS', layout)

    while True:
        event, values = window.read()
        if event == 'Convert to ICS':
            try:
                csvLoc = values['-INCSV-']
                newCal = sics.csvToICS(csvLoc)
                icsPath = csvLoc[:-3] + "ics"
                sics.writeCal(newCal, icsPath)
                sg.popup('Saved to ' + icsPath)
                break
            except Exception as e:
                sg.popup("Error! Please report this if you selected a valid salad.nu CSV:\n\n" + traceback.format_exc())
                
        if event == sg.WIN_CLOSED:
            break
        print(event)
    window.close()
if __name__ == "__main__":
    guiApp()
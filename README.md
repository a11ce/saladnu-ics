# salad.nu to ICS

> Convert CSV schedules from salad.nu to ICS files.

## Usage
- Download and install python3 [here](https://www.python.org/downloads/) unless you know that you have it.
- Download SaladNU-ICS [here](https://github.com/a11ce/saladnu-ics/releases/download/v1.0/SaladNU-ICS.zip), open the zip, and run the app.
- Select your downloaded schedule.
- The ICS will be saved next to the CSV, ready to be opened in your calendar of choice.

## Setup

- Install GUI library with `pip3 install pysimplegui` if you want a GUI.
- Download with `git clone https://github.com/a11ce/saladnu-ics.git`

## Building
- Install [platypus](https://sveinbjorn.org/platypus) CLI with `brew install platypus`
- Run `make`

## CLI Usage

### GUI
- Run `python3 gui.py`
- Browse for your nu_schedule.csv.
- The ICS will be saved next to the CSV.

### Script
- Export your CSV schedule from salad.nu 
- Place nu_schedule.csv in this folder.
- Run `python3 saladnu_ics.py`
- Open nu_schedule.ics in your calendar of choice.
- Salad.nu uses CST, and ICS by default uses UTC, so the conversion should 'just work'.

--- 

All contributions are welcome by pull request or issue.

saladnu-ics is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.
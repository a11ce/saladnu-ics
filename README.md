# salad.nu to ICS

> Convert CSV schedules from salad.nu to ICS files.

## Setup

- Install ICS library with `pip3 install ics`
- Download with `git clone https://github.com/a11ce/saladnu-ics.git`

## Usage

- Export your CSV schedule from salad.nu 
- Place nu_schedule.csv in this folder.
- Run `python3 saladnu-ics.py`
- Open nu_schedule.ics in your calendar of choice.
- Salad.nu uses CST, and ICS by default uses UTC, so the conversion should 'just work'.

--- 

All contributions are welcome by pull request or issue.

saladnu-ics is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.
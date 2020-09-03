from datetime import datetime
from dateutil import tz
import ics

def main():

    newCal = csvToICS('nu_schedule.csv')
    writeCal(newCal, "nu_schedule.ics")
    
def csvToICS(path):
    myCal = ics.Calendar()
    with open(path) as f:
        next(f)
        for line in f:
            lineDat = [item[1:-1] for item in line.strip().split(',')]
            lineEvent = ics.Event()
            lineEvent.name = lineDat[0]

            lineEvent.begin = datetimeToUTC(convDate(lineDat[1]) + " " + lineDat[2])
            lineEvent.end   = datetimeToUTC(convDate(lineDat[3]) + " " + lineDat[4])
                
            myCal.events.add(lineEvent)
    return myCal

def writeCal(cal, path):
    with open(path,'w') as f:
        f.writelines(cal)
        
# MM-DD-YYYY to YYYY-MM-DD
def convDate(date):
    return date[-4:] + "-" + date[:-5]

def datetimeToUTC(dt):
    form = '%Y-%m-%d %H:%M'
    dtObj = datetime.strptime(dt, form).replace(tzinfo=tz.gettz('America/Chicago'))
    dtObj = dtObj.astimezone(tz.tzutc())
    return dtObj.strftime(form)
    
if __name__ == "__main__":
    main()
from datetime import datetime
from dateutil import tz
import uuid

def main():

    newCal = csvToICS('nu_schedule.csv')
    writeCal(newCal, "nu_scheduleTEST.ics")
    
def csvToICS(path):
    myCal = ['BEGIN:VCALENDAR','VERSION:2.0']
    with open(path) as f:
        next(f)
        for line in f:
            lineDat = [item[1:-1] for item in line.strip().split(',')]
                    
            myCal.append("BEGIN:VEVENT")
            myCal.append("DTEND:"+datetimeToUTC(convDate(lineDat[3]) + " " + lineDat[4]))
            myCal.append("DTSTART:" +datetimeToUTC(convDate(lineDat[1]) + " " + lineDat[2]))
            myCal.append("SUMMARY:" + lineDat[0])
            myCal.append("UID:" + makeUID())
            myCal.append("END:VEVENT")
    myCal.append("END:VCALENDAR")
    return myCal

def writeCal(cal, path):
    with open(path,'w') as f:
        f.write("\n".join(cal))
    
        
# MM-DD-YYYY to YYYY-MM-DD
def convDate(date):
    return date[-4:] + "-" + date[:-5]

def makeUID():
    uid = str(uuid.uuid4())
    return "{}@{}.org".format(uid, uid[:4]) 

def datetimeToUTC(dt):
    form = '%Y-%m-%d %H:%M'
    outForm ="%Y%m%dT%H%M%SZ"
    dtObj = datetime.strptime(dt, form).replace(tzinfo=tz.gettz('America/Chicago'))
    dtObj = dtObj.astimezone(tz.tzutc())
    return dtObj.strftime(outForm)
    
if __name__ == "__main__":
    main()
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from datetime import date
# Returns the current local date
todayDate=date.today()
todayMonth=str(todayDate)
todayMonth=todayMonth[5:7]
todayDay=str(todayDate)
todayDay=todayDay[8:]
file1 = open('C:/Users/agupta-22/Magic-Mirror/calendar1.txt', 'w')
def findCalendar(textFile) :
    g = open(textFile,'rb')
    gcal = Calendar.from_ical(g.read())
    for component in gcal.walk():
        if component.name == "VEVENT":
            startTime=component.get('DTSTART').to_ical()
            startTimeString = startTime.decode('utf-8')
            startTimeString1=startTimeString[4:6]
            startTimeString2=startTimeString[6:8]
            if startTimeString1 == todayMonth and startTimeString2 == todayDay:
                menu=component.get('summary')
                menu2=component.get('location') 

                
                if menu != None and menu2 != None:
                    file1.write(menu)
                    file1.write('\n')
                    
                    file1.write(menu2)
                    file1.write('\n')
                elif menu!= None:
                    file1.write(menu)
                    file1.write('\n')
                    file1.write('')
            else:
                menu=''
                file1.write(menu)
         
    g.close()
findCalendar('calendar1.ics')
file1.close()
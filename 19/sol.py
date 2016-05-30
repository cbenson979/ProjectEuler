import datetime
currentDay = datetime.datetime(1900,12,31)
sundayCount = 0
while True:
	currentDay += datetime.timedelta(1)
	if currentDay.isoweekday() == 7 and currentDay.day == 1: # Is it a sunday?
		sundayCount += 1
	if currentDay.year == 2000 and currentDay.month == 12 and currentDay.day == 31:
		break
print 'Number of sundays: '+str(sundayCount)
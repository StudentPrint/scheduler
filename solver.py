from Time import *
from Schedule import *
from Globals import *

def main() :
	return

def test() :
	print "passed: ScheduleTimeIterator" if test_scheduleTimeIterator() else "failed: ScheduleTimeIterator"
	print "passed: Schedule" if test_schedule() else "failed: Schedule"

def test_scheduleTimeIterator() :
	passed = True

	# test time and iterator
	test = ScheduleTimeIterator(OPEN_TIME)
	test.next()
	if str(test.time) != "9:30AM" :
		passed = False 

	test = ScheduleTimeIterator(Time(12, 45))
	test.next()
	if str(test.time) != "1:00PM" :
		passed = False 

	test = ScheduleTimeIterator(CLOSE_TIME)
	test.next()
	if str(test.time) != str(OPEN_TIME) :
		passed = False

	return passed

def test_schedule() :
	passed = True

	sch = Schedule()
	print sch.schedule[0][0].isEmpty()
	print sch.schedule[0][0]
	sch.schedule[0][0] = Shift(0, OPEN_TIME, CLOSE_TIME)
	print sch.schedule[0][0].isEmpty()
	print sch.schedule[0][0]
	try :
		sch.schedule[0][1] = Shift(0, OPEN_TIME, Time(23, 45))
	except ValueError as err :
		print(err)


	return passed

test()
main()
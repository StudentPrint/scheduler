from Time import Time

OPEN_TIME = Time(9, 15)
CLOSE_TIME = Time(17, 45)
SHIFT_INTERVAL_LENGTH = 15
NUM_SHIFT_INTERVALS = 34

# time: Time
class ScheduleTimeIterator :
	def __init__(self, time) :
		self.time = Time(time.hours, time.minutes)

	# increments time by shift interval length
	def next(self) :
		self.time.next(SHIFT_INTERVAL_LENGTH)
		if(self.time.compare(CLOSE_TIME)) :
			self.time.set(OPEN_TIME.hours, OPEN_TIME.minutes)

def main() :
	test()
	return

def test() :
	passed = True
	
	# test time and iterator
	test = ScheduleTimeIterator(OPEN_TIME)
	test.next()
	if test.time.toString() != "9:30AM" :
		passed = False 

	test = ScheduleTimeIterator(Time(12, 45))
	test.next()
	if test.time.toString() != "1:00PM" :
		passed = False 

	test = ScheduleTimeIterator(CLOSE_TIME)
	test.next()
	if test.time.toString() != OPEN_TIME.toString() :
		passed = False 

	print "passed: ScheduleTimeIterator" if passed else "failed: ScheduleTimeIterator"

main()
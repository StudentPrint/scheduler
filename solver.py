from Time import Time

OPEN_TIME = Time(9, 15, True)
CLOSE_TIME = Time(5, 45, True)
SHIFT_INTERVAL_LENGTH = 15
NUM_SHIFT_INTERVALS = 34

# time: Time
class ScheduleTimeIterator :
	def __init__(self, time) :
		self.time = time

	# increments time by shift interval length
	def next(self) :
		self.time.next(SHIFT_INTERVAL_LENGTH)
		if(self.time.compare(CLOSE_TIME)) :
			self.time.set(OPEN_TIME.hours, OPEN_TIME.minutes, OPEN_TIME.isAM)

def main() :
	test = ScheduleTimeIterator(OPEN_TIME)
	test.next()
	print test.time.toString()
	return

main()
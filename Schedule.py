from Time import *
from Globals import *

# Iterator over times from a starting time (time) until
# the closing time, at which the iterator cycles to open time
#
# time: Time
class ScheduleTimeIterator :
	def __init__(self, time) :
		self.time = Time(time.hours, time.minutes)

	# increments time by shift interval length
	def next(self) :
		self.time.next(SHIFT_INTERVAL_LENGTH)
		if(self.time.compare(CLOSE_TIME)) :
			self.time.set(OPEN_TIME.hours, OPEN_TIME.minutes)

# Schedule data structure
class Schedule :
	def __init__(self) :
		# creates an array of tuples representing shifts for a given day
		self.schedule = [[Shift(0, 0, 0) for i in DAYS_OPEN_IN_WEEK] for i in range(NUM_EMPLOYEES)]

# Shift data structure
class Shift :
	def __init__(self, day, start_time, end_time) :
		if(isinstance(start_time, int) or isinstance(end_time, int)) :
			self.shift = (day, 0, 0)
			return

#		if(day < 0 or day >= len(DAYS_OPEN_IN_WEEK)) :
#			raise ValueError("shift day must be between 0 and " + str(len(DAYS_OPEN_IN_WEEK)-1))
#		if(OPEN_TIME.compare(start_time) or end_time.compare(CLOSE_TIME)) :
#			raise ValueError("shift must be between " + str(OPEN_TIME) + " and " + str(CLOSE_TIME))

		self.shift = (day, start_time, end_time)

	def modify(self, day, start_time, end_time) :
		self.shift = (day, start_time, end_time)

	def isEmpty(self) :
		return isinstance(self.shift[1], int) or isinstance(self.shift[2], int)

	def __str__(self) :
		if self.isEmpty() :
			return "Empty Shift"
		else :
			return str(DAYS_OPEN_IN_WEEK[self.shift[0]]) + ": " + str(self.shift[1]) + " - " + str(self.shift[2])


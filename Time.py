# hours: int
# minutes: int
# isAM: bool
class Time :
	def __init__(self, hours, minutes) :
		self.set(hours, minutes)

	# increments time by increment
	def next(self, increment) :
		self.minutes += increment
		if(self.minutes >= 60) :
			self.hours += 1
			self.minutes -= 60
		if(self.hours > 24) :
			self.hours -= 24

	# resets time to given value
	def set(self, hours, minutes) :
		self.hours = hours
		self.minutes = minutes

	# returns true if self is later than time, false o.w.
	def compare(self, time) :
		if(self.hours != time.hours) :
			return self.hours > time.hours
		else :
			return self.minutes > time.minutes

	# returns true if self equals time, false o.w.
	def equals(self, time) :
		return self.hours == time.hours and self.minutes == time.minutes

	def __str__(self) :
		if(self.hours > 12) :
			return str(self.hours-12) + ':' + str(self.minutes).zfill(2) + ('AM' if self.hours == 24 else 'PM')
		else :
			return str(self.hours) + ':' + str(self.minutes).zfill(2) + ('PM' if self.hours == 12 else 'AM')

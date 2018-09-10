# hours: int
# minutes: int
# isAM: bool
class Time :
	def __init__(self, hours, minutes, isAM) :
		self.set(hours, minutes, isAM)

	# increments time by increment
	def next(self, increment) :
		self.minutes += increment
		if(self.minutes >= 60) :
			self.hours += 1
			self.minutes -= 60
		if(self.hours >= 13) :
			self.hours -= 12
			self.am = not self.am

	# resets time to given value
	def set(self, hours, minutes, isAM) :
		self.hours = hours
		self.minutes = minutes
		self.isAM = isAM

	# returns true if self is later than time, false o.w.
	def compare(self, time) :
		if(self.isAM != time.isAM) :
			return time.isAM
		elif(self.hours != time.hours) :
			return self.hours > time.hours
		else :
			return self.minutes > time.minutes

	# returns true if self equals time, false o.w.
	def equals(self, time) :
		return self.hours == time.hours and self.minutes == time.minutes and self.isAM == time.isAM

	def toString(self) :
		return str(self.hours) + ':' + str(self.minutes).zfill(2) + ('AM' if self.isAM else 'PM')

SHIFT_INTERVAL_LENGTH = 15
OPENING_TIME = 915
CLOSING_TIME = 1745
NUM_SHIFT_INTERVALS = ((CLOSING_TIME - OPENING_TIME)%100) * (60/SHIFT_INTERVAL_LENGTH) + ((CLOSING_TIME - OPENING_TIME)/100 / SHIFT_INTERVAL_LENGTH)

class schedule :
	def __init__(self, numEmployees) :
		self.employeeClassTimes = employeeClassTimes
		self.schedule = [[0 for y in range(60/SHIFT_INTERVAL_LENGTH)] for x in range(rows_count)]

def main() :
	print NUM_SHIFT_INTERVALS
	return

main()
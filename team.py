import sys

class TeamStats:

	def __init__(self, name: str, player_ids:set):
		self.name = name
		self.player_ids = player_ids
		self.total_points = 0
		self.curr_week = None

	def add_week(self):
		self.curr_week = WeekStat()

	def add_points(self, points, player_name: str):
		self.curr_week.add(points, player_name.decode("utf-8"))
		self.total_points += points

	def print_week_high(self):
		print(f'Team {self.name}: {self.curr_week.high_player_name} ({self.curr_week.high_points})')

	def print_week_low(self):
		print(f'Team {self.name}: {self.curr_week.low_player_name} ({self.curr_week.low_points})')

	def print_week_total(self):
		print(f'Team {self.name}: {round(self.curr_week.total_points,2)}')

	def print_season_total(self):
		print(f'Team {self.name}: {round(self.total_points,2)}')


class WeekStat:

	def __init__(self):
		self.total_points = 0
		self.high_points = -1
		self.high_player_name = "NA"

		self.low_points = sys.maxsize
		self.low_player_name = "NA"

	def add(self, points, player_name: str):
		self.total_points += points

		if self.high_points < points:
			self.high_points = points
			self.high_player_name = player_name

		if self.low_points > points:
			self.low_points = points
			self.low_player_name = player_name
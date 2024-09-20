class TeamStats:

	def __init__(self, name: str, player_ids:set):
		self.name = name
		self.player_ids = player_ids

		self.weekly_stats = []
		self.total_points = 0

	def add_week(self):
		self.weekly_stats.append(WeekStat())

	def add_points(self, points, player_name: str):
		self.weekly_stats[-1].add(points, player_name.decode("utf-8"))
		self.total_points += points

	def get_current_week(self):
		return self.weekly_stats[-1]

class WeekStat:

	def __init__(self):
		self.total_points = 0
		self.high_points = -1
		self.high_player_name = "NA"

	def add(self, points, player_name: str):
		self.total_points += points

		if self.high_points < points:
			self.high_points = points
			self.high_player_name = player_name

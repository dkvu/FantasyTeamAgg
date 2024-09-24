import yaml

from pathlib import Path
from yfpy.query import YahooFantasySportsQuery
from team import TeamStats

def main():
	config = yaml.safe_load(open('./config.yml'))

	team_a = TeamStats(config['team_a_name'], set(config['team_a_ids']))
	team_b = TeamStats(config['team_b_name'], set(config['team_b_ids']))

	def run_on_teams(func):
		func(team_a)
		func(team_b)

	query = YahooFantasySportsQuery(Path("."), league_id=config['leauge_id'])
	
	current_week = get_current_week(query) - 1
	print( f'Current Week: {current_week}')

	for week in range(1,current_week+1):
		print(f'Gathering stats for week: {week}')

		run_on_teams(TeamStats.add_week)

		scoreboard = query.get_league_scoreboard_by_week(week)
		for matchup in scoreboard.matchups:
			for teamItem in matchup['matchup'].teams:
				team = teamItem['team']

				if team.team_id in team_a.player_ids:
					team_a.add_points(team.team_points.total, team.name)
				elif team.team_id in team_b.player_ids:
					team_b.add_points(team.team_points.total, team.name)
				else:
					raise Exception(f'Team Id ({team.team_id}) not part of any team.')

	print()
	print("###### SUMMARY ######")
	print(f'Week {current_week} Top Scorer:')
	run_on_teams(TeamStats.print_week_high)

	print()
	print(f'Week {current_week} Bottom Scorer:')
	run_on_teams(TeamStats.print_week_low)

	print()
	print(f'Week {current_week} Team Total:')
	run_on_teams(TeamStats.print_week_total)

	print()
	print(f'Season Team Total:')
	run_on_teams(TeamStats.print_season_total)

def get_current_week(query):
	league = query.get_league_info()
	return league.current_week

if __name__ == "__main__":
	main()
from pathlib import Path
from yfpy.query import YahooFantasySportsQuery
from team import TeamStats

def main():
	league_id = '730330'

	team_a_ids = {
		4, #khang
		6, #bhoang
		8, #tin
		9, #viv
		11, #lieu
		12, #dalz
	}
	team_a = TeamStats("Vivian", team_a_ids)

	team_b_ids = {
		1, #wu
		2, #hansel
		3, #cao
		5, #dimitry
		7, #josh
		10, #nam
	}
	team_b = TeamStats("Josh", team_b_ids)


	query = YahooFantasySportsQuery(Path("."), league_id=league_id)
	
	current_week = get_current_week(query) - 1
	print( f'Current Week: {current_week}')

	for week in range(1,current_week+1):
		print(f'Gathering stats for week: {week}')

		team_a.add_week()
		team_b.add_week()

		scoreboard = query.get_league_scoreboard_by_week(week)
		for matchup in scoreboard.matchups:
			for teamItem in matchup['matchup'].teams:
				team = teamItem['team']

				if team.team_id in team_a.player_ids:
					team_a.add_points(team.team_points.total, team.name)
				elif team.team_id in team_b.player_ids:
					team_b.add_points(team.team_points.total, team.name)
				else:
					raise Exception(f'Team Id ({team.id}) not part of any team.')

	curr_a = team_a.get_current_week()
	curr_b = team_b.get_current_week()

	print()
	print("###### SUMMARY ######")
	print(f'Week {current_week} Top Scorer:')
	print(f'Team {team_a.name}: {curr_a.high_player_name} ({curr_a.high_points})')
	print(f'Team {team_b.name}: {curr_b.high_player_name} ({curr_b.high_points})')

	print()
	print(f'Week {current_week} Team Total:')
	print(f'Team {team_a.name}: {round(curr_a.total_points,2)}')
	print(f'Team {team_b.name}: {round(curr_b.total_points,2)}')

	print()
	print(f'Season Team Total:')
	print(f'Team {team_a.name}: {round(team_a.total_points,2)}')
	print(f'Team {team_b.name}: {round(team_b.total_points,2)}')

def get_current_week(query):
	league = query.get_league_info()
	return league.current_week

if __name__ == "__main__":
	main()
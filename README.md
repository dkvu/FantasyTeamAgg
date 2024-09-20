# FantasyTeamAgg

## Setup
1. install python (locally running 3.7.2)
2. follow Installation, Setup, and Authentication from https://github.com/uberfastman/yfpy
	* for Setup: stop at "Note: If you are only planning on using YFPY to pull "read only" data from public leagues, you do not need to do this."

## Config
in fantasyTeamAgg.py you need to set
* league_id:
	* on browser, sign into yahoo sports and navigate to your league
	* in the url you should see f1/followed by an int (your league id)
	* ex. football.fantasysports.yahoo.com/f1/730330, league id = 730330
* player_id:
	* tedious but use your league url and append 1-12
	* ex: football.fantasysports.yahoo.com/f1/730330/1, will tell you who player_id=1 is

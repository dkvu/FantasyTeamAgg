# FantasyTeamAgg

## Setup
(Wrapper / ref https://github.com/uberfastman/yfpy)
1. install python (locally running 3.7.2)
	* does not run on 3.11
2. pip install yfpy
3. pip instal yaml
4. https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html
	* Just the I. Setting Up: Create an Application ... (If I'm remembering right)
	* Yahoo's (OWN!!!) docs are out-dated, refer to https://github.com/uberfastman/yfpy?tab=readme-ov-file#setup for guidance
5. https://github.com/uberfastman/yfpy?tab=readme-ov-file
   	* Usage -> Authentication (this part will trigger the first time you run the app, see usage below)
   	* keep private.json and token.json in same directory as fantasyTeamAgg.py

TODO: one more pip install and then don't be lazy and add Requirements.txt...

## Config
create a config.yml using config.template.yml as reference
* league_id:
	* on browser, sign into yahoo sports and navigate to your league
	* in the url you should see f1/followed by an int (your league id)
	* ex. football.fantasysports.yahoo.com/f1/730330, league id = 730330
	* or on the phone app under league settings
* player_id:
	* tedious but use your league url and append 1-12
	* ex: football.fantasysports.yahoo.com/f1/730330/1, will tell you who player_id=1 is

# Usage
* to run: python fantasyTeamAgg.py
* Tuesday(ish) marks a new week so if you run the script on tuesday 'current_week = get_current_week(query) - 1' is correct
* if you run it monday night, it should read 'current_week = get_current_week(query)'

TODO: maybe infer '-1' by the day of the week or take it in as an arg

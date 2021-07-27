import os

"""This method gets the league log from the teams that played matches"""
def get_league_log(sample_data):

    league_log = {}
    with open(sample_data, encoding='utf-8') as matches:
        for match in matches:
            match_teams = str(match).strip("\n").split(",")
            home_team = str(match_teams[0])[0:-2].strip()
            away_team = str(match_teams[1])[0:-2].strip()
            initials_points = 0
            if home_team not in league_log:
                league_log[home_team] = initials_points
            if away_team not in league_log:
                league_log[away_team] = initials_points

    return league_log

"""This method initializes the league table and calculates teams points and finnally print out the updated league table"""
def init(input_file):

    league_log = get_league_log(input_file)
    with open(input_file, encoding='utf8') as matchResults:
        for result in matchResults:
            score = str(result).strip("\n").split(",")
            home_team = str(score[0])[0:-2].strip()
            home_team_goals = str(score[0])[-1]
            away_team = str(score[1])[0:-2].strip()
            away_team_goals = str(score[1])[-1]
            if home_team_goals == away_team_goals:
                league_log[home_team] = league_log[home_team] + 1
                league_log[away_team] = league_log[away_team] + 1

            elif home_team_goals > away_team_goals:
                league_log[home_team] = league_log[home_team] + 3

            elif home_team_goals < away_team_goals:
                league_log[away_team] = league_log[away_team] + 3

    league_team_name_sort_list = sorted(league_log.items())
    league_team_name_sort_dict = {team: points for team, points in league_team_name_sort_list}
    league_team_points_sort_list = sorted(
        league_team_name_sort_dict.items(),
        key=lambda x: x[1],
        reverse=True)
    league_table = {team: points for team, points in league_team_points_sort_list}

    count = 0
    for team in league_table:
        count += 1
        print(f'{count}. {team}, {league_table[team]} pts')

"""This method prompts for sample data text file, to be used in producing the league table"""
def get_input_data():

    data_file_name = input("Enter your sample data text file with it's .txt extension: ")
    try:
        if os.path.exists(data_file_name):
            init(data_file_name)
        else:
            print("FILE NOT FOUND! Please ensure you provided the correct and existing "
                  "file name with its extension(.txt).")
            get_input_data()
    except os.error:
        print("FILE NOT FOUND! Please ensure you provided the correct and existing "
              "file name with its extension(.txt).")
        get_input_data()


if __name__ == '__main__':
    get_input_data()

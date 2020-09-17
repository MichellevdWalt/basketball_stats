import constants
import copy

# if __name__ == "__main__":

teams_c = copy.deepcopy(constants.TEAMS)
players_c = copy.deepcopy(constants.PLAYERS)

def clean_data():
    for player in players_c:
        height_int = int(player["height"][0:2])
        player["height"] = height_int
        if player["experience"] == "YES":
            player["experience"] = True
        elif player["experience"] == "NO":
            player["experience"] = False
        guardian = player["guardians"].split("and")
        player["guardians"] = guardian
clean_data()


def balance_teams():
    exp_players = []
    inexp_players = []
    for player in players_c:
        if player["experience"]:
            exp_players.append(player)
        elif player["experience"] == False:
            inexp_players.append(player)
    exp_players_per_team = int(len(exp_players)/len(teams_c))
    inexp_players_per_team = int(len(inexp_players)/len(teams_c))
    exp_start = 0
    inexp_start = 0
    teams = [{}]
    for team in teams_c:
        exp_end = exp_start + exp_players_per_team
        inexp_end = inexp_start + inexp_players_per_team
        teams[0][team] = exp_players[exp_start:exp_end] + inexp_players[inexp_start:inexp_end]
        exp_start += exp_players_per_team 
        inexp_start += inexp_players_per_team
    return teams
    

teams = balance_teams()

while True:
    print("\nBASKETBALL TEAM STATS TOOL")
    print ("\n---Menu---\n")
    print("Here are your choices: \n1.) Display team stats. \n2.) Quit")
    option = input("Enter an option   ")

    if option == "1":
        print("\nPlease choose from these teams:")
        for index, team in enumerate(teams[0], 1):
            print(f'{index}.) {team}')
        print(f'{len(teams_c) + 1}.) Quit')
    elif option == "2":
        break
    else:
        print("\nPlease enter a valid option")
        continue
    

    def exp(team):
        exp_player = []
        for player in teams[0][team]:
            if player["experience"]:
                exp_player.append(player)
        return exp_player

        
    def inexp(team):
        inexp_player = []
        for player in teams[0][team]:
            if player["experience"] == False:
                inexp_player.append(player)
        return inexp_player


    def average_height(team):
        total_height = 0
        for player in teams[0][team]:
            total_height += player["height"]
        average_height = total_height/len(teams[0][team])
        return average_height


    def print_team(option):
        team_chosen = teams_c[int(option)-1]
        team_sentence = f'\nTeam: {team_chosen} Stats'
        exp_players = exp(team_chosen)
        inexp_players = inexp(team_chosen)
        avg_height = average_height(team_chosen)
        print(team_sentence)
        print("-"*len(team_sentence))
        print(f"Total Players: {len(teams[0][team_chosen])}")
        print(f"Experienced Players: {len(exp_players)} ")
        print(f"Inexperienced Players: {len(inexp_players)}")
        print(f"Average Height of Players: {avg_height}inches")
        print("\nPlayers on team:")
        players = []
        for player in teams[0][team_chosen]:
            players.append(player["name"])
        players_sentence = ', '.join(players)
        print(f'  {players_sentence}')
        guardians = []
        for player in teams[0][team_chosen]:
            guardians += (player["guardians"])
        print(f"\nTeam Guardians: \n  {', '.join(guardians)}")

    while True:
        option = input("Please enter an option   ")
        if option == "1" or option == "2" or option == "3":
            print_team(option)
            break
        elif option == "4":
            break
        else:
            print("\nPlease enter a valid numerical option  ")
            continue
    

    while True:
        would_continue = input("\nWould you like to Continue? y or n  ")
        if would_continue.upper() == "Y":
            restart = True
            break
        elif would_continue.upper() == "N":
            restart = False
            break
        else:
            print("\nPlease enter a y for yes or a n for no. ")
            continue
    
    if restart:
        continue
    elif restart == False:
        print("\nThanks for using our Basketball Stats Tool. Goodbye")
        break



enemies = {}
enemies['david'] = ['lucy', 'jose', 'chris']
enemies['lucy'] = ['david', 'brian', 'emily']
enemies['emily'] = ['lucy', 'jack']
enemies['jose'] = ['david', 'paul']
enemies['paul'] = ['jose', 'chris']
enemies['chris'] = ['paul', 'david', 'brian']
enemies['brian'] = ['lucy', 'chris', 'jack']
enemies['jack'] = ['brian', 'emily']


team1 = set()
team2 = set()

def find_teams():
    for kid, enemy_list in enemies.items():
        if kid in team1:
            for enemy in enemy_list:
                team2.add(enemy)
        elif kid in team2:
            for enemy in enemy_list:
                team1.add(enemy)
        else:
            enemy_team = None
            for enemy in enemy_list:
                if enemy in team1:
                    if enemy_team == team2:
                        return False
                    else:
                        enemy_team = team1
                if enemy in team2:
                    if enemy_team == team1:
                        return False
                    else:
                        enemy_team = team2
            if enemy_team == team1:
                team2.add(kid)
            else:
                team1.add(kid)
    return team1, team2

print(find_teams())


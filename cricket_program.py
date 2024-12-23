import random

def toss():

    return random.choice(['Heads','Tails'])

def ball_outcome():
    """Simulate the outcome of a single ball"""
    outcomes = [1,2,3,4,6, 'wide', 'no ball',  'out']
    return random.choice(outcomes)

def play_over(players):
    ''''Simulate one over of cricket (6 balls) for a team with multiple players'''
    runs = 0
    balls = 0
    extra_ball = false
    players_out_index = -1
    players_outs = 0

    while balls < 6 and player_outs <  len(players):
        outcomes = ball_outcome()
        if outcome == 'wide' or outcome == 'no ball':
            runs += 1
            extra_ball = True
            print(f"ball {balls + 1}: {outcome} (Extra ball, runs: {runs})")
            continue
        elif outcome == 'out':
            if extra_ball:
                print(f'ball {balls + 1}: {outcome} (Player not out due to no ball)")
                extra_ball = false
            else:
                player_outs += 1
                print(f"Ball {balls +1}: {outcome}  (player {player[player_out_index]}))
                if players_out_index >= len(players):
                      break
                       

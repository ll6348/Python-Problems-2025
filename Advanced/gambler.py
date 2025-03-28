import random

def gambler(stake,goal,number_of_times):
    '''This function Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal. 
    Keeps track of the number of times he/she wins and the number of bets he/she makes.
    Run the experiment N times, averages the results, and prints them out.'''
    bet_losses = 0
    bet_wins = 0
    bets = 0
    game_wins = 0
    game_losses = 0
    for _ in range(1, number_of_times+1):
        current_stake = stake
        while 0 < current_stake < goal:
            win_or_lose = random.choice([0,1])
            if win_or_lose == 1:
                current_stake += 1
                bets += 1
                bet_wins += 1
            else:
                current_stake -= 1
                bets += 1
                bet_losses += 1
        print(f"Number of Wins in game {_} = {bet_wins}")
        print(f"Win Percentage of game {_} = {bet_wins/bets}")
        print(f"Loss Percentage of game {_} = {bet_losses/bets}")
        

        if current_stake == goal:
            game_wins += 1
        if current_stake == 0:
            game_losses += 1
    print(f"Number of Game Wins = {game_wins}")
    print(f"Percentage of wins = {game_wins/number_of_times}")
    print(f"Percentage of losses = {game_losses/number_of_times}")

stake = int(input("Enter the stake:"))
goal = int(input("Enter the goal:"))
number_of_times = int(input("Enter the number of times:"))
gambler(stake, goal, number_of_times)



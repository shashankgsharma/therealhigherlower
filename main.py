from time import sleep
from random import choice
from game_data import male_data, female_data
from art import logo, vs
from os import system
import datetime


def read_file(file_name):
    with open(file_name) as file:
        winner = file.readline()
        winner = winner.split(', ')
        winner_name = winner[0]
        winner_score = winner[1]
        date = winner[2]
        return winner_name, winner_score, date


def write_file(file_name, winner_name, winner_score, date):
    with open(file_name, 'w') as file:
        file.write(f"{winner_name}, {winner_score}, {date}")


def greetme(player_name):
    return f"Hi {player_name}, Welcome to the Higher-Lower Cricket Game.\n"


def random_player_selector(data):
    return choice(data)


def print_player(player, gender):
    return f"{player['name']}, a {player['age']} years old {gender}s cricketer from {player['country']}, having taken {player['international_wickets']} international wickets.\n"


def compare(a, b):
    if a > b:
        return "l"
    elif a < b:
        return "h"
    else:
        return "equal"


def play():
    print(logo)
    player_name = input("Player name: ")
    system('clear')
    print(logo)
    print(greetme(player_name))
    ans1 = input(
        "Type 'm' to play Men's Cricket Trivia, 'w' to play Women's Cricket Trivia: "
    ).lower()

    if ans1 == 'w':
        data = female_data
        gender = 'Women'
    else:
        data = male_data
        gender = 'Men'

    player1 = random_player_selector(data)
    player2 = random_player_selector(data)
    while player1 == player2:
        player2 = random_player_selector(data)

    game_end = False
    score = 0

    while not game_end:
        system('clear')
        print(logo + "\n")
        winner_name, winner_score, date = read_file('winner.txt')
        print(f"Highest score: {winner_name}: {winner_score} on {date}.")
        print(f"Your current score: {score}.\n")
        print(print_player(player1, gender))
        print(vs)
        print(print_player(player2, gender))

        result = compare(player1['international_runs'],
                         player2['international_runs'])
        user_guess = input(
            f"Type 'h' if you think {player2['name']}'s international runs is higher than {player1['name']}'s international runs, \nType 'l' if you think it's lower: \n"
        ).lower()

        print(
            f"\nInternational runs:\n{player1['name']}: {player1['international_runs']} runs.\n{player2['name']}: {player2['international_runs']} runs.\n"
        )
        sleep(3)
        if user_guess == result:
            score += 1
            player1 = player2
            player2 = random_player_selector(data)
            if player1 == player2:
                player2 = random_player_selector(data)

        else:
            game_end = True
    print(f"\nGame ended, final_score: {score}.\n")
    if score > int(winner_score):
        winner_name = player_name
        winner_score = score
        now = datetime.datetime.now()
        date = now.date()
        # time = now.strftime("%H:%M:%S")
        write_file('winner.txt', winner_name, winner_score, date)
        print("Congratulations! This is a new high score!")


while (input(
        "Wanna play a game of higher-lower? (Type 'y' to play, 'n' to end): ").
       lower() == 'y'):
    system('clear')
    play()

system('clear')
print('GoodBye!')

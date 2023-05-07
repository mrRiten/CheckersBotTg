import time
from config import *
import telebot as tl
from game import *
from threading import Thread

# bot token
bot = tl.TeleBot(Token)


# Player`s information
player_ready = []
player_in_game = []
server = []


# Start message
@bot.message_handler(commands=['start'])
def start_mes(message):
    bot.send_message(message.chat.id, 'hi!')
    while True:
        print(f'ready {player_ready}')
        print(f'play {player_in_game}')
        print(f'{server}')
        time.sleep(3)


@bot.message_handler(commands=['find'])
def start_game(message):
    global player_ready
    global player_in_game
    bot.send_message(message.chat.id, 'Начался поиск соперника')
    player_ready.append(message.chat.id)
    if len(player_ready) == 2:
        player_in_game.append([player_ready[0], player_ready[1]])
        game_start(player_ready)
        player_ready = []


def game_start(players):
    bot.send_message(players[0], 'Соперник найден!')
    bot.send_message(players[1], 'Соперник найден!')
    run_server(players[0], players[1])


def run_server(pl1, pl2):
    server.append(GamePlay('session', pl1, pl2))


# Run bot with infinite mode
try:
    bot.infinity_polling()
    # run all threads in loop
    for n in range(5):
        thr = Thread(target=run_server, args=(n,))
        thr.start()

except Exception as _ex:
    print(_ex)

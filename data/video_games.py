from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

computer_games = Problem("Play real-time computer & video games", ["world-modelling", "realtime-games", "agi", "language"])

games_requiring_novel_language = Problem("Games that require inventing novel language, forms of speech, or communication")
games_requiring_speech = Problem("Games that require both understanding and speaking a language")
games_requiring_speech.metric("Starcraft")

games_requiring_language_comprehension = Problem("Games that require language comprehension", ["agi", "languge"])

computer_games.add_subproblem(games_requiring_novel_language)
games_requiring_novel_language.add_subproblem(games_requiring_speech)
games_requiring_speech.add_subproblem(games_requiring_language_comprehension)


# Atari 2600 Games: Breakout, Enduro, Pong, Q*Bert, Seaquest, S. Invaders. Each game has its own metric.
# We previously used hand-compiled by Yomna Nasser and Miles Brundage; this is
# now mostly obsolete, and the data is scraped in scrapers/atari.py

simple_games = Problem("Simple video games", ["world-modelling", "realtime-games", "agi"]) 
computer_games.add_subproblem(simple_games)

# Alien
alien_metric = simple_games.metric("Atari 2600 Alien", scale=atari_linear, target=6875, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# alien_metric.measure(date(2015, 2, 26), 3069, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# alien_metric.measure(date(2015,11,20), 1620, "DQN","https://arxiv.org/abs/1511.06581v1")
# alien_metric.measure(date(2015,11,20), 3747.7, "DDQN","https://arxiv.org/abs/1511.06581v1")
# alien_metric.measure(date(2015,11,20), 4461.4, "Duel","https://arxiv.org/abs/1511.06581v1")

# Amidar
amidar_metric = simple_games.metric("Atari 2600 Amidar", scale=atari_linear, target=1676, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# amidar_metric.measure(date(2015, 2, 26), 739.5, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# amidar_metric.measure(date(2015,11,20), 978, "DQN","https://arxiv.org/abs/1511.06581v1")
# amidar_metric.measure(date(2015,11,20), 1793.3, "DDQN","https://arxiv.org/abs/1511.06581v1")
# amidar_metric.measure(date(2015,11,20), 2354.5, "Duel","https://arxiv.org/abs/1511.06581v1")

# Assault
assault_metric = simple_games.metric("Atari 2600 Assault", scale=atari_linear, target=1496, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# assault_metric.measure(date(2015, 2, 26), 3359, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# assault_metric.measure(date(2015,11,20), 4280.4, "DQN","https://arxiv.org/abs/1511.06581v1")
# assault_metric.measure(date(2015,11,20), 5393.2, "DDQN","https://arxiv.org/abs/1511.06581v1")
# assault_metric.measure(date(2015,11,20), 4621.0, "Duel","https://arxiv.org/abs/1511.06581v1")

# Asterix
asterix_metric = simple_games.metric("Atari 2600 Asterix", scale=atari_linear, target=8503, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# asterix_metric.measure(date(2015, 2, 26), 6012, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# asterix_metric.measure(date(2015,11,20), 4359, "DQN","https://arxiv.org/abs/1511.06581v1")
# asterix_metric.measure(date(2015,11,20), 17356, "DDQN","https://arxiv.org/abs/1511.06581v1")
# asterix_metric.measure(date(2015,11,20), 28188, "Duel","https://arxiv.org/abs/1511.06581v1")

# Asteroids
asteroids_metric = simple_games.metric("Atari 2600 Asteroids", scale=atari_linear, target=13157, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# asteroids_metric.measure(date(2015, 2, 26), 1629, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# asteroids_metric.measure(date(2015,11,20), 1364.5, "DQN","https://arxiv.org/abs/1511.06581v1")
# asteroids_metric.measure(date(2015,11,20), 734.7, "DDQN","https://arxiv.org/abs/1511.06581v1")
# asteroids_metric.measure(date(2015,11,20), 2837.7, "Duel","https://arxiv.org/abs/1511.06581v1")

# Atlantis
atlantis_metric = simple_games.metric("Atari 2600 Atlantis", scale=atari_linear, target=29028, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# atlantis_metric.measure(date(2015, 2, 26), 85641, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# atlantis_metric.measure(date(2015,11,20), 279987, "DQN","https://arxiv.org/abs/1511.06581v1")
# atlantis_metric.measure(date(2015,11,20), 106056, "DDQN","https://arxiv.org/abs/1511.06581v1")
# atlantis_metric.measure(date(2015,11,20), 382572, "Duel","https://arxiv.org/abs/1511.06581v1")

# Bank Heist
bank_heist_metric = simple_games.metric("Atari 2600 Bank Heist", scale=atari_linear, target=734.4, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# bank_heist_metric.measure(date(2015, 2, 26), 429.7, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# bank_heist_metric.measure(date(2015,11,20), 455, "DQN","https://arxiv.org/abs/1511.06581v1")
# bank_heist_metric.measure(date(2015,11,20), 1030.6, "DDQN","https://arxiv.org/abs/1511.06581v1")
# bank_heist_metric.measure(date(2015,11,20), 1611.9, "Duel","https://arxiv.org/abs/1511.06581v1")

# Battle Zone
battle_zone_metric = simple_games.metric("Atari 2600 Battle Zone", scale=atari_linear, target=37800, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# battle_zone_metric.measure(date(2015, 2, 26), 26300, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# battle_zone_metric.measure(date(2015,11,20), 29900, "DQN","https://arxiv.org/abs/1511.06581v1")
# battle_zone_metric.measure(date(2015,11,20), 31700, "DDQN","https://arxiv.org/abs/1511.06581v1")
# battle_zone_metric.measure(date(2015,11,20), 37150, "Duel","https://arxiv.org/abs/1511.06581v1")

# Beam Rider
beam_rider_metric = simple_games.metric("Atari 2600 Beam Rider", scale=atari_linear, target=7456, target_source="https://arxiv.org/pdf/1312.5602.pdf", atari=True)
# beam_rider_metric.measure(date(2013,12,19), 4092, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# beam_rider_metric.measure(date(2015,11,20), 8627, "DQN","https://arxiv.org/abs/1511.06581v1")
# beam_rider_metric.measure(date(2015,11,20), 13772, "DDQN","https://arxiv.org/abs/1511.06581v1")
# beam_rider_metric.measure(date(2015,11,20), 12164, "Duel","https://arxiv.org/abs/1511.06581v1")

# Berzerk 
berzerk_metric = simple_games.metric("Atari 2600 Berzerk", scale=atari_linear, target=2630.4, target_source="https://arxiv.org/abs/1511.06581v1", atari=True)
# berzerk_metric.measure(date(2015,11,20), 585, "DQN","https://arxiv.org/abs/1511.06581v1")
# berzerk_metric.measure(date(2015,11,20), 1225, "DDQN","https://arxiv.org/abs/1511.06581v1")
# berzerk_metric.measure(date(2015,11,20), 1472, "Duel","https://arxiv.org/abs/1511.06581v1")

# Bowling
bowling_metric = simple_games.metric("Atari 2600 Bowling", scale=atari_linear, target=154.8, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# bowling_metric.measure(date(2015, 2, 26), 42.8, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# bowling_metric.measure(date(2015,11,20), 50.4, "DQN","https://arxiv.org/abs/1511.06581v1")
# bowling_metric.measure(date(2015,11,20), 68.1, "DDQN","https://arxiv.org/abs/1511.06581v1")
# bowling_metric.measure(date(2015,11,20), 65.5, "Duel","https://arxiv.org/abs/1511.06581v1")

# Boxing
boxing_metric = simple_games.metric("Atari 2600 Boxing", scale=atari_linear, target=4.3, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# boxing_metric.measure(date(2015, 2, 26), 71.8, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# boxing_metric.measure(date(2015,11,20), 88, "DQN","https://arxiv.org/abs/1511.06581v1")
# boxing_metric.measure(date(2015,11,20), 91.6, "DDQN","https://arxiv.org/abs/1511.06581v1")
# boxing_metric.measure(date(2015,11,20), 99.4, "Duel","https://arxiv.org/abs/1511.06581v1")

# Breakout
breakout_metric = simple_games.metric("Atari 2600 Breakout", scale=atari_linear, target=31.8, target_source="https://pdfs.semanticscholar.org/340f/48901f72278f6bf78a04ee5b01df208cc508.pdf", atari=True)
# breakout_metric.measure(date(2013,12,19), 225, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# breakout_metric.measure(date(2015,2,26), 401.2, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# breakout_metric.measure(date(2015,10,22), 375, "DoubleDQN", "https://pdfs.semanticscholar.org/3b97/32bb07dc99bde5e1f9f75251c6ea5039373e.pdf")

# breakout_metric.measure(date(2015,11,20), 385.5, "DQN", "https://arxiv.org/abs/1511.06581v1")
# breakout_metric.measure(date(2015,11,20), 418.5, "DDQN", "https://arxiv.org/abs/1511.06581v1")
# breakout_metric.measure(date(2015,11,20), 345.3, "Duel", "https://arxiv.org/abs/1511.06581v1")

# breakout_metric.measure(date(2016,6,16), 766.8, "A3C LSTM", "https://arxiv.org/pdf/1602.01783.pdf")

# Centipede
centipede_metric = simple_games.metric("Atari 2600 Centipede", scale=atari_linear, target=11963, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# centipede_metric.measure(date(2015, 2, 26), 8309, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# centipede_metric.measure(date(2015,11,20), 4657, "DQN","https://arxiv.org/abs/1511.06581v1")
# centipede_metric.measure(date(2015,11,20), 5409, "DDQN","https://arxiv.org/abs/1511.06581v1")
# centipede_metric.measure(date(2015,11,20), 7561, "Duel","https://arxiv.org/abs/1511.06581v1")

# Chopper Command
chopper_command_metric = simple_games.metric("Atari 2600 Chopper Command", scale=atari_linear, target=9882, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# chopper_command_metric.measure(date(2015, 2, 26), 6687, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# chopper_command_metric.measure(date(2015,11,20), 6126, "DQN","https://arxiv.org/abs/1511.06581v1")
# chopper_command_metric.measure(date(2015,11,20), 5809, "DDQN","https://arxiv.org/abs/1511.06581v1")
# chopper_command_metric.measure(date(2015,11,20), 11215, "Duel","https://arxiv.org/abs/1511.06581v1")

# Crazy Climber
crazy_climber_metric = simple_games.metric("Atari 2600 Crazy Climber", scale=atari_linear, target=35411, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# crazy_climber_metric.measure(date(2015, 2, 26), 114103, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# crazy_climber_metric.measure(date(2015,11,20), 110763, "DQN","https://arxiv.org/abs/1511.06581v1")
# crazy_climber_metric.measure(date(2015,11,20), 117282, "DDQN","https://arxiv.org/abs/1511.06581v1")
# crazy_climber_metric.measure(date(2015,11,20), 143570, "Duel","https://arxiv.org/abs/1511.06581v1")

# Demon Attack
demon_attack_metric = simple_games.metric("Atari 2600 Demon Attack", scale=atari_linear, target=3401, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# demon_attack_metric.measure(date(2015, 2, 26), 9711, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# demon_attack_metric.measure(date(2015,11,20), 12149, "DQN","https://arxiv.org/abs/1511.06581v1")
# demon_attack_metric.measure(date(2015,11,20), 58044, "DDQN","https://arxiv.org/abs/1511.06581v1")
# demon_attack_metric.measure(date(2015,11,20), 60813, "Duel","https://arxiv.org/abs/1511.06581v1")

# Double Dunk
# TODO: investigate alternate scale
double_dunk_metric = simple_games.metric("Atari 2600 Double Dunk", scale=atari_linear, target=-15.5, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# double_dunk_metric.measure(date(2015, 2, 26), -18.1, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# double_dunk_metric.measure(date(2015,11,20), -6.6, "DQN","https://arxiv.org/abs/1511.06581v1")
# double_dunk_metric.measure(date(2015,11,20), -5.5, "DDQN","https://arxiv.org/abs/1511.06581v1")
# double_dunk_metric.measure(date(2015,11,20), 0.1, "Duel","https://arxiv.org/abs/1511.06581v1")

# Enduro
enduro_metric = simple_games.metric("Atari 2600 Enduro", scale=atari_linear, target=309.6, target_source="https://pdfs.semanticscholar.org/340f/48901f72278f6bf78a04ee5b01df208cc508.pdf", atari=True)
# enduro_metric.measure(date(2013,12,19), 661, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# enduro_metric.measure(date(2015,2,26), 301, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# enduro_metric.measure(date(2015,10,22), 319, "DoubleDQN", "https://pdfs.semanticscholar.org/3b97/32bb07dc99bde5e1f9f75251c6ea5039373e.pdf")

# enduro_metric.measure(date(2015,11,20), 729.0, "DQN", "https://arxiv.org/abs/1511.06581v1")
# enduro_metric.measure(date(2015,11,20), 1211.8, "DDQN", "https://arxiv.org/abs/1511.06581v1")
# enduro_metric.measure(date(2015,11,20), 2258.2, "Duel", "https://arxiv.org/abs/1511.06581v1")

# enduro_metric.measure(date(2016,6,16), 82.5, "A3C LSTM", "https://arxiv.org/pdf/1602.01783.pdf")

# Fishing Derby
fishing_derby_metric = simple_games.metric("Atari 2600 Fishing Derby", scale=atari_linear, target=5.5, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# fishing_derby_metric.measure(date(2015, 2, 26), -0.8, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# fishing_derby_metric.measure(date(2015,11,20), -4.9, "DQN","https://arxiv.org/abs/1511.06581v1")
# fishing_derby_metric.measure(date(2015,11,20), 15.5, "DDQN","https://arxiv.org/abs/1511.06581v1")
# fishing_derby_metric.measure(date(2015,11,20), 46.4, "Duel","https://arxiv.org/abs/1511.06581v1")

# Freeway
freeway_metric = simple_games.metric("Atari 2600 Freeway", scale=atari_linear, target=29.6, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# freeway_metric.measure(date(2015, 2, 26), 30.3, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# freeway_metric.measure(date(2015,11,20), 30.8, "DQN","https://arxiv.org/abs/1511.06581v1")
# freeway_metric.measure(date(2015,11,20), 33.3, "DDQN","https://arxiv.org/abs/1511.06581v1")
# freeway_metric.measure(date(2015,11,20), 0, "Duel","https://arxiv.org/abs/1511.06581v1")

# Frostbite
frostbite_metric = simple_games.metric("Atari 2600 Frostbite", scale=atari_linear, target=4355, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# frostbite_metric.measure(date(2015, 2, 26), 328.3, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# frostbite_metric.measure(date(2015,11,20), 797.7, "DQN","https://arxiv.org/abs/1511.06581v1")
# frostbite_metric.measure(date(2015,11,20), 1683.3, "DDQN","https://arxiv.org/abs/1511.06581v1")
# frostbite_metric.measure(date(2015,11,20), 4672, "Duel","https://arxiv.org/abs/1511.06581v1")

# Gopher
gopher_metric = simple_games.metric("Atari 2600 Gopher", scale=atari_linear, target=2321, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# gopher_metric.measure(date(2015, 2, 26), 8520, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# gopher_metric.measure(date(2015,11,20), 8777, "DQN","https://arxiv.org/abs/1511.06581v1")
# gopher_metric.measure(date(2015,11,20), 14840, "DDQN","https://arxiv.org/abs/1511.06581v1")
# gopher_metric.measure(date(2015,11,20), 15718, "Duel","https://arxiv.org/abs/1511.06581v1")

# Gravitar
gravitar_metric = simple_games.metric("Atari 2600 Gravitar", scale=atari_linear, target=2672, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# gravitar_metric.measure(date(2015, 2, 26), 306.7, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# gravitar_metric.measure(date(2015,11,20), 473, "DQN","https://arxiv.org/abs/1511.06581v1")
# gravitar_metric.measure(date(2015,11,20), 412, "DDQN","https://arxiv.org/abs/1511.06581v1")
# gravitar_metric.measure(date(2015,11,20), 588, "Duel","https://arxiv.org/abs/1511.06581v1")

# H.E.R.O.
hero_metric = simple_games.metric("Atari 2600 HERO", scale=atari_linear, target=25763, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# hero_metric.measure(date(2015, 2, 26), 19950, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# hero_metric.measure(date(2015,11,20), 20437, "DQN","https://arxiv.org/abs/1511.06581v1")
# hero_metric.measure(date(2015,11,20), 20130, "DDQN","https://arxiv.org/abs/1511.06581v1")
# hero_metric.measure(date(2015,11,20), 20818, "Duel","https://arxiv.org/abs/1511.06581v1")

# Ice Hockey
ice_hockey_metric = simple_games.metric("Atari 2600 Ice Hockey", scale=atari_linear, target=0.9, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# ice_hockey_metric.measure(date(2015, 2, 26), -1.6, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# James Bond
james_bond_metric = simple_games.metric("Atari 2600 James Bond", scale=atari_linear, target=406.7, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# james_bond_metric.measure(date(2015, 2, 26), 576.7, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Kangaroo
kangaroo_metric = simple_games.metric("Atari 2600 Kangaroo", scale=atari_linear, target=3035, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# kangaroo_metric.measure(date(2015, 2, 26), 6740, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Krull
krull_metric = simple_games.metric("Atari 2600 Krull", scale=atari_linear, target=2395, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# krull_metric.measure(date(2015, 2, 26), 3805, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Kung-Fu Master
kung_fu_master_metric = simple_games.metric("Atari 2600 Kung-Fu Master", scale=atari_linear, target=22736, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# kung_fu_master_metric.measure(date(2015, 2, 26), 23270, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Montezuma's Revenge
montezumas_revenge_metric = simple_games.metric("Atari 2600 Montezuma's Revenge", scale=atari_linear, target=4367, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# montezumas_revenge_metric.measure(date(2015, 2, 26), 0, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Ms. Pacman
ms_pacman_metric = simple_games.metric("Atari 2600 Ms. Pacman", scale=atari_linear, target=15693, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# ms_pacman_metric.measure(date(2015, 2, 26), 2311, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Name This Game
name_this_game_metric = simple_games.metric("Atari 2600 Name This Game", scale=atari_linear, target=4076, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# name_this_game_metric.measure(date(2015, 2, 26), 7257, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Pong
pong_metric = simple_games.metric("Atari 2600 Pong", scale=atari_linear, target=9.3, target_source="https://pdfs.semanticscholar.org/340f/48901f72278f6bf78a04ee5b01df208cc508.pdf", atari=True)
# pong_metric.measure(date(2013,12,19), 21, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# pong_metric.measure(date(2015,2,26), 18.9, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# pong_metric.measure(date(2015,10,22), 21, "DoubleDQN", "https://pdfs.semanticscholar.org/3b97/32bb07dc99bde5e1f9f75251c6ea5039373e.pdf")

# pong_metric.measure(date(2015,11,20), 21, "DQN", "https://arxiv.org/abs/1511.06581v1")
# pong_metric.measure(date(2015,11,20), 20.9, "DDQN", "https://arxiv.org/abs/1511.06581v1")
# pong_metric.measure(date(2015,11,20), 19.5, "Duel", "https://arxiv.org/abs/1511.06581v1")

# pong_metric.measure(date(2016,6,16), 10.7, "A3C LSTM", "https://arxiv.org/pdf/1602.01783.pdf")

# Private Eye
private_eye_metric = simple_games.metric("Atari 2600 Private Eye", scale=atari_linear, target=69571, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# private_eye_metric.measure(date(2015, 2, 26), 1788, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Q*Bert
q_bert_metric = simple_games.metric("Atari 2600 Q*Bert", scale=atari_linear, target=13455, target_source="https://pdfs.semanticscholar.org/340f/48901f72278f6bf78a04ee5b01df208cc508.pdf", atari=True)
# q_bert_metric.measure(date(2013,12,19), 4500, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# q_bert_metric.measure(date(2015,2,26), 10596, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# q_bert_metric.measure(date(2015,10,22), 14875, "DoubleDQN", "https://pdfs.semanticscholar.org/3b97/32bb07dc99bde5e1f9f75251c6ea5039373e.pdf")

# q_bert_metric.measure(date(2015,11,20), 13117.3, "DQN", "https://arxiv.org/abs/1511.06581v1")
# q_bert_metric.measure(date(2015,11,20), 15088.5, "DDQN", "https://arxiv.org/abs/1511.06581v1")
# q_bert_metric.measure(date(2015,11,20), 19220, "Duel", "https://arxiv.org/abs/1511.06581v1")

# q_bert_metric.measure(date(2016,6,16), 21307, "A3C LSTM", "https://arxiv.org/pdf/1602.01783.pdf")

# River Raid
river_raid_metric = simple_games.metric("Atari 2600 River Raid", scale=atari_linear, target=13513, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# river_raid_metric.measure(date(2015, 2, 26), 8316, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Road Runner
road_runner_metric = simple_games.metric("Atari 2600 Road Runner", scale=atari_linear, target=7845, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# road_runner_metric.measure(date(2015, 2, 26), 18257, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Robotank
robotank_metric = simple_games.metric("Atari 2600 Robotank", scale=atari_linear, target=11.9, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# robotank_metric.measure(date(2015, 2, 26), 51.6, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Seaquest
seaquest_metric = simple_games.metric("Atari 2600 Seaquest", scale=atari_linear, target=20182, target_source="https://pdfs.semanticscholar.org/340f/48901f72278f6bf78a04ee5b01df208cc508.pdf", atari=True)
# seaquest_metric.measure(date(2013,12,19), 1740, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# seaquest_metric.measure(date(2015,2,26), 5286, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# seaquest_metric.measure(date(2015,10,22), 7995, "DoubleDQN", "https://arxiv.org/abs/1509.06461")

# seaquest_metric.measure(date(2015,11,20), 5860.6, "DQN", "https://arxiv.org/abs/1511.06581v1")
# seaquest_metric.measure(date(2015,11,20), 16452.7, "DDQN", "https://arxiv.org/abs/1511.06581v1")
# seaquest_metric.measure(date(2015,11,20), 50254.2, "Duel", "https://arxiv.org/abs/1511.06581v1")

# seaquest_metric.measure(date(2016,6,16), 1326.1, "A3C LSTM", "https://arxiv.org/pdf/1602.01783.pdf")

# Space Invaders
space_invaders_metric = simple_games.metric("Atari 2600 Space Invaders", scale=atari_linear, target=1652, target_source="https://pdfs.semanticscholar.org/340f/48901f72278f6bf78a04ee5b01df208cc508.pdf", atari=True)
# space_invaders_metric.measure(date(2013,12,19), 1075, "DQN", "https://arxiv.org/pdf/1312.5602.pdf")
# space_invaders_metric.measure(date(2015,2,26), 1976, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")
# space_invaders_metric.measure(date(2015,10,22), 3154, "DoubleDQN", "https://arxiv.org/abs/1509.06461")

# space_invaders_metric.measure(date(2015,11,20), 1692.3, "DQN", "https://arxiv.org/abs/1511.06581v1")
# space_invaders_metric.measure(date(2015,11,20), 2525.5, "DDQN", "https://arxiv.org/abs/1511.06581v1")
# space_invaders_metric.measure(date(2015,11,20), 6427.3, "Duel", "https://arxiv.org/abs/1511.06581v1")

# space_invaders_metric.measure(date(2016,6,16), 23846, "A3C LSTM", "https://arxiv.org/pdf/1602.01783.pdf")

# Star Gunner
star_gunner_metric = simple_games.metric("Atari 2600 Star Gunner", scale=atari_linear, target=10250, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# star_gunner_metric.measure(date(2015, 2, 26), 57997, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Tennis
# TODO: negative linear scale?
tennis_metric = simple_games.metric("Atari 2600 Tennis", scale=atari_linear, target=-8.9, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# tennis_metric.measure(date(2015, 2, 26), -2.5, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Time Pilot
time_pilot_metric = simple_games.metric("Atari 2600 Time Pilot", scale=atari_linear, target=5925, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# time_pilot_metric.measure(date(2015, 2, 26), 5947, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Tutankham
tutankham_metric = simple_games.metric("Atari 2600 Tutankham", scale=atari_linear, target=167.6, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# tutankham_metric.measure(date(2015, 2, 26), 186.7, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Up and Down
up_and_down_metric = simple_games.metric("Atari 2600 Up and Down", scale=atari_linear, target=9082, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# up_and_down_metric.measure(date(2015, 2, 26), 8456, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Venture
venture_metric = simple_games.metric("Atari 2600 Venture", scale=atari_linear, target=1188, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# venture_metric.measure(date(2015, 2, 26), 3800, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Video Pinball
video_pinball_metric = simple_games.metric("Atari 2600 Video Pinball", scale=atari_linear, target=17298, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# video_pinball_metric.measure(date(2015, 2, 26), 42684, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Wizard of Wor
wizard_of_wor_metric = simple_games.metric("Atari 2600 Wizard of Wor", scale=atari_linear, target=4757, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# wizard_of_wor_metric.measure(date(2015, 2, 26), 3393, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Zaxxon
zaxxon_metric = simple_games.metric("Atari 2600 Zaxxon", scale=atari_linear, target=9173, target_source="https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508", atari=True)
# zaxxon_metric.measure(date(2015, 2, 26), 4977, "DQN", "https://www.semanticscholar.org/paper/Human-level-control-through-deep-reinforcement-Mnih-Kavukcuoglu/340f48901f72278f6bf78a04ee5b01df208cc508")

# Results from the original DQN paper

beam_rider_metric.measure(None, 5184, "DQN best", "https://arxiv.org/abs/1312.5602")
breakout_metric.measure(None, 225, "DQN best", "https://arxiv.org/abs/1312.5602")
enduro_metric.measure(None, 661, "DQN best", "https://arxiv.org/abs/1312.5602")
pong_metric.measure(None, 21, "DQN best", "https://arxiv.org/abs/1312.5602")
q_bert_metric.measure(None, 4500, "DQN best", "https://arxiv.org/abs/1312.5602")
seaquest_metric.measure(None, 1740, "DQN best", "https://arxiv.org/abs/1312.5602")
space_invaders_metric.measure(None, 1075, "DQN best", "https://arxiv.org/abs/1312.5602")

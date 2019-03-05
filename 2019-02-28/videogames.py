PRICE_PER_LETTER = .32
import math

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
    "Call Of Duty: Infinite Warfare",
    "Call Of Duty: Modern Warfare III",
]

for game in video_games:
  length = len(game.replace(" ", ""))

  print("The cost of the banner for", game, " is: $", round(length * PRICE_PER_LETTER, 3))


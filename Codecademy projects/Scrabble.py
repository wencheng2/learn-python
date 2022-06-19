# Scrabble project from Codecademy
# 
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create dictionary where key = letters and value = points
letter_to_points = {key:value for key, value in zip(letters, points)}
# Add value of no words (" ") as 0
letter_to_points[" "] = 0

# Define function that calculates score of words
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Test score_word function
brownie_points = score_word("BROWNIE")
print(brownie_points) #should be 15

# Create dictionary of players and their words
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Define function to add words to player list
def play_word(player, word):
  # Check if player is in dictionary and new word isn't
  if player in player_to_words:
    if not word in player_to_words[player]:
        player_to_words[player].append(word)
        return player_to_words
    else:
        print("You already played that word")
  else:
    print("Player does not exist")

# Convert players' words to score
def update_point_totals(player, word):
  player_to_points = {}
  play_word(player, word)
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print("Current scores are:", "\n", player_to_points)
  print("Current words are:", "\n", player_to_words)

# Test - "Wow" should be to Prof Reader's list, and Prof Reader should have the highest score of 40
update_point_totals("Prof Reader", "Wow")

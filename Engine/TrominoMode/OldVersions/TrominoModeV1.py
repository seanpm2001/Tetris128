# Start of script
import math
import random
import pygui # I don't know any graphics libraries, so this is filler
# Tromino
def TrominoLineClassic():
  # A classic Tromino line piece. Not yet available
def TrominoCornerClassic():
  # A classic Tromino corner piece. Not yet available
# Score
curScoreTrominoClassicMode = int(0)
highScoreTrominoClassicMode = int(0)
# Pieces
curPiece = str("Tromino (line)")
curPieceID = float(3.0)
if (nextPiece == 3.0):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - White")
if (nextPiece == 3.1):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Black")
if (nextPiece == 3.2):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Grey/Gray")
if (nextPiece == 3.3):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Ruby red")
if (nextPiece == 3.4):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Olive green")
if (nextPiece == 3.5):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Silver")
if (nextPiece == 3.6):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Orange")
if (nextPiece == 3.7):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Yellow")
if (nextPiece == 3.8):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Salmon pink")
if (nextPiece == 3.9):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Magenta")
if (nextPiece == 3.10):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Cyan")
if (nextPiece == 3.11):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Turquiose")
if (nextPiece == 3.12):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Brown")
if (nextPiece == 3.13):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Bronze")
if (nextPiece == 3.14):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Gold")
if (nextPiece == 3.15):
  # Wait for piece to be placed
  curPiece = str("Tromino (line) - Purple")
if (nextPiece == 3.16):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - White")
if (nextPiece == 3.17):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Black")
if (nextPiece == 3.18):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Grey/Gray")
if (nextPiece == 3.19):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Ruby red")
if (nextPiece == 3.20):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Olive green")
if (nextPiece == 3.21):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Silver")
if (nextPiece == 3.22):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Orange")
if (nextPiece == 3.23):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Yellow")
if (nextPiece == 3.24):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Salmon pink")
if (nextPiece == 3.25):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Magenta")
if (nextPiece == 3.26):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Cyan")
if (nextPiece == 3.27):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Turquiose")
if (nextPiece == 3.28):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Brown")
if (nextPiece == 3.29):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Bronze")
if (nextPiece == 3.30):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Gold")
if (nextPiece == 3.31):
  # Wait for piece to be placed
  curPiece = str("Tromino (angle) - Purple")
else:
  print("Error, no piece with this ID " + str(nextPiece) + " found. Game crashed")
print("Next:\n" + str(curPiece))
nextPiece = float(3.0)
nextPiece = random.randint(3.0, 3.31) # I am not sure if float is compatible with randint
'''
Piece ID list or Tromino mode:
Tromino1(white) - 3.0
Tromino1(black) - 3.1
Tromino1(grey) - 3.2
Tromino1(ruby red) - 3.3
Tromino1(olive green) - 3.4
Tromino1(silver) - 3.5
Tromino1(orange) - 3.6
Tromino1(yellow) - 3.7
Tromino1(salmon pink) - 3.8
Tromino1(magenta) - 3.9
Tromino1(cyan) - 3.10
Tromino1(turquiose) - 3.11
Tromino1(brown) - 3.12
Tromino1(bronze) - 3.13
Tromino1(gold) - 3.14
Tromino1(purple) - 3.15
Tromino2(white) - 3.16
Tromino2(black) - 3.17
Tromino2(grey) - 3.18
Tromino2(ruby red) - 3.19
Tromino2(olive green) - 3.20
Tromino2(silver) - 3.21
Tromino2(orange) - 3.22
Tromino2(yellow) - 3.23
Tromino2(salmon pink) - 3.24
Tromino2(magenta) - 3.25
Tromino2(cyan) - 3.26
Tromino2(turquiose) - 3.27
Tromino2(brown) - 3.28
Tromino2(bronze) - 3.29
Tromino2(gold) - 3.30
Tromino2(purple) - 3.31
32 IDs for colored Tromino pieces
'''
# Run
print("This script is highly incomplete. Please close the program")
noMore = input("Press [ENTER] key to quit")
print("Goodbye!")
# End of script

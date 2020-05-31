# Start of script
import math
import random
import pygui # I don't know any graphics libraries, so this is filler
# Tetromino
def TetrominoLineClassic():
  # A classic Tetromino line piece. Not yet available
def TetrominoSquareClassic():
  # A classic Tetromino square piece. Not yet available
def TetrominoLClassic():
  # A classic Tetromino L piece. Not yet available
def TetrominoTpieceClassic():
  # A classic Tetromino T piece. Not yet available
def TetrominoInverseSkewClassic():
  # A classic Tetromino inverse skew piece. Not yet available
# Score
curScoreTetrominoClassicMode = int(0)
highScoreTetrominoClassicMode = int(0)
# Pieces
curPiece = str("Tetromino (line)")
curPieceID = float(3.0)
if (nextPiece == 3.0):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - White")
if (nextPiece == 3.1):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Black")
if (nextPiece == 3.2):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Grey/Gray")
if (nextPiece == 3.3):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Ruby red")
if (nextPiece == 3.4):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Olive green")
if (nextPiece == 3.5):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Silver")
if (nextPiece == 3.6):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Orange")
if (nextPiece == 3.7):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Yellow")
if (nextPiece == 3.8):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Salmon pink")
if (nextPiece == 3.9):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Magenta")
if (nextPiece == 3.10):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Cyan")
if (nextPiece == 3.11):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Turquiose")
if (nextPiece == 3.12):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Brown")
if (nextPiece == 3.13):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Bronze")
if (nextPiece == 3.14):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Gold")
if (nextPiece == 3.15):
  # Wait for piece to be placed
  curPiece = str("Tetromino (line) - Purple")
if (nextPiece == 3.16):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - White")
if (nextPiece == 3.17):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Black")
if (nextPiece == 3.18):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Grey/Gray")
if (nextPiece == 3.19):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Ruby red")
if (nextPiece == 3.20):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Olive green")
if (nextPiece == 3.21):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Silver")
if (nextPiece == 3.22):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Orange")
if (nextPiece == 3.23):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Yellow")
if (nextPiece == 3.24):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Salmon pink")
if (nextPiece == 3.25):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Magenta")
if (nextPiece == 3.26):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Cyan")
if (nextPiece == 3.27):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Turquiose")
if (nextPiece == 3.28):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Brown")
if (nextPiece == 3.29):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Bronze")
if (nextPiece == 3.30):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Gold")
if (nextPiece == 3.31):
  # Wait for piece to be placed
  curPiece = str("Tetromino (square) - Purple")
# Other pieces not yet listed
else:
  print("Error, no piece with this ID " + str(nextPiece) + " found. Game crashed")
print("Next:\n" + str(curPiece))
nextPiece = float(3.0)
nextPiece = random.randint(3.0, 3.31) # I am not sure if float is compatible with randint
'''
Piece ID list or Tetromino mode:
Tetromino1(white) - 3.0
Tetromino1(black) - 3.1
Tetromino1(grey) - 3.2
Tetromino1(ruby red) - 3.3
Tetromino1(olive green) - 3.4
Tetromino1(silver) - 3.5
Tetromino1(orange) - 3.6
Tetromino1(yellow) - 3.7
Tetromino1(salmon pink) - 3.8
Tetromino1(magenta) - 3.9
Tetromino1(cyan) - 3.10
Tetromino1(turquiose) - 3.11
Tetromino1(brown) - 3.12
Tetromino1(bronze) - 3.13
Tetromino1(gold) - 3.14
Tetromino1(purple) - 3.15
Tetromino2(white) - 3.16
Tetromino2(black) - 3.17
Tetromino2(grey) - 3.18
Tetromino2(ruby red) - 3.19
Tetromino2(olive green) - 3.20
Tetromino2(silver) - 3.21
Tetromino2(orange) - 3.22
Tetromino2(yellow) - 3.23
Tetromino2(salmon pink) - 3.24
Tetromino2(magenta) - 3.25
Tetromino2(cyan) - 3.26
Tetromino2(turquiose) - 3.27
Tetromino2(brown) - 3.28
Tetromino2(bronze) - 3.29
Tetromino2(gold) - 3.30
Tetromino2(purple) - 3.31
Tetromino3(white) - 3.32
Tetromino3(black) - 3.33
Tetromino3(grey) - 3.34
Tetromino3(ruby red) - 3.35
Tetromino3(olive green) - 3.36
Tetromino3(silver) - 3.37
Tetromino3(orange) - 3.38
Tetromino3(yellow) - 3.39
Tetromino3(salmon pink) - 3.40
Tetromino3(magenta) - 3.41
Tetromino3(cyan) - 3.42
Tetromino3(turquiose) - 3.43
Tetromino3(brown) - 3.44
Tetromino3(bronze) - 3.45
Tetromino3(gold) - 3.46
Tetromino3(purple) - 3.47
Tetromino4(white) - 3.48
Tetromino4(black) - 3.49
Tetromino4(grey) - 3.50
Tetromino4(ruby red) - 3.51
Tetromino4(olive green) - 3.52
Tetromino4(silver) - 3.53
Tetromino4(orange) - 3.54
Tetromino4(yellow) - 3.55
Tetromino4(salmon pink) - 3.56
Tetromino4(magenta) - 3.57
Tetromino4(cyan) - 3.58
Tetromino4(turquiose) - 3.59
Tetromino4(brown) - 3.60
Tetromino4(bronze) - 3.61
Tetromino4(gold) - 3.62
Tetromino4(purple) - 3.63
Tetromino5(white) - 3.64
Tetromino5(black) - 3.65
Tetromino5(grey) - 3.66
Tetromino5(ruby red) - 3.67
Tetromino5(olive green) - 3.68
Tetromino5(silver) - 3.69
Tetromino5(orange) - 3.70
Tetromino5(yellow) - 3.71
Tetromino5(salmon pink) - 3.72
Tetromino5(magenta) - 3.73
Tetromino5(cyan) - 3.74
Tetromino5(turquiose) - 3.75
Tetromino5(brown) - 3.76
Tetromino5(bronze) - 3.77
Tetromino5(gold) - 3.78
Tetromino5(purple) - 3.79
80 IDs for colored Tetromino pieces
'''
# Run
print("This script is highly incomplete. Please close the program")
noMore = input("Press [ENTER] key to quit")
print("Goodbye!")
# End of script

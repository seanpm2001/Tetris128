# Start of script
""" The menu system script for Tetris 128 """
# Is there a language with a similar syntax to what I am writing here, or is this a way Python can be written? I don't know if Python allows function names to have decimals in them.
# This script is a work in progress, and alot currently doesn't function, as I haven't learned the proper way of doing this yet.
class menumaster
import random # Just in case it is needed

def objectpack.titlescreen.foreground():
  titleHeader = str("TETRIS 128\nBy Seanpm2001 Et All,")
  titleButton1 = str("Play")
  titleButton2 = str("Quit")

def objectpack.gameMode.Select.foreground():
  titleHeader2 = str("Select a gamemode")
  gameOption1Str = str("Mino mode")
  gameOption2Str = str("Domino mode")
  gameOption3Str = str("Tromino mode")
  gameOption4Str = str("Tetromino mode")
  gameOption5Str = str("Pentomino mode")
  gameOption6Str = str("Hexomino mode")
  gameOption7Str = str("Heptomino mode")
  gameOption8Str = str("Octomino mode")
  gameOption9Str = str("Nonomino mode")
  gameOption10Str = str("Decomino mode")
  gameOption11Str = str("Party mode") # Party mode mixes various polyominoes into gameplay, so that you can have Tetrominoes, Pentominoes, Dominoes, etc. all at once

def partyMode.setup():
  # Incomplete
  print ("Party mode setup")
  print ("Minoes [x] [ ]")
  print ("Dominoes [x] [ ]")
  print ("Trominoes [x] [ ]")
  print ("Tetrominoes [x] [ ]")
  print ("Pentominoes [x] [ ]")
  print ("Hexominoes [x] [ ]")
  print ("Septominoes [x] [ ]")
  print ("Heptominoes [x] [ ]")
  print ("Octominoes [x] [ ]")
  print ("Nonominoes [x] [ ]")  
  print ("Decominoes [x] [ ]")

def gameType.selector():
  titleHeader3 = str("Select a game type")
  gameTypeOption1Str = str("Not Tetris")
  gameTypeOption2Str = str("Puyo Puyo") # Am I allowed to use the name? The name might have to be changed
  gameTypeOption3Str = str("Normal")
  gameTypeOption4Str = str("Hospital (domino)") # Similar to the Dr. Mario style of gameplay

def gamePersonalize.graphics():
  titleHeader4 = str("Setup your game graphics\nPress X to skip") # X letter chosen for video game console cross-compatibility, since most controllers have an X key
  gameGraphicsOption1Str = str("Monochrome (black and white)") # 2 bit
  gameGraphicsOption2Str = str("16 color") # 4 bit
  gameGraphicsOption3Str = str("256 color (8 bit)") # 8 bit
  gameGraphicsOption4Str = str("65536 color (16 bit)") # 16 bit, do we really need 24 or 32 bit graphics for Tetris right now?
  gameGraphicsOption5Str = str("Softbody graphics")
  
def ingame.pause():
  pauseHeader1 = str("Game is paused")
  input1 = input("Save and quit") # Need a way to cycle through inputs without activating all 5 input methods in a row
  input2 = input("Quit without saving")
  input3 = input("Add/remove players")
  input4 = input("Settings")
  input5 = input("Resume (any key)") # Wheres the "any" key

""" File info
File type: Python source file (*.py)
File version: 1 (Tuesday, May 4th 2021 at 10:09 pm)
Line count (including blank lines and compiler line): 71
"""
# End of script

// Start of script
// import math
// import random
// import pygui # This likely doesn't work, I don't know any GUI libraries
// Mino (1)
#include <iostream>
#include <vector>
#include <stdexcept>
int softbodyMino() {
  // This script is for the mino piece, a custom piece that is only 1x1
  std::cout << "Mino mode is currently unavailable for the softbody engine." ;
}
// Domino (2)
int softbodyDomino() {
  // This script is for the domino piece
  std::cout << "Domino mode is currently unavailable for the softbody engine.");
}
// Trominoes (3)
int softbodyTromino() {
  std::cout << "Tromino mode is currently unavailable for the softbody engine.");
  int softbodyTrominoAngle3piece() {
    // This script is for the tromino angle 3 piece |_
  }
  int softbodyTromino3LinePiece() {
    // This script is for the Tromino 3 line piece |
  }
}  	
// Tetrominoes (4)
int softbodyTetromino() {
  std::cout << "Tetromino mode is currently unavailable for the softbody engine");
  int softbodyLine4piece() {
    // This script is for the Tetromino line piece |
  }
  int softbodySquare4Piece() {
    // This script is for the Tetromino square piece ::
  }
  int softbodyL4piece() {
    // This script is for the Tetromino square piece L
  }
  int softbodyInverseSkew4piece() {
    // This script is for the Tetromino Inverse skew piece []
  }
  int softbodyTSpin4piece() {
    // This script is for the Tetromino T-Spin piece
  }
}
// Pentominoes (5)
int softbodyPentomino() {
  std::cout << "Pentomino mode is currently unavailable for the softbody engine");
  int pentomino5LinePiece() {
    // This script is for the Pentomino 5 line piece |
  }
  // More Coming soon (I don't know how to name or place this many pieces yet)
}
// Hexominoes (6)
int softbodyHexomino() {
  std::cout << "Hexomino mode is currently unavailable for the softbody engine");
  int hexomino6LinePiece() {
    // This script is for the Hexomino 6 line piece |
  }
// More Coming soon (I don't know how to name or place this many pieces yet)
}
// Septominoes (7)
int softbodyHeptomino() {
  std::cout << "Heptomino mode is currently unavailable for the softbody engine");
  int septomino7LinePiece() {
    // This script is for the septomino 7 line piece |
    }
// More Coming soon (I don't know how to name or place this many pieces yet)
}
// Octominoes (8)
int softbodyOctomino() {
  std::cout << "Octomino mode is currently unavailable for the softbody engine");
  int octomino8LinePiece() {
    // This script is for the octomino 8 line piece |
  }
// More Coming soon (I don't know how to name or place this many pieces yet)
}
// Nonominoes (9)
int softbodyNonomino() {
  std::cout << "Nonomino mode is currently unavailable for the softbody engine");
  int nonomino9LinePiece() {
    // This script is for the nonomino 9 line piece |
  }
// More Coming soon (I don't know how to name or place this many pieces yet)
}
// Decominoes (10)
int softbodyDecomino() {
  std::cout << "Decomino mode is currently unavailable for the softbody engine");
  int decomino10LinePiece() {
    // This script is for the decomino 10 line piece |
  }
// More Coming soon (I don't know how to name or place this many pieces yet)
}
int errorHandlingCPP() {
    try {
        std::vector<int> vec{3, 4, 3, 1};
        int i{vec.at(4)}; // Throws an exception, std::out_of_range (indexing for vec is from 0-3 not 1-4)
    }
    // An exception handler, catches std::out_of_range, which is thrown by vec.at(4)
    catch (std::out_of_range &e) {
        std::cerr << "Accessing a non-existent element: " << e.what() << '\n';
    }
    // To catch any other standard library exceptions (they derive from std::exception)
    catch (std::exception &e) {
        std::cerr << "Exception thrown: " << e.what() << '\n';
    }
    // Catch any unrecognised exceptions (i.e. those which don't derive from std::exception)
    catch (...) {
        std::cerr << "Some fatal error\n";
    }
}
// Run
std::cout << "This program is highly incomplete. Please exit");
// noMore = input("Press [ENTER] key to exit")
// print("Goodbye")
/* File info
* File type: C++ source file (*.cpp, *.cxx)
* File version: 1 (Wednesday, May 5th 2021 at 5:26 pm)
* Line count (including blank lines and compiler line): 123
*/
// End of script

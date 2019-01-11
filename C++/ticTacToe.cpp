#include <iostream>

using namespace std;

enum Player {X, O, Empty};

class Slot {
	
	private:
	Player playerHeld;
	
	public:
	Player getPlayerHeld() {
		return playerHeld;
	}
	
	void setPlayerHeld(Player aPlayer) {
		playerHeld = aPlayer;
	}
	
};

int main() {
	bool win = false;
	bool player1Turn = true;
	Player thisPlayer;
	int col;
	int row;
	
	Slot ar[3][3];
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			ar[i][j].setPlayerHeld(Empty);
		}
	}
	
	while (win == false) {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (ar[i][j].getPlayerHeld() == X) {
					cout << "|X|";
				} else if (ar[i][j].getPlayerHeld() == O) {
					cout << "|O|";
				} else {
					cout << "| |";
				}
			}
			cout << endl;
		}
		if (player1Turn == true) {
			thisPlayer = X;
		} else {
			thisPlayer = O;
		}
		cout << "Please enter the column number (1-3)";
		cin >> col;
		cout << "Please enter the row number (1-3)";
		cin >> row;
		if (ar[row-1][col-1].getPlayerHeld() == Empty) {
			ar[row-1][col-1].setPlayerHeld(thisPlayer);
			
			if (ar[0][0].getPlayerHeld() == thisPlayer && ar[1][1].getPlayerHeld() == thisPlayer && ar[2][2].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[0][2].getPlayerHeld() == thisPlayer && ar[1][1].getPlayerHeld() == thisPlayer && ar[2][0].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[0][0].getPlayerHeld() == thisPlayer && ar[0][1].getPlayerHeld() == thisPlayer && ar[0][2].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[1][0].getPlayerHeld() == thisPlayer && ar[1][1].getPlayerHeld() == thisPlayer && ar[1][2].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[2][0].getPlayerHeld() == thisPlayer && ar[2][1].getPlayerHeld() == thisPlayer && ar[2][2].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[0][0].getPlayerHeld() == thisPlayer && ar[1][0].getPlayerHeld() == thisPlayer && ar[2][0].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[0][1].getPlayerHeld() == thisPlayer && ar[1][1].getPlayerHeld() == thisPlayer && ar[2][1].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			if (ar[0][2].getPlayerHeld() == thisPlayer && ar[1][2].getPlayerHeld() == thisPlayer && ar[2][2].getPlayerHeld() == thisPlayer) {
				win = true;
			}
			
			if (player1Turn == true) {
				player1Turn = false;
			} else {
				player1Turn = true;
			}
		} else {
			cout << "That spot's already taken";
		}
		
	}
	
	for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (ar[i][j].getPlayerHeld() == X) {
					cout << "|X|";
				} else if (ar[i][j].getPlayerHeld() == O) {
					cout << "|O|";
				} else {
					cout << "| |";
				}
			}
			cout << endl;
		}
	
	if (player1Turn == true) {
				cout << "Player 2 Won!";
	} else {
				cout << "Player 1 Won!";
	}
	
}
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

using namespace std;

enum Mood {Happy, Sad, Mad, Default};

class StateMac {
  public:
  Mood state;
  
  StateMac() {
    state = Default;
  }
  StateMac(Mood newState) {
    state = newState;
  }
  Mood getState() {
    return state;
  }
  void setState(Mood newState) {
    state = newState;
  }
  string talk() {
    switch(state) {
      case Happy : return "I'm happy!";
      case Sad : return "I'm sad...";
      case Mad : return "I'm Mad!!!";
      case Default : return "...";
    }
  }

  string interact(StateMac* aStateMachine) {
    switch (aStateMachine -> getState()) {
      case Sad : if (state == Happy) {
        aStateMachine -> state = Happy;
        return "Oh, cheer up!";
      } else {
        state = Sad;
        return "Darn it, why... Let's cry together...";
      }
      case Mad : if(state == Happy) {
        aStateMachine -> setState(Happy);
        return "There's nothing to be mad about!";
      } else {
        state = Mad;
        return "Why in the world did this have to happen to me!!!";
      }
      case Happy : if (state == Happy) {
        srand(time(NULL));
        switch(rand() % 2) {
          srand(time(NULL));
          case 0 : state = Sad;
          return "Having a bad day today...";
          case 1 : state = Mad;
          return "That guy!!!";
        }
      } else {
        state = Happy;
        return "You look happy, might as well forget about that.";
      }
    }
  }
  
  bool compare(StateMac aStateMachine) {
    if (state == aStateMachine.getState()) {
      return true;
    }
    return false;
  }
};

int getSMarSize(StateMac SMar[]) {
  int counter = 0;
  for (int i = 0; i < 100; i++) {
    if (SMar[i].compare(StateMac())) { 
      break;
    } else {
      counter += 1;
    }
  }
  return counter;
}

void everyone(StateMac SMar[]) {
  for (int i=0; i < 3; i++) {
    cout << "SM" << i << ": " << SMar[i].talk() << endl;
  }
}

int main() {
  StateMac ar[] = {StateMac(Happy), StateMac(Sad), StateMac(Mad)};
  for (int j = 0; j < 5; j++) {
  everyone(ar);
  srand(time(NULL));
  int first = rand() % 3;
  srand(time(NULL));
  int second = rand() % 3;
  string response = ar[first].interact(&ar[second]);
  cout << "SM" << first << " to SM" << second << ": " << response << endl;
  }
}
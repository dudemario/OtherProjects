#include <iostream>
#include <string>

using namespace std;

class Human
{
  public:
  void createHuman(string myName, int myAge)
  {
    name = myName;
    age = myAge;
  }
  
  void setName(string myName)
  {
    name = myName;
  }
  
  string getName()
  {
    return name;
  }
  
  void setAge(int myAge)
  {
    age = myAge;
  }
  
  int getAge()
  {
    return age;
  }
  
  private:
  string name;
  int age;
    
};


int main() {
    int state = 0;
    Human myHuman;
    string newName;
    int newAge;
    string response;
    do {
    switch ( state )
    {
    case(0):
      cout << "Hello There!" << endl;
      cout << "What's your name?" << endl;
      cin >> newName;
      myHuman.setName(newName);
      cout << "Hi " + myHuman.getName() << endl;
      state++;
      break;
    case(1):
      cout << "What's your age?" <<endl;
      cin >> newAge;
      if ((newAge) < 10)
      {
        state = 2;
      }
      else if ((newAge) < 18)
      {
        state = 3;
      }
      else if ((newAge) < 60)
      {
        state = 4;
      }
      else
      {
        state = 5;
      }
      break;
    case(2):
      cout << "Wow, you're small." << endl;
      cout << "Have Fun!" << endl;
      state = 6;
      break;
    case(3):
      cout << "Yo, Wazzup dawg." << endl;
      cout << "How's them school going?" << endl;
      cin >> response;
      cout << "Coolz"<<endl;
      state = 6;
      break;
    case(4):
      cout << "Well, hope I'm not intruding any precious work time." << endl;
      cout << "Let's get back to work then." << endl;
      state = 6;
      break;
    case(5):
      cout << "Wow, you're pretty old" << endl;
      cout << "Have you retired yet?" << endl;
      cin >> response;
      if (response == "yes" or "Yes") 
      {
        cout << "Hope you have a good retirement!" << endl;
      }
      else if (response == "no" or "No")
      {
        cout << "Hope you retire soon!" << endl;
      }
      state = 6;
      break;
    default:
      state = 6;
    }
    } while (state <= 5);
    cout << "See you later, aligator" << endl;
}
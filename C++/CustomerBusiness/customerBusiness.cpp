#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

class Item {
	private:
	string name;
	float cost;
	string description;
	
	public:
	Item () {
		name = "";
		cost = 0;
		description = "";
	}
	
	Item (string name, float cost, string description) {
		this -> name = name;
		this -> cost = cost;
		this -> description = description;
	}
	
	
	void setName(string name) {
		this -> name = name;
	}
	string getName() {
		return name;
	}
	void setCost(float cost) {
		this -> cost = cost;
	}
	float getCost() {
		return cost;
	}
	void setDescription(string description) {
		this -> description = description;
	}
	string getDescription() {
		return description;
	}
	bool compare(Item anotherItem) {
	  if (name == anotherItem.getName()) {
	    if (cost == anotherItem.getCost()) {
	      if (description == anotherItem.getDescription()) {
	        return true;
	      }
	    }
	  }
	  return false;
	}
	
};

class Business {
	private:
	Item records [100];
	string BusinessName;
	
	public:
	void setRecord(Item newRecord, int number) {
		records[number] = newRecord;
	}
	void setBusinessName(string name) {
		BusinessName = name;
	}
	string getBusinessName() {
		return BusinessName;
	}
	Item getRecord(int number) {
		return records[number];
	}
	int getRecordSize() {
	  int counter = 0;
	  for (int i = 0; i < 100; i++) {
	    if (records[i].compare(Item())) { 
	      break;
	    } else {
	      counter += 1;
	    }
	  }
	  return counter;
	}
	void getProducts() {
  	cout << "---------------------------------------------------" << endl;
		cout << "For the business: " << getBusinessName() << endl;
		cout << "Total number of records: " << getRecordSize() << endl;
		for (int i = 0; i < getRecordSize(); i++) {
  		cout << endl;
  		cout << "Product Name: " << getRecord(i).getName() <<  endl;
  		cout << "Price: $" << getRecord(i).getCost() <<  endl;
  		cout << "Description: " << getRecord(i).getDescription() <<  endl;
  	}
  	cout << "---------------------------------------------------" << endl;
    cout << endl;
    cout << endl;
	}
};

class Inventory : public Business {
  public:
  void getProducts(string name) {
  	cout << "---------------------------------------------------" << endl;
		cout << name << "'s Products: " << endl;
		cout << "Total number of products: " << getRecordSize() << endl;
		for (int i = 0; i < getRecordSize(); i++) {
  		cout << "Product Name: " << getRecord(i).getName() <<  endl;
  	}
  	cout << "---------------------------------------------------" << endl;
    cout << endl;
    cout << endl;
	}
};

class Customer {
	private:
	string customerName;
	Business myBusiness;
	Inventory myInventory;
	
	public:
	Customer() {
	}
	
	Customer(string name, Business aBusiness) {
		customerName = name;
		myBusiness = aBusiness;
	}
	
	void setCustomerName(string name) {
		customerName = name;
	}
	string getCustomerName() {
		return customerName;
	}
	
	void getBusinessProducts() {
	  myBusiness.getProducts();
	}
	
	void getInventoryProducts() {
	  myInventory.getProducts(customerName);
	}
	void get1Product(int recordNumber) {
  	cout << myBusiness.getRecord(recordNumber).getName() <<  endl;
  	cout << "$" << myBusiness.getRecord(recordNumber).getCost() <<  endl;
  	cout << myBusiness.getRecord(recordNumber).getDescription() <<  endl;
  	cout << endl;
	}
	void buyProduct(int recordNumber) {
	  cout << "Bought: " << myBusiness.getRecord(recordNumber - 1).getName().substr(0,myBusiness.getRecord(recordNumber - 1).getName().length()-1) << ", Spent: "<<myBusiness.getRecord(recordNumber - 1).getCost()<< endl;
	  myInventory.setRecord(myBusiness.getRecord(recordNumber - 1), myInventory.getRecordSize());
	  int push = 0;
	  int length = myBusiness.getRecordSize();
	  myBusiness.setRecord(Item(), recordNumber - 1);
	  for (int i = 0; i < length; i++) {
	    if (myBusiness.getRecord(i).compare(Item())) {
	      push = 1;
	    } else {
  		myBusiness.setRecord(Item(myBusiness.getRecord(i).getName(), myBusiness.getRecord(i).getCost(), myBusiness.getRecord(i).getDescription()), i - push);
	    }
  	}
  	myBusiness.setRecord(Item(), length - 1);
  	getInventoryProducts();
    cout << endl;
	}
};

int main() {
	Business allBusinesses [100];
	int businessCount = 0;
	int recordCount = 0;
	string line;
	string test;
	string newName;
	float newCost;
	string newDescription;
  fstream myfile ("Database.txt");
  while ( getline (myfile,line) )
  {
  	allBusinesses[businessCount].setBusinessName(line);
  	getline(myfile,line);
  	test = line;
  	while (test.length() != 1) {
	  	recordCount += 1;
			newName = line;
		  getline(myfile,line);
			newCost = stof(line.c_str());
		  getline(myfile,line);
			newDescription = line;
			allBusinesses[businessCount].setRecord(Item(newName, newCost, newDescription), recordCount-1);
			getline(myfile,line);
			test = line;
  	}
  	recordCount = 0;
  	businessCount += 1;
  }
  Customer Victor = Customer("Victor", allBusinesses[0]);
  Victor.getBusinessProducts();
  Customer Bob = Customer("Bob", allBusinesses[1]);
  Bob.getBusinessProducts();
  cout << "Victor ";
  Victor.buyProduct(1);
  cout << "Victor ";
  Victor.buyProduct(1);
  cout << "Bob ";
  Bob.buyProduct(2);
}
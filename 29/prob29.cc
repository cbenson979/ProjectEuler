#include "math.h"
#include <iostream>
#include <vector>

using namespace std;

void powerLoop(int a, vector<long long int>* vect) {	
	for (int b=2; b<=100; b++) {
		long long int tempResult = pow(a,b);
		bool inIt = false;
		for (int j=0; j<vect->size();j++) {
			if (tempResult == vect->at(j)) {
				inIt = true;
				break;
			}
		}
		if (inIt == false)
			vect->push_back(tempResult);
	}		
}

int main() {
	vector<long long int>* theNums = new vector<long long int>();
	
	powerLoop(4, theNums);

	for (int j=0; j<theNums->size(); j++) {
		cout<<theNums->at(j)<<endl;
	}

	return 0;
}
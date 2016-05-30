#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int factorGen(int num) {
	vector<int> theFactors;
	
	int upperLimit = num/2;
	
	theFactors.push_back(1);
	theFactors.push_back(num);
	for (int i=2; i<=upperLimit; i++) {
		if (num%i == 0) {
			int otherNum = num/i;
			if (otherNum < i) {
				break;
			}
			if (otherNum == i) {
				theFactors.push_back(i);
				break;
			}
			theFactors.push_back(i);
			theFactors.push_back(otherNum);
		} 
	}
	return theFactors.size();
}

int main() {
	
	bool stopLoop = false;
	int minFactors = 500;
	
	int currentTrig = 1;
	int currentNum = 2;	
	while (!stopLoop) {
		currentTrig += currentNum;
		currentNum++;
		cout<<currentTrig<<endl;
		int numFactors = factorGen(currentTrig);
		cout<<numFactors<<endl;
		if (numFactors > minFactors) {
			stopLoop = true;
			cout<<"The answer is: "<<currentTrig<<endl;
			break;
		}
	}
	
	return 0;
}
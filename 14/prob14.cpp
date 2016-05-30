#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int firstNum = 2;
	double lastNum = 1000000;
	vector<long long int> iterationRecord;
	for (long long int startingNumber = firstNum; startingNumber < lastNum+1;startingNumber++) {
		long long int tempNum = startingNumber;
		long long int iterationCounter = 1;
		while (tempNum != 1) {
			iterationCounter++;
// 			cout<<tempNum<<",";
			// check if it is odd or even and apply method
			if (tempNum%2 == 1) {
				// odd condition
				tempNum = 3*tempNum + 1;
			}
			else if (tempNum%2 == 0) {
				// even condition
					tempNum = tempNum/2;			
			}
			else {
				cout<<"Error: Strange logical condition."<<endl;
				cout<<"mod result for "<<tempNum<<": "<<tempNum%2<<endl;
				break;
			}
		}
// 		cout<<"1"<<endl;
		cout<<"Starting Number:"<<startingNumber<<"; Number of Iterations: "<<iterationCounter<<endl;
		iterationRecord.push_back(iterationCounter);
	}
	
	long long int numIterss = 0;
	long long int tempMax = 0;
	for (int i=0; i<iterationRecord.size();i++) {
		if (iterationRecord[i] > tempMax) {
			tempMax = i+firstNum;
			numIterss = iterationRecord[i];
			cout<<"A new Num: "<<numIterss<<" at "<<tempMax<<endl;
		}
	}
	cout<<"The answer is: "<<tempMax<<" With "<<numIterss<<" iterations!"<<endl;
	
}
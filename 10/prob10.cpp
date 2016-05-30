#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

bool isPrime(long long int numm) {
// 	long long int upLimit = numm;
	
	long long int upLimit = ceil(pow(numm,0.5)*1.1);
	
	// loop over all the ints up to the limit (only evens)
	for (int i=2; i<upLimit; i++) {
		if (numm % i != 0) {
			continue;
		} else {
			return false;
		}
		
	}
	return true;
}

int main() {
	int upperLim = 10;

	long long int runningSum = 0;
	
	for (int i=0; i<upperLim; i++) {
		bool resultt = isPrime(i);
		if (resultt)  {
			runningSum += i;
			cout<<i<<endl;
		}
	}
	
	cout<<"The answer is: "<<runningSum<<endl;
	return 0;
}



#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

bool isPrime(long long int numm) {
	long long int upLimit = numm;
	
// 	if (numm > 100) {
// 		upLimit = ceil(pow(numm,0.5));
// 	}

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
	int nth_Prime = 10001;
	
	int primeCount = 0;
	long long int current_number = 1;
	while	(primeCount < nth_Prime){
		current_number++;
// 		cout<<current_number<<endl;
		bool primeResult = isPrime(current_number);
		if (primeResult) {
			primeCount++;
			cout<<primeCount<<" "<<current_number<<endl;
		}
	}

	return 0;
}



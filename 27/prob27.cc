#include <iostream>
#include "math.h"

using namespace std;

bool isPrime(int num) {
	if (num <= 1) {
		return false;
	} else if (num == 2) {
		return true;
	} else if (num % 2 == 0) {
		return false;
	} else {
		bool prime = true;
		int divisor = 3;
		double num_d = (double) num;
		int upperLimit = (int) sqrt(num_d);
		while (divisor <= upperLimit){
			if (num % divisor == 0) {
				prime = false;
				break;
			}
			divisor += 2;
		}
		return prime;
	}
}

int consecutivePrimes(int a, int b) {
 int consecPrimes = 0;
 int n = 0;
 bool lastPrime = true;
 int tempNum = 0;
 while (n < 1000) {
 		tempNum = pow(n,2) + a*n + b;
 		if (isPrime(tempNum)) {
 			consecPrimes += 1;
 			n++;
 		} else {
 		break;
 		}
 	}
	return consecPrimes;
}

int main () {
	// loop over b then a
	int mostConsec = 0;
	int tempConsec = 0;
	for (int b=-1000; b<1001; b++) {
		for (int a=-999; a<1000; a++){
			tempConsec = consecutivePrimes(a,b);
			if (tempConsec > mostConsec) {
				mostConsec = tempConsec;
				cout<<mostConsec<<", a:"<<a<<", b:"<<b<<", a*b:"<<a*b<<endl;
			}
		}
	}

	
	return 0;
}



#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  cout << "Hello World!" << endl;
	
	long long int runningSum1 = 0;
	long long int runningSum2 = 0;
	
	int maxNum = 100;
	for (int i=1; i<=maxNum; i++) {
		runningSum1 += pow(i,2);
		runningSum2 += i;
	}
	runningSum2 = pow(runningSum2,2);
	
	long long int differ = runningSum2 - runningSum1;
	
	cout<<"Sum1 = "<<runningSum1<<endl;
	cout<<"Sum2 = "<<runningSum2<<endl;
	cout<<"diff = "<<differ<<endl;
	return 0;
}
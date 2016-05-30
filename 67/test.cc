#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<int> summedRowCalc(vector<int> bottom, vector<int> top)
{
	// we know stepping backwards that bottom should always have a length of +1 rel to top.
	vector<int> result;
	
	for (int iTop=0;iTop<top.size();iTop++)
	{
		if ((top[iTop]+bottom[iTop])>(top[iTop]+bottom[iTop+1])) // Left number wins on bottom.
		{
			result.push_back(top[iTop]+bottom[iTop]);
		} else  if ((top[iTop]+bottom[iTop])<(top[iTop]+bottom[iTop+1])) {
			result.push_back(top[iTop]+bottom[iTop+1]);
		} else if ((top[iTop]+bottom[iTop])==(top[iTop]+bottom[iTop+1])) {
			cout<<"Errr...."<<endl;
		}
	}
	
	return result;
}


int main() 
{
	string getContent;
	ifstream tempFile("p067_triangle.txt");
	
// 	int currentIndex = 0;
// 	long int tempSum = 0;
	int rowCounter = 0;
	
	// data set
	vector<vector<int> > dataSet;
	
	if (tempFile.is_open()) 
	{
		while(!tempFile.eof()) {
			rowCounter++;
			
			getline(tempFile, getContent);
// 			cout<<getContent<<endl;
			stringstream ss;
			ss<<getContent;
			
			vector<int> tempNumbers;
			
			// This puts the numbered rows into vectors
			int number;
			while (!ss.eof()) {
				if (ss.peek() != '.') {
					ss >> number;
					tempNumbers.push_back(number);
				} else { ss.get(); }
			}

			dataSet.push_back(tempNumbers);
			
		}
		
		vector<int> prevResult = summedRowCalc(dataSet[dataSet.size()-1], dataSet[dataSet.size()-2]);
		// Now check out the rows in reverse....
		for (int i=dataSet.size()-2;i>0;i--)
		{
			prevResult = summedRowCalc(prevResult, dataSet[i-1]);
		}	
		
		// Now print the result!
		for (int cow=0;cow<prevResult.size();cow++)
		{
			cout<<prevResult[cow]<<endl;
		}

	}
	
	return 0;
}
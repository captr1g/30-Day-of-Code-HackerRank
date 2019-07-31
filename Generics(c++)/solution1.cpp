#include <iostream>
#include <vector>
#include <string>
/*  a single generic function named printArray; this function must take an array of 
 generic elements as a parameter (the exception to this is C++, which takes a vector)*/
using namespace std;
// if operator '>' is overloaded 
template <typename T> 
  
void printArray(vector<T> myvector) 
{ 
    for(int i=0;i<myvector.size();i++){
        cout<<myvector[i]<<endl;
    } 
}
/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}

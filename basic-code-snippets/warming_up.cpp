#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
  string line;
  unsigned long counter = 0;
  ifstream inFile("file1.txt");
  ofstream outFile("file2.txt");
  while(getline(inFile, line)) { 
    outFile << ++counter << ": " << line << endl;
  }
}
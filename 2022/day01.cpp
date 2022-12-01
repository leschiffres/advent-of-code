#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

string trim(string& str)
{
    str.erase(str.find_last_not_of(' ')+1);         //suffixing spaces
    str.erase(0, str.find_first_not_of(' '));       //prefixing spaces
    return str;
}

int max(int a, int b){
  if(a>b){
    return a;
  }
  else{
    return b;
  }
}

bool comp(int i, int j) { return i > j; }

void first_part(){
  string line;
  unsigned long counter = 0;
  ifstream inFile("input/day01.txt");
  int n = 0, total_calories = 0, max_calories = 0;
  while(getline(inFile, line)) { 
    if(trim(line).length() > 0){
      n = stoi(line);
      total_calories += n;
    }
    else{
      max_calories = max(max_calories, total_calories);
      total_calories = 0;
    }
  }
  cout << max_calories << endl; 
}

void second_part(){
  string line;
  unsigned long counter = 0;
  ifstream inFile("input/day01.txt");
  int n = 0, total_calories = 0;
  vector<int> v;

  while(getline(inFile, line)) { 
    if(trim(line).length() > 0){
      n = stoi(line);
      total_calories += n;
    }
    else{
      v.push_back(total_calories);
      total_calories = 0;
    }
  }
  sort (v.begin(), v.begin() + v.size(), comp);
  cout << v[0] + v[1] + v[2] << endl; 
}

int main() {
  // part 1
  first_part();

  // part 2
  second_part();
}
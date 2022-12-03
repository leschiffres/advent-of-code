#include <iostream>
#include <string>
#include <fstream>
#include <set>
#include <map>

using namespace std;

set<char> intersection(string& s1, string& s2 ){
    set<char> inter;
    for(int i = 0; i < s1.size(); i++){
        for(int j = 0; j < s2.size(); j++){
            if(s1[i] == s2[j]){
                inter.insert(s1[i]);
            }
        }
    }
    return inter;
}

string set_to_string(set<char>& myset){
    set<char>::const_iterator setIterator;
    string s;
    for(setIterator = myset.begin(); setIterator != myset.end(); setIterator++) {
        s+= *setIterator;
    }
    return s;
}

void first_part(map<char, int>& priorities){
    string line;
    ifstream inFile("input/day03.txt");
    string s1, s2;
    string str;
    
    set<char> s;

    int priorities_sum = 0;

    while(getline(inFile, line)) { 
        s1 = "";
        s2 = "";
        for(int i = 0; i < line.size(); i++){
            if (i < line.size()/2){
                s1 += line[i];
            }
            else{
                s2 += line[i];
            }
        }
        s = intersection(s1,s2);
        str = set_to_string(s);

        for(int i = 0; i < str.size(); i++){
            priorities_sum += priorities[str[i]];
        }
    }
    // cout << s1 << endl; 
    // cout << s2 << endl; 
    
    // cout << str << endl; 
    
    cout << priorities_sum << endl; 
}

void second_part(map<char, int>& priorities){
    string line;
    ifstream inFile("input/day03.txt");
    
    string s1, s2, s3, str;
    set<char> s;

    int priorities_sum = 0;

    while(getline(inFile, line)) { 
        s1 = line;
        getline(inFile, line);
        s2 = line;

        s = intersection(s1,s2);
        str = set_to_string(s);

        getline(inFile, line);
        s3 = line;

        s = intersection(str,s3);
        str = set_to_string(s);

        for(int i = 0; i < str.size(); i++){
            priorities_sum += priorities[str[i]];
        }
    }
    cout << priorities_sum << endl;
    
}

int main() {
  string letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  map<char, int> priorities;
  for(int i=0; i<letters.size(); i++){
    priorities[letters[i]] = i+1;
    // cout << letters[i] << ": " << priorities[letters[i]] << endl;
  }

  // part 1
  first_part(priorities);

  // part 2
  second_part(priorities);
}
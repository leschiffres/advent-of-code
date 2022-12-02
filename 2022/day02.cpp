#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int get_score(char a, char b){
    if (a == 'A'){ // rock
        if (b == 'X'){ // rock
            return 1 + 3;
        }
        else if (b == 'Y'){ // paper
            return 2 + 6;
        }
        else{ //scissors
            return 3;
        }
    }
    else if (a == 'B'){
        if (b == 'X'){ // rock
            return 1;
        }
        else if(b == 'Y'){// paper
            return 2 + 3;
        }
        else{ //scissors
            return 3 + 6;
        }
    }
    else{ //scissors
        if (b == 'X'){ // rock
            return  1 + 6;
        }
        else if (b == 'Y') {// paper
            return 2;
        }
        else{ // scissors
            return 3 + 3;
        }
    }
}

void first_part(){
    string line;
    ifstream inFile("input/day02.txt");
    int n = 0, total_score = 0;
    while(getline(inFile, line)) { 
        char a = line[0], b = line[2];
        total_score += get_score(a,b);
    }
    cout << total_score << endl; 
}

void second_part(){
    string line;
    ifstream inFile("input/day02.txt");
    int n = 0, total_score = 0;
    while(getline(inFile, line)) { 
        char a = line[0], result = line[2], b = ' ';

        if (a == 'A'){ // rock
            if (result == 'X'){ // lose
                b = 'Z';
            }
            else if (result == 'Y'){ // draw
                b = 'X';
            }
            else{ //win
                b = 'Y';
            }
        }
        else if (a == 'B'){
            if (result == 'X'){ // lose
                b = 'X';
            }
            else if(result == 'Y'){// draw
                b = 'Y';
            }
            else{ //win
                b = 'Z';
            }
        }
        else{ //scissors
            if (result == 'X'){ // lose
                b = 'Y';
            }
            else if (result == 'Y') {// draw
                b = 'Z';
            }
            else{ // win
                b = 'X';
            }
        }
        
        total_score += get_score(a,b);
    }
    cout << total_score << endl; 
}

int main() {
  // part 1
  first_part();

  // part 2
  second_part();
}
#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <vector>
#include <chrono>
#include <unordered_map>


using namespace std;

int d01pt1(const string& folder_path, const string& filename) {
    cout << endl << "Day 01 - Pt1: " << filename << endl;

    string file_path = folder_path + filename;

    vector<int> a = {1,2,3};
    ifstream inputFile(file_path);

    if (!inputFile) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    int sum = 0;
    string line;
    while(getline(inputFile, line)) {
        char d1 = '\0';
        char d2 = '\0';

        for (auto it = line.begin(); it != line.end(); it++) {
            if (isdigit(*it)) {
                d1 = *it;
                break;
            }
        }
        string::reverse_iterator rit;
        for (rit = line.rbegin(); rit != line.rend(); rit++) {
            if (isdigit(*rit)) {
                d2 = *rit;
                break;
            }
        }

        string number_string;
        number_string += d1;
        number_string += d2;
        int number = stoi(number_string);
        sum += number;
        //cout << number << endl;
    }

    return sum;
}

int d01pt2(const string& folder_path, const string& filename) {
    cout << endl << "Day 01 - Pt2: " << filename << endl;

    string file_path = folder_path + filename;

    vector<int> a = {1,2,3};
    
    ifstream inputFile(file_path);

    if (!inputFile) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    int result = 0;

    unordered_map<string, int> numstr;
    numstr["one"] = '1';
    numstr["two"] = '2';
    numstr["three"] = '3';
    numstr["four"] = '4';
    numstr["five"] = '5';
    numstr["six"] = '6';
    numstr["seven"] = '7';
    numstr["eight"] = '8';
    numstr["nine"] = '9';

    string line;
    while(getline(inputFile, line)) {
        char d1 = '\0';
        char d2 = '\0';

        for (auto it = line.begin(); it != line.end(); it++) {
            if (isdigit(*it)) {
                d1 = *it;
                break;
            } else {
                for (auto& [nstr, nr] : numstr) {
                    auto index = distance(line.begin(), it);
                    if (index + nstr.length() > line.length()) {
                        continue;
                    }
                    string sub = line.substr(index, nstr.length());
                    if (sub == nstr) {
                        d1 = nr;
                        goto break_left;
                    }
                }
            }
        }
        break_left:
        string::reverse_iterator rit;
        for (rit = line.rbegin(); rit != line.rend(); rit++) {
            if (isdigit(*rit)) {
                d2 = *rit;
                break;
            } else {
                bool br = false;
                for (auto& [nstr, nr] : numstr) {
                    auto rindex = distance(line.rbegin(), rit);
                    auto index = line.length() - rindex - nstr.length();
                    if (line.length() < rindex + nstr.length()) {
                        continue;
                    }
                    auto sub = line.substr(index, nstr.length());
                    if (index > 0 && sub == nstr) {
                        d2 = nr;
                        goto break_right;
                    }
                }
            }
        }
        break_right:
        string number_string;
        number_string += d1;
        number_string += d2;
        int number = stoi(number_string);
        result += number;
                
    }

    return result;
}
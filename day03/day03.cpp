#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <functional>
#include <algorithm>

#include "util.hpp"

using namespace std;


bool check_char(vector<string> lines, int i, int j) {
    if (i < 0 || j < 0) return false;
    if (i >= lines.size() || j >= lines[i].size()) return false;
    char c = lines[i][j];
    if (isdigit(c)) return false;
    if (c == '.') return false;

    return true;
}

bool check_char2(vector<string> lines, int i, int j) {
    if (i < 0 || j < 0) return false;
    if (i >= lines.size() || j >= lines[i].size()) return false;
    char c = lines[i][j];
    if (c == '*') return true;
    return false;
}

int d03pt1(const string& folder_path, const string& filename) {
    cout << endl << "Day 03 - Pt1: " << filename << endl;

    string file_path = folder_path + filename;
    vector<string> lines;

    fstream file(file_path);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << file_path << endl;
        return 1;
    }

    int result = 0;
    string line;
	while (getline(file, line)) {
		lines.push_back(line);
	}

    file.close();

    for (int i = 0; i < lines.size(); i++) {
        line = lines[i];
        string number = "";

        for (int j = 0; j < line.size(); j++) {
            char c = line[j];
            if (isdigit(c)) {
                number.push_back(c);
            }
            
            if (number != "" && (!isdigit(c) || j == line.length() - 1)) {
                int nr = stoi(number);
                int l = number.length();
                number = "";
                if (j == line.size() - 1 && isdigit(c)) j = line.size();

                bool found = false;
                for (int ii = i - 1; ii <= i + 1 && !found; ii++) {
                    for (int jj = j - l - 1; jj <= j && !found; jj++) {
                        auto b = check_char(lines, ii, jj);
                        if (b) {
                            result += nr;
                            //cout << nr << endl;
                            found = true;
                        }
                    }
                }
            }
        }
    }

    return result;
}

int d03pt2(const string& folder_path, const string& filename) {
    cout << endl << "Day 03 - Pt2: " << filename << endl;

    string file_path = folder_path + filename;

    fstream file(file_path);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << file_path << endl;
        return 1;
    }

    int result = 0;
    string line;
    vector<string> lines;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    file.close();

    vector<set<tuple<int, int>>> coords;
    vector<int> numbers;

    for (int i = 0; i < lines.size(); i++) {
        line = lines[i];
        string number = "";

        for (int j = 0; j < line.size(); j++) {
            char c = line[j];
            if (isdigit(c)) {
                number.push_back(c);
            }

            if (number != "" && (!isdigit(c) || j == line.length() - 1)) {
                int nr = stoi(number);
                int l = number.length();
                number = "";
                if (j == line.size() - 1 && isdigit(c)) j = line.size();

                set<tuple<int, int>> co;
                for (int ii = i - 1; ii <= i + 1; ii++) {
                    for (int jj = j - l - 1; jj <= j; jj++) {
                        auto b = check_char2(lines, ii, jj);
                        if (b) {
                            co.insert(tuple(ii, jj));
                        }
                    }
                }
                if (co.size() > 0) {
                    coords.push_back(co);
                    numbers.push_back(nr);
                }
            }
        }
    }

    for (int i = 0; i < coords.size(); i++) {
        for (int j = 0; j < coords.size(); j++) {
            if (i != j && i < j) {
                set<tuple<int, int>> inter;
                set_intersection(
                    coords[i].begin(), coords[i].end(),
                    coords[j].begin(), coords[j].end(),
                    inserter(inter, inter.begin()));

                if (inter.size() > 0) {
                    result += numbers[i] * numbers[j];
                }
            }
        }
    }
    return result;
}

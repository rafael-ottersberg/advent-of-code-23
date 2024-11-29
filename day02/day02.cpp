#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <functional>
#include <algorithm>

#include "util.hpp"

using namespace std;

int d02pt1(const string& folder_path, const string& filename) {
    cout << endl << "Day 02 - Pt1: " << filename << endl;

    string file_path = folder_path + filename;

    fstream file(file_path);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << file_path << endl;
        return 1;
    }

    string line;

    int max_red = 12;
    int max_green = 13;
    int max_blue = 14;

    int id = 1;
    int result = 0;

    while (getline(file, line)) {
        int red = 0, green = 0, blue=0;

        auto label_games = split(line, ": ");
        auto games = split(label_games[1], "; ");

        unordered_map<string, function<void(int)>> check_max_color;

        check_max_color["red"] = [&red](int nr) {
            red = max(red, nr);
        };
        check_max_color["green"] = [&green](int nr) {
            green = max(green, nr);
        };
        check_max_color["blue"] = [&blue](int nr) {
            blue = max(blue, nr);
        };
        

        for (auto game : games) {
            for (auto ball : split(game, ", ")) {
                auto number_color = split(ball, " ");
                int number = stoi(number_color[0]);
                auto color = number_color[1];
                check_max_color[color](number);
            }
        }

        // cout << "Red: " << red << ", Green: " << green << ", Blue: " << blue << endl;

        if (blue <= max_blue && red <= max_red && green <= max_green) {
            result += id;
        }
        id++;
    }

    file.close();

    return result;
}

int d02pt2(const string& folder_path, const string& filename) {
    cout << endl << "Day 02 - Pt2: " << filename << endl;

    string file_path = folder_path + filename;

    fstream file(file_path);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << file_path << endl;
        return 1;
    }

    string line;

    int result2 = 0;

    while (getline(file, line)) {
        int red = 0, green = 0, blue=0;

        auto label_games = split(line, ": ");
        auto games = split(label_games[1], "; ");

        unordered_map<string, function<void(int)>> check_max_color;

        check_max_color["red"] = [&red](int nr) {
            red = max(red, nr);
        };
        check_max_color["green"] = [&green](int nr) {
            green = max(green, nr);
        };
        check_max_color["blue"] = [&blue](int nr) {
            blue = max(blue, nr);
        };
        

        for (auto game : games) {
            for (auto ball : split(game, ", ")) {
                auto number_color = split(ball, " ");
                int number = stoi(number_color[0]);
                auto color = number_color[1];
                check_max_color[color](number);
            }
        }

        result2 += red * blue * green;
    }

    file.close();

    return result2;
}

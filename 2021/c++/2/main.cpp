#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

std::vector<string> read_file(string filename) {

        std::vector<string> return_vec = {};
        ifstream file;
        string line;
        file.open(filename);
        while ( getline( file, line ) ){

                return_vec.push_back( line );

        }
        return return_vec;

}

string split_word(string str){

	int string_length = str.length();
	string word = "";

	for (int i = 0; i < string_length; i++){

		if (str[i] == ' ' or i == string_length-1){

			return word;

		}else {

			word += str[i];

		}

	}
	return word;
}

int split_value(string str){

	int string_length = str.length();
	string value = "";
	bool getting = false;

	for (int i = 0; i < string_length; i++){
	
		if (getting == true){
			value += str[i];
		}
		if (str[i] == ' ') { getting = true; };

	}
	
	int value_int = std::stoi(value);

	return value_int;

}

int solve_first_problem(vector<string> data){

	int depth = 0;
	int h_pos = 0;

	for (int i = 0; i < data.size(); i++){
	
		string current_element = data[i];
		//string word;

		//istringstream iss(current_element);
		//iss >> word;
		//cout << word << endl;
		
		string word = split_word(data[i]);
		int value = split_value(data[i]);

		if (word == "forward") { h_pos += value; };
		if (word == "down") { depth += value; };
		if (word == "up") { depth -= value; };

	}

	return depth*h_pos;
}

int solve_second_problem(vector<string> data){

	int depth = 0;
	int h_pos = 0;
	int aim = 0;

	for (int i = 0; i < data.size(); i++){

		string current_element = data[i];

		string word = split_word(data[i]);
		int value = split_value(data[i]);

		if (word == "forward") { h_pos += value; depth += aim * value; };
		if (word == "down") { aim += value; };
		if (word == "up") { aim -= value; };

	}

	return depth*h_pos;
}

int main(){

	vector<string> problem_data = read_file("../data/2.txt");
	cout << "The answer to the first problem is: "; cout << solve_first_problem(problem_data) << endl;
	cout << "The answer to the second problem is: "; cout << solve_second_problem(problem_data) << endl;
	
}

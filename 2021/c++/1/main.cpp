#include<iostream>
#include<vector>
#include<fstream>
#include<string>
using namespace std;

std::vector<int> read_file_to_int(string filename) {

	std::vector<int> return_vec = {};
	ifstream file;
	string line;
	file.open(filename);
	while ( getline( file, line ) ){
	
		int append = std::stoi( line );
		return_vec.push_back( append );

	}
	return return_vec;

}

int solve_first_problem(vector<int> data) {

	int bigger_than = 0;
	for (int i = 0; i < data.size(); i++){
		int current_element = data[i];
		if (i != 0 ){
			int previous_element = data[i-1];
			if (current_element > previous_element) { bigger_than++; };
		}
	}
	return bigger_than;
}

std::vector<int> solve_second_problem(vector<int> data){

	int counter = 0;

	std::vector<int> sums = {};

	for (int i = 0; i < data.size(); i++){
	
		if (i >= 2){
			int append = data[i-2] + data[i-1] + data[i];
			sums.push_back(append);

		}

	}

	return sums;

}

int main(){
	
	std::vector<int> problem_data = read_file_to_int("../data/1.txt");
	std::vector<int> test_data = {199, 200, 208, 210, 200, 207, 240, 269, 260, 263};

	std::vector<int> second_answer_data = solve_second_problem(problem_data);

	int second_answer = solve_first_problem(second_answer_data);

	cout << second_answer << endl;

		
}

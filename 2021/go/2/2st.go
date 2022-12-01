package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path);
	if err != nil {
		return nil, err;
	};
	defer file.Close()

	var lines []string;
	scanner := bufio.NewScanner(file);
	for scanner.Scan() {
		
		lines = append(lines, scanner.Text());

	}
	return lines, scanner.Err()
}

func check_error(e error){

	if e != nil {
		panic(e);
	};

}

func solve_first_problem(data []string) (int){

	var depth int = 0;
	var h_pos int = 0;

	for i := 1; i < len(data); i++ {

		var element string = data[i];
		element_array := strings.Split(element, " ");
		var word string = string(element_array[0]);
		value, err := strconv.Atoi(element_array[1]); 
		check_error(err);

		var check_forward bool = word == "forward";
		var check_down bool = word == "down";
		var check_up bool = word == "up";

		if check_forward == true {
			h_pos += value;
		}
		if check_up == true{
			depth -= value;
		}
		if check_down == true{
			depth += value;
		}
	}

	return h_pos*depth;
}

func solve_second_problem(data []string) (int64){

	var depth int64 = 0;
	var h_pos int64 = 0;
	var aim int64 = 0;

	var counter int = 0;

	for counter < len(data) {

		var element string = data[counter];
		element_array := strings.Split(element, " ");
		var word string = string(element_array[0]);
		value, err := strconv.ParseInt(element_array[1], 0, 64);
		check_error(err);
		
		var check_forward bool = word == "forward";
		var check_down bool = word == "down";
		var check_up bool = word == "up";

		if check_forward { 

			h_pos += value;
			depth += value * aim;
		};

		if check_down { aim += value; };
		if check_up { aim -= value; };

		counter++;
	}

	return depth*h_pos;

}

func main(){

	final_array, err := readLines("data/2st.txt");
	check_error(err);

	var first_answer int = solve_first_problem(final_array);
	fmt.Println(first_answer);

	var second_answer int64 = solve_second_problem(final_array);
	fmt.Println(second_answer);

}

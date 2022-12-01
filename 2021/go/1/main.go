package main;

import "fmt";
import "os";
import "bufio"
import "strconv"

func read_problem_file(path string) ([]int, error) {

	file, err := os.Open(path);
	check_error(err);
	defer file.Close();

	var lines []int;
	scanner := bufio.NewScanner(file);
	for scanner.Scan(){

		var appnd_string string = scanner.Text();
		appnd, err := strconv.ParseInt(appnd_string, 0, 64);
		check_error(err);

		lines = append(lines, int(appnd));

	}
	return lines, scanner.Err();
}

func check_error(e error){

	if (e != nil) { panic(e); };

}

func solve_first_problem(data []int) (int) {

	var bigger_than int = 0;

	for i:= 0; i < len(data); i++{

		if (i != 0){

			if (data[i] > data[i-1]){

				bigger_than++;

			}
		}
	}
	return bigger_than;
}

func return_second_problem_data(data []int) ([]int){

	var sums []int;

	for i := 0; i < len(data); i++{

		if (i >= 2){

			var sum int = data[i-2] + data[i-1] + data[i];
			sums = append(sums, sum);
		}
	}
	return sums;
}

func main(){
	
	//var test_data []int = []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263};
	problem_data, err := read_problem_file("../data/1st.txt");
	check_error(err);

	var second_problem_data []int = return_second_problem_data(problem_data);
	fmt.Println(solve_first_problem(second_problem_data));

}

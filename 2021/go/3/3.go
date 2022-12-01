package main;

import "fmt"
import "bufio"
import "os"
import "strconv"


func read_file(path string) ([]string, error) {

	file, err := os.Open(path);
	if err != nil {
		return nil, err;
	}
	defer file.Close();

	var lines []string;
	scanner := bufio.NewScanner(file);
	for scanner.Scan() {

		lines = append(lines, scanner.Text());

	}
	return lines, scanner.Err();

}

func check_error(e error){

	if e != nil{
		panic(e);
	}

}

func return_digit_list(data []string) ([][]string) {

	var counter int = 0;

	var return_list [][]string;

	for counter < len(data){

		var element string = data[counter];
		chars := []rune(element);

		var tamanho_do_numero int = len(chars);
		if (counter == 0){

			for digito := 0; digito < tamanho_do_numero; digito++{

				var lista_digito_ordem []string;
				return_list = append(return_list, lista_digito_ordem);

			}
		}

		var i int = 0;
		for i<len(chars) {
			char := string(chars[i]);
			return_list[i] = append(return_list[i], char);
			i++;

		}
		counter++

	}
	return return_list;
}

func solve_first_problem(digit_lists [][]string) (string, string){

	var gamma_rate string;
	var epsilon_rate string;

	for counter := 0; counter < len(digit_lists); counter++{

		var digit_list []string = digit_lists[counter];
		var ones int = 0;
		var zeroes int = 0;
		for i:= 0; i < len(digit_list); i++{
			if(digit_list[i] == "0") {zeroes += 1};
			if(digit_list[i] == "1") {ones += 1};
		}
		if (ones > zeroes) { gamma_rate = gamma_rate + "1"; epsilon_rate = epsilon_rate + "0" };
		if (zeroes > ones) { gamma_rate = gamma_rate + "0"; epsilon_rate = epsilon_rate + "1" };

	}
	return gamma_rate, epsilon_rate;
}

func binary_to_decimal(bin_num string) (int64){

	num, err := strconv.ParseInt(bin_num, 2, 64);
	check_error(err);
	return num;

}

func return_answer(gamma_rate int, epsilon_rate int) (int) { return gamma_rate * epsilon_rate }

func return_most_common_digits(digit_list [][]string) ([]string, []string){

	var most_common []string;
	var least_common []string;

	for i := 0; i < len(digit_list); i++{

		var element_list []string = digit_list[i];

		var zeroes int = 0;
		var ones int = 0;
		
		for k := 0; k < len(element_list); k++{

			var element string = element_list[k];
			if (element == "0") { zeroes++ };
			if (element == "1") {ones++ };

		}

		if (zeroes > ones) { most_common = append(most_common, "0"); least_common = append(least_common, "1") };
		if (ones > zeroes) { most_common = append(most_common, "1"); least_common = append(least_common, "0") };
		if (ones == zeroes) { most_common = append(most_common, "1"); least_common = append(least_common, "0") };

	}

	return most_common, least_common

}

func get_oxygen_rate(common_digits []string, uncommon_digits []string, overall_digits []string) ([]string){

	for i := 0; i < len(common_digits); i++{
	
		var common_digit string = common_digits[i];

		var temp_list []string = []string{};

		for k := 0; k < len(overall_digits); k++{

			var element string = overall_digits[k];
			
			var digit string = string(element[i]);

			if (digit == common_digit) {

				temp_list = append(temp_list, element);

			}

		}
		overall_digits = temp_list;
		fmt.Println(overall_digits);
		
		new_digit_list := return_digit_list(overall_digits);
		common_digits, uncommon_digits = return_most_common_digits(new_digit_list);

	}
	fmt.Println(uncommon_digits);

	return overall_digits;
		
}

func get_coTwo_rate(common_digits []string, uncommon_digits []string, overall_digits []string) ([]string) {

	for i := 0; i < len(uncommon_digits); i++{
	
		var uncommon_digit string = uncommon_digits[i];

		var temp_list []string = []string{};

		for k := 0; k < len(overall_digits); k++{

			var element string = overall_digits[k];

			var digit string = string(element[i]);

			if (digit == uncommon_digit) {

				temp_list = append(temp_list, element);

			}
			fmt.Println("Uncommon overall_digits: ");
			fmt.Println(overall_digits);
		}
		if (len(temp_list) > 0){ overall_digits = temp_list };
		//overall_digits = temp_list;

		new_digit_list := return_digit_list(overall_digits);
		common_digits, uncommon_digits = return_most_common_digits(new_digit_list);

	}
	fmt.Println(common_digits);

	return overall_digits;

}

func main(){

	//test_array, err := read_file("../data/3st_test.txt");
	test_array, err := read_file("../data/3st.txt");
	check_error(err);
	
	var digit_list [][]string = return_digit_list(test_array);

	most_common_digits, least_common_digits := return_most_common_digits(digit_list);
	fmt.Println(least_common_digits);

	var oxygen []string = get_oxygen_rate(most_common_digits, least_common_digits, test_array);
	var coTwo []string = get_coTwo_rate(most_common_digits, least_common_digits, test_array);

	fmt.Println("Answers in binary: ");
	fmt.Println(oxygen);
	fmt.Println(coTwo);

	fmt.Println("Overall answer: ");
	var oxygen_int int64 = binary_to_decimal(oxygen[0]);
	var coTwo_int int64 = binary_to_decimal(coTwo[0]);
	fmt.Println(coTwo_int*oxygen_int);
}
